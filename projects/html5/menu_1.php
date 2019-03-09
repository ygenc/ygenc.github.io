<html>
<head>
 
 <script src="loadfiles.js"></script>
 
<title>HTML Frames Example - Menu 1</title>
<style type="text/css">
body {
	font-family:verdana,arial,sans-serif;
	font-size:10pt;
	margin:10px;
	background-color:#ff9900;
	}
.btn {
	  background: #8f8f8f;
	  background-image: -webkit-linear-gradient(top, #8f8f8f, #a8782f);
	  background-image: -moz-linear-gradient(top, #8f8f8f, #a8782f);
	  background-image: -ms-linear-gradient(top, #8f8f8f, #a8782f);
	  background-image: -o-linear-gradient(top, #8f8f8f, #a8782f);
	  background-image: linear-gradient(to bottom, #8f8f8f, #a8782f);
	  -webkit-border-radius: 8;
	  -moz-border-radius: 8;
	  border-radius: 8px;
	  font-family: Arial;
	  color: #ffffff;
	  font-size: 14px;
	  padding: 10px 18px 10px 20px;
	  text-decoration: none;
	}

.btn:hover {
	  background: #3cb0fd;
	  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);
	  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);
	  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);
	  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);
	  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);
	  text-decoration: none;
	}
.tb8 {
	width: 100px;
	height: 30;
	border: 1px solid #3366FF;
	border-left: 4px solid #3366FF;
}

</style>
</head>
<body>
<h3>Threads to visualize</h3>
<!-- <p><a href="white.html" target="content">White Page</a></p> -->

<form id="myform" action="visual.php" target = "content"  method="post">
<input list="browsers" id="browserpick"  name="browserpick" class="tb8" value="Select Thread"> 
<datalist  id="browsers">
	  
	  <?php
	  // Read directory, spit out links
	  if ($handle = opendir('json/')) {
	      while (false !== ($entry = readdir($handle))) {
	          if (  strpos($entry, ".") !==0){
	  	   // if ($entry != ".." && $entry != "."  && $entry != ".DS Store") {
	              echo '<option value="'.$entry.'">';
	          }
	      }
	      closedir($handle);
	  }
	  ?>
</datalist>
<input id="submitbutton" type="submit" class="btn">
</form>





<?php
if ($handle = opendir('json/')) {
    while (false !== ($entry = readdir($handle))) {
        if (  strpos($entry, ".") !==0){ 
			$files[] = $entry;
			//echo '<a href="javascript: submitform(\''.$entry.'\');" > '.htmlentities($entry).'</a><br>';
		}
    }
    closedir($handle);
}
rsort($files);
foreach ($files as &$entry){
	echo '<a href="javascript: submitform(\''.$entry.'\');" > '.htmlentities($entry).'</a><br>';
	}
?>


<!-- 


-->



<script type="text/javascript">
function submitform(val)
{
	console.log(val);
  document.getElementById('browserpick').value = val;	
  document.getElementById('submitbutton').click();
}
</script>


<!-- <h4>More Examples:</h4>
<a href="http://www.quackit.com/html/templates/frames/frames_example_1.html" target="_top">Example 1</a><br />
<a href="http://www.quackit.com/html/templates/frames/frames_example_2.html" target="_top">Example 2</a><br />
<a href="http://www.quackit.com/html/templates/frames/frames_example_3.html" target="_top">Example 3</a><br />
<a href="http://www.quackit.com/html/templates/frames/frames_example_4.html" target="_top">Example 4</a><br />
<a href="http://www.quackit.com/html/templates/frames/frames_example_5.html" target="_top">Example 5</a><br /> -->
</body>
</html>