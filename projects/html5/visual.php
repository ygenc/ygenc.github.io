
<!DOCTYPE html>
 <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
 <script src="http://d3js.org/d3.v3.min.js"></script>
 <script src="dndTree.js"></script>
 <script src="loadfiles.js"></script>
<meta charset="utf-8">


<style type="text/css">

  
	.node {
    cursor: pointer;
  }

  .overlay{
      background-color:#EEE;
  }
   
  .node circle {
    fill: #fff;
    stroke: steelblue;
    stroke-width: 1.5px;
  }
   
  .node text {
    font-size:10px; 
    font-family:sans-serif;
  }
   
  .link {
    fill: none;
    stroke: #ccc;
    stroke-width: 1.5px;
  }

  .templink {
    fill: none;
    stroke: red;
    stroke-width: 3px;
  }

  .ghostCircle.show{
      display:block;
  }

  .ghostCircle, .activeDrag .ghostCircle{
       display: none;
  }

</style>




<body onload="load_d3('<?php echo $_POST["browserpick"]; ?>')">

	<div id="top_name"></div>
	 
	<?php 
	
	 $name_num= $pieces = explode("_", $_POST["browserpick"]);
	
     echo '<h4> '.substr($name_num[1], 0, -5).' </h4>'; 		 
	 echo '('.$name_num[0].' messages )';
	 ?>
    
	<div id="tree-container"></div>
</body>
</html>