<html>
<head>
<title> sysTAMI </title>
<body>
<p>

<?php
$filenamet = './cgi-bin/rrd/temp/time.txt';
$filedatet = filemtime($filenamet);
if ($filedatet+60 <= time()) {
	$outputex = shell_exec("./cgi-bin/rrd/temp/current_graph.py");
}
$filenameh = './cgi-bin/rrd/humidity/time.txt';
$filedateh = filemtime($filenameh);
if ($filedateh+60 <= time()) {
	$outputex = shell_exec("./cgi-bin/rrd/humidity/current_graph.py");
}
?>

<img src="images/temp/01hr.png">
<br>
<img src="images/humidity/01hr.png">

<br>
<br>

<a href="./detailed-temp.php">
Historic Temperatures</a><br>
<a href="./detailed-humidity.php">
Historic Humidity</a>
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
