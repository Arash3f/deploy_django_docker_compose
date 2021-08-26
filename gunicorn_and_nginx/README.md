# Django + Gunicorn + PostgreSQL + Nginx
### How to deploy 
> **Note** :  Docker and Docker-compose are required to run project

- clone project 

`git clone ... `

- go to project folder

`cd  ... `

`cd  gunicorn_and_nginx `

- Run docker compose

`sudo docker-compose up -d --build `

- create superuser 

`sudo docker exec -it ... sh`

`python manage.py createsuperuser`

- first object 

To see the Nginx performance , go to admin panel and create one object for image_test model and after that go to this page ( 127.0.0.1:8000/image/(id)/ )

The project is running on port 8000 on container and Nging listening on port 80 , we connect it to port 8000 on the Docker host

And we can see the project on 127.0.0.1:8000

> Note: to close docker-compose run this code : `sudo docker-compose down `

> Note : to access project container run this code : `sudo docker exec -it ... sh `
