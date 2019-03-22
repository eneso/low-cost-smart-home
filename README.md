# low-cost-smart-home

Low Cost Smart Home Project

With this project, users can activate/deactivate their outlets from anywhere in the world by either using the website we created or via Alexa.
The website was created using Django as it runs well on raspberry pi with Raspbian OS which is compatible Apache server and SQLite. 
When users activate any of the switches on the website, it sends requests to the server which serves as a central database. 
When it gets a request from the client, the database gets updated and broadcast that change of state which reflects on the website as either on or off. 

In terms of hardware, it is using 8-channel power relay, raspberry pi zero, Alexa, electrical outlet box, basic outlets and cables from home depot.

What cool is that everything costs less than 80$!

