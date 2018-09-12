# sysTAMI
the Temperature And Moisture Information system

Collect and record data from multiple locations using raspberry pi's and DHT22 sensors (other sensors can be used, currently this only supports the DHT22, however additional sensor support is planned for the future)
primary focus is storing data in RRD files (for a time frame of 1 year) and generate graphs on demand.
There is also an option to store data in a mysql database to avoid data loss associated with RRD files.

Visit the wiki for setup information and details of planned features https://github.com/the-amaya/sysTAMI/wiki