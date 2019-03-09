from lxml import etree
from xml.etree.ElementTree import iterparse


# coding: utf-8
from sqlalchemy import Table, Column,Integer,String,Float , DateTime, create_engine,MetaData,or_ 
from sqlalchemy.orm import mapper, sessionmaker

 
# import loadText as lt
import os
import pprint
import re
import os
import sys
import shutil
#from gensim import corpora,models,similarities
import itertools
import threading, time
from sets import Set
import cStringIO 
from lxml import etree, html
from xml.etree.ElementTree import iterparse
import HTMLParser
import datetime

import pandas as pd
import numpy as np
import colorsys

import threading, Queue 
# import xapian
# from xapian import SimpleStopper

import networkx as nx
from networkx.readwrite import json_graph


import json


singlelock = threading.Lock() 
html_parser = HTMLParser.HTMLParser()

entities = [   ('&-',''),   ('&|','')]


def create_text_db(text_folder):
    engine = create_engine('sqlite:///%s/W3C.db'%(text_folder), echo=True)
    metadata = MetaData(bind=engine)
    documents_table = Table('Messages', metadata,
                            Column('Id', String(150), primary_key=True),
                            Column('Subject', String ),
                            Column('Text', String),
                            Column('AuthorID', String),
                            Column('AuthorName', String),
                            Column('AuthorEmail', String),
                            Column('ThreadID', String),
                            Column('Date', DateTime),
                            Column('Type', String),
                            Column('ResponseTo', String),
                            Column('URL', String),
                            Column('Level', String),
                            Column ('SubjectChanged',String),
                            Column('FromOtherList', String)
                        )
    metadata.create_all()   




class Message(object):
    pass


def init():
    folder=os.path.join('')
    engine = create_engine('sqlite:///' + os.path.join(folder, 'w3c.db'), echo=False)
    metadata = MetaData(bind=engine)
    global Session
    Session=sessionmaker(bind=engine)

    global message_table
    message_table= Table('Messages', metadata, autoload=True)
    try:
        mapper(Message, message_table)
    except:
        pass


base='http://lists.w3.org/Archives/Public/public-html/{0}/{1}.html'
    


def create_threads(size=10):
    
    init()
    session=Session()
    messages=session.query(Message).all()
    # messages=session.query(Message).all()
    
    print len(messages)
    
    G=nx.DiGraph()
    for message in messages:
        if message.ResponseTo !='':
            G.add_node(message.ResponseTo, name=message.AuthorName[0:20])
            G.add_node(message.Id, name=message.AuthorName[0:20])
            G.add_edge(message.ResponseTo, message.Id)
    

    
    threads=nx.weakly_connected_component_subgraphs(G)
    threads=[t for t in threads if len(t)>size] 
    
    
    thread_info=[]
    for thread in threads:
        root=nx.topological_sort(thread)[0]
               
        m=session.query(Message).filter(or_(Message.Id==str(root), Message.ResponseTo==str(root)) ).first()
 
        thread_info.append((len(thread), m.Subject, root, thread ))
    
    
    
    return thread_info


def json_thread(size=100):
        
    threads=create_threads(size=size)
    
    
    for thread_size, thread_subject,  root, t_thread  in  threads:
        
        names= [d['name'] for n, d in t_thread.nodes(data=True)]
        unique_names=list(set(names))
        colors=pick_color(len(unique_names))
        col_pallette=dict(zip(unique_names, colors))
        
        for n,d in t_thread.nodes(data=True):
            d['color']=col_pallette[d['name']]
        
        
        # root=nx.topological_sort(t_thread)[0]
        file='%s_%s.json'%(thread_size, thread_subject)
        file=re.sub('/',':', file )
        
        data = json_graph.tree_data(t_thread,root=root)
        with open(os.path.join('json', file), 'w') as outfile:
            json.dump(data,outfile)
       
    

    

def pick_color(n=1):
    h = np.random.random() # use random start value
    
    golden_ratio_conjugate = 0.618033988749895
    hexcolors=[]
    for i in range(n):
        h += golden_ratio_conjugate
        h %= 1
     
        rgb_tuple=colorsys.hsv_to_rgb(h, .5, .95)
        rgb_tuple=tuple( map(lambda x: int(x*256), rgb_tuple))
        hexcolors.append('#%02x%02x%02x' % rgb_tuple)
    return hexcolors



