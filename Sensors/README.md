# Data Generation  

- City creation  
- Sensor Virtualization  

## City creation  

In order to watch this project working we needed to intruduce citys to the DataBase.  
A set of streets belonging to a city was generated with Python script and fed to the API. After the insertion of the data, a set of Sections was returned that will be used later on.  

## Sensor Virtualization  

The objective with this part of data generation is to sucessefully substitute real sensors by a script that generates data in a aproxymate way.  
We could opt to create a set of static messages to recreate the same scenario every time but we decided to go for a more bold move and let the messages be created randomly by a somewhat consistent virtual sensor.  

The previously returned sections are divisions of the sent streets and are needed for the next step (virtualization of sensor data). It was needed to run a few more python scripts on this sections to put it in the desired way, for example find all the connections between Sections so that in the simulation, cars would go from one section to another without magicaly appearing in the order side of the map. Note as well that this responsability should not be from the server, as this consistency in sensor virtualization would not be a concern in a real word project.  
