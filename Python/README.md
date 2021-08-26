# Django + Sqlite3
### How to deploy 
> **Note** :  Docker and Docker-compose are required to run project

- clone project 

`git clone ... `

- go to project folder

`cd  ... `

`cd  Python `

- Run docker compose

`sudo docker-compose up -d --build `

Now the project is running on port 8000 on container and we connect it to port 8000 on the Docker host

And we can see the project on 127.0.0.1:8000

> Note: for close docker-compose run this code : `sudo docker-compose down `

> Note : for access to project container run this code : `sudo docker exec -it ... sh `