# def hsv_to_rgb(h, s, v):
#
#   h_i = int(h*6)
#   f = h*6 - h_i
#   p = v * (1 - s)
#   q = v * (1 - f*s)
#   t = v * (1 - (1 - f) * s)
#
#   if h_i==0: r, g, b = v, t, p
#   if h_i==1: r, g, b = q, v, p
#   if h_i==2: r, g, b = p, v, t
#   if h_i==3: r, g, b = p, q, v
#   if h_i==4: r, g, b = t, p, v
#   if h_i==5: r, g, b = v, p, q
#   return int(r*256), int(g*256), int(b*256)







###################
#POPULATE     

class updater(threading.Thread):
   

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        
        
    def run(self):
        global files_being_proccessed
        while True:
            # gets the url from the queue
            doci = self.queue.get()
            period,id=doci.split('~')
            # save doc
            try:
                self.process(period, id)
            except:
                print 'error @', period, id
            
            # send a signal to the queue that the job is done
            self.queue.task_done()
            singlelock.acquire()
            print period, id, ' Done..'
           
           
            singlelock.release()
            # rem_files= [file for file in files_being_proccessed if file!=doc]
            # files_being_proccessed=rem_files
            # update_remaining(files_being_proccessed) 


    def process(self, period, id): 
        murl=base.format(period,"%04d" % (int(id)))
        print murl
        # xmldata=re.sub(r' (\w+)=[A-Z0-9-]+>','>',xmldata)
        # 
        # for before, after in entities:
        #     xmldata = xmldata.replace(before, after.encode('utf-8'))

        # xmldatafile=cStringIO.StringIO(xmldata)
        # context = etree.iterparse( xmldatafile, tag='DOC' ) 
        
        try:
            doc = html.parse(murl)
        
        except:
            print 'Missing page, ', id
            return
        
        comments=doc.getroot().xpath("//comment()")
        comments_dict={}
        for comment in comments:
                
            comment=html_parser.unescape(unicode(comment))
            
            tag=re.findall(r"(?<=\s).*?(?==)", comment)[0]
            value=re.findall(r"(?<=\").*?(?=\")", comment)[0]
            comments_dict[tag]= unicode(value)
            
        
        #ID
        m_id= comments_dict['id']
        # m_id= doc.getroot().xpath("//span[@id='message-id']/text()")[0]
#         try:
#             m_id= re.findall(r"(?<=<).*?(?=>)",m_id)[0]
#         except:
#             m_id=doc.getroot().xpath("//span[@id='message-id']/text()")[0].strip()
#
        #SUBJECT
        subject= comments_dict['subject']
        
        #subject=doc.getroot().xpath("//meta[@name='Subject']/@content")[0]
        
        #AUTHOR
        author_name=comments_dict.get('name', '')
        author_email=comments_dict['email']
        #author=doc.getroot().xpath("//meta[@name='Author']/@content")
        
        
        #DATE
        m_date=doc.getroot().xpath("//meta[@name='Date']/@content")[0]
        m_date_array=map(int, m_date.split('-'))
        
        m_date=datetime.date(m_date_array[0],m_date_array[1],m_date_array[2])
        print m_date
        
        
        #TYPE
        type_='Message'
        if '[BUG]' in subject:
            type_='Bug'
            
        
        #RESPONSETO
        responseto=comments_dict.get('inreplyto', '')
        
        
        
        #TEXT
        o_text= ' '.join(doc.getroot().xpath("//pre[@id='body']/text()"))
        
        text=re.sub(r'>+.*\n', '',o_text)
        text=re.sub(r'On.*wrote:\n', '',text)
        text=re.sub(r'\s+',' ', text)
        
        
        #URL
        
        
        
        i = message_table.insert()
        q = i.execute({'Id':m_id, 
                       'Text':text,
                       'AuthorEmail':author_email,
                       'AuthorName':author_name,
                       'Subject':subject,
                       'Date':m_date,
                       'Type': type_,
                       'ResponseTo':responseto,
                       'URL': murl})
        
        
        
        
        
        
        del doc 
        




        
        
if __name__ == '__main__':
            
 
    # files=[]
    file='htmlmessages.csv'
    message_list=pd.read_csv(file)
    queue = Queue.Queue()  
    
    for j in range(10):
       
        t=updater(queue)
        t.setDaemon(True)
        t.start()
        
  
    init()
    print 'starting' 
    ids=range(0,20)
    
    
    for i, r in message_list.iterrows():
        for j in range(r['count']):
             queue.put(r['period']+'~'+str(j))
             
    
    
    # for i in ids:
    #
    #         queue.put(str(ids[i])+'~'+str(ids[i]))
    
    
    
        
    queue.join()
    # db_pass.flush()
    # db_doc.flush()
    print 'Finished...', i
     
     







