<?php

$readTime = $_POST['time'];
$name = $_POST['name'];
$key = $_POST['key'];
$temp = '';
$humidity = '';

$mysql = "0" //change this to a 1 if you want to also push data to a mySQL server

if ($key == ""){ //if this is public facing you should probably generate a key and put here. this acts as an API key. You will need to put the same key in sensor-push.py
	if (isset($_POST['temp'])){
		$temp = $_POST['temp'];
		$cmd = "cgi-bin/temp.py $readTime $temp $name";
		exec($cmd . " > /dev/null &");
	}
	if (isset($_POST['humidity'])){
		$humidity = $_POST['humidity'];
		$cmd = "cgi-bin/humidity.py $readTime $humidity $name";
		exec($cmd . " > /dev/null &");
	}
	if ($mysql == "1"){
		$cmd = "cgi-bin/mysql.py $name $readTime $temp $humidity";
		exec($cmd . " > /dev/null &");
	}
} else {
	header("Location: index.php");
}
?>
<!--
/* Version 0.9.5
 * Date 9/4/18
 * https://github.com/the-amaya/sysTAMI
 -->
</html>