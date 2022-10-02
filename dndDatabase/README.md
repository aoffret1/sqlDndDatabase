# Overview

This project is my first attempt to set up a database that directly connects to an executable program. I am have background in using mySQL and Python. However I haven't used SQLite inside Python together, so I got to test that.

This program is similar to rolling a skill check or an attack roll in DnD Beyond and calculating the math that goes with it. For a more in-depth explaination of what that is, please see my demo video.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

The relational database is SQLite based. The structure of this database is essentially two tables. They are not joined, but accessible through Python. The first table is the "Skills" Table that contains an id, skill name, and a modifier. The second table is the "Attacks" table that holds the attack name and various modifier information. 

# Development Environment

The tools that I used for the Enviorment:
* [Python 3.9.13](https://www.python.org/downloads/)
* [SQLite 3](https://www.sqlite.org/download.html)



# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Python](https://www.python.org/downloads/)
* [SQLite](https://www.sqlite.org/download.html)
* [Replit](https://replit.com/~)
* [Youtube](https://www.youtube.com/watch?v=pd-0G0MigUA)

# Future Work
* Join the attack and skill tables.
* GUI Interface.
* Seperate the rolls into its own class.