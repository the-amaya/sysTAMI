# sysTAMI
the Temperature And Moisture Information system

Collect and record data from multiple locations using raspberry pi's and DHT22 sensors (other sensors can be used, this is just written for the DHT22)
primary focus is storing data in RRD files (for a time frame of 1 year) and generate graphs on demand
There is also an option to store data in a mysql database to avoid data loss associated with RRD files.

Basic usage- put the contents of the deploy folder on a raspberry pi with a temperature, humidity, or both sensor
(this is currently designed to use the DHT22 sensor but can be adapted to other sensor types) everything else goes in a web directory

-all file paths should be relevent, however that may break things
-follow the comments in individual files to configure as necessary

this project uses the adafruit python dht library which can be installed on your pi as follows
```sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python setup.py install
```
You will also need RRD python libraries on your webserver, installation will depend on your OS
