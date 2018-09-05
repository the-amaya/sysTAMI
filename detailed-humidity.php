<html>
<head>
<title> sysTAMI Historic Humidity Data </title>
<body>
<p>

<?php
$filename = './cgi-bin/rrd/humidity/dy/time.txt';
$filedate = filemtime($filename);
if ($filedate+60 <= time()) {
	$outputex = shell_exec("./cgi-bin/rrd/humidity/current_graph.py");
}
?>

<img src="images/humidity/01hr.png">
<br>
<img src="images/humidity/03hr.png">
<br>
<img src="images/humidity/24hr.png">
<br>
<img src="images/humidity/1week.png">
<br>
<img src="images/humidity/4weeks.png">
<br>
<img src="images/humidity/3months.png">
<br>
<img src="images/humidity/1year.png">
<br>
<br>

<a href="./index.php">
Take me home</a>
<br>
<br>
<a href="https://github.com/the-amaya/sysTAMI">
sysTAMI v0.9.5 - 9/4/18</a>
</body>
<!--
/* Version 0.9.5
 * Date 9/4/18
 * https://github.com/the-amaya/sysTAMI
 -->
</html>