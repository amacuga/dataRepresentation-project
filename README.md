# dataRepresentation-project

This repository contains my solutions to the Project for the module Data Representation and Querying at GMIT.

I decided to create a Web application project, which includes:

1. A basic Flask server that has a
2. REST API, (to perform CRUD operations)
3. One database table and
4. Accompanying web interface, using AJAX
calls, to perform these CRUD operations

I also tried to make my webpage looks nice. Before you run the code, please create dbconfig.py file in the downloaded repository that will contain your machine's configuration in the following format:

mysql = {

    "host": "localhost",

    "user": "your mysql username (usually it's root)",

    "password": "your mysql password (usually is root or is not set)",

    "database": "datarepresentation"
    
}