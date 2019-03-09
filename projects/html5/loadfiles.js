var relationshipTemp = '';

function printtemp(name_){
	
	// var e = document.getElementById("browser");
	// var strUser = e.options[e.selectedIndex].value;
	// // relationshipTemp = $("#browser option:selected").text();
	file='data'+name_+'.json';
	console.log(name_);
	console.log(file)
	$("#tree-container").load();
	document.getElementById("top_name").innerHTML= name_ ;
}

