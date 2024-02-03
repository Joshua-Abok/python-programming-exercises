"""
Question 1: 
----------

Imagine you are working on a DevOps automation script to manage server configurations. 
Design a Python class named ServerConfig that includes the following features:

Attributes:

hostname: A string representing the server's hostname.
ip_address: A string representing the server's IP address.
is_running: A boolean indicating whether the server is currently running.

Methods:

start_server(): A method that starts the server and updates the is_running attribute.
stop_server(): A method that stops the server and updates the is_running attribute.
get_server_info(): A method that returns a string with information about the server, including hostname, 
                   IP address, and its running status.

Implement the ServerConfig class and demonstrate its usage by creating an instance of the class, 
starting and stopping the server, and retrieving server information."""

# Write your code here  


















"""

Question 2: 
----------

Now design a Python class hierarchy that includes two subclasses WebServer and DatabaseServer. 
Have ServerConfig as the base class. 


Subclass WebServer (Inherits from ServerConfig):

Additional Attributes:

web_framework: A string representing the web framework installed on the server.
Additional Method:

update_web_framework(new_framework): A method that updates the web framework on the server if it's running.


Subclass DatabaseServer (Inherits from ServerConfig):

Additional Attributes:

database_engine: A string representing the database engine installed on the server.
Additional Method:

update_database_engine(new_engine): A method that updates the database engine on the server if it's running.


Implement the WebServer and DatabaseServer subclasses based on the provided requirements.
Demonstrate the usage of these classes with relevant actions, including starting and stopping servers, 
and updating specific configurations."""

# Write your code here 

















