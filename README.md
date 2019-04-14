# Movie Application web
This repository contains a django project and the files needed to run docker and heroku with it. The project is expected to deal with users that want to find out information about films (including the trailer) and where to buy and/or watch the movie. Additionally, users can rate and write reviews about films.

For now we have implemented the login, admin page, home and the structure of the database so far.

## Authors
- David Jovellar Fantova
- Edgar Moreno Molina
- Marc Perez Arnaiz
- Aitor Zaragoza Galiana


## Requirements
Needs python 3.7.2 installed. To install it, run the following command:
```bash
pip3 install -r requirements.txt  
```
For the docker-container part, it needs the docker-engine. To install it, run following command:
```bash
yum install docker-engine  
```
## Usage

- Django project: 

	First we need to create a user who can login on the admin site (/admin) and then run the server. Run the following commands:
	
	```bash
	python3 manage.py createsuperuser
	python3 manage.py runserver 
	```
	and then to check everything is working open: [django local link](http://127.0.0.1:8000/login) and the application should show up.
	
	
- Heroku implementation:

	In order to see the application implemened in Heroku open: [heroku link](https://movieappwebproject.herokuapp.com/login).
	````
	User: admin	
	Password: admin123
	````

- Docker-container implementation:

	First of all we need to start the docker and enable it with this commands:
	```
	systemctl start docker
	systemctl enable docker
	```
	next step is building the django project into docker:
	```
	docker build -t django_application_image .
	```
	
	and then to run docker:
	```
	docker run -p 8000:8000 -i -t django_application_image
	```
	
	Finally, open [docker local link](http://0.0.0.0:8000/login) in order to see the web application. The user requested for login 		is the same user the one created for the django project.
	
## Deployment proposed

See this [document](https://github.com/DJovellar/MovieApp/blob/master/deployment_proposed_sol.pdf) for the proposal.

