
# Movie Application web
This repository tale a project django implemented with heroku and also with a docker-container. A project that in the future will deal with a webpage that will show all the information of all the films with the trailer and where can buy or watch online. Additionally, users can dial and write reviews about it.

For now we have implemented the login, admin page, home and the structure of the data base.

## Authors
- David Jovellar Fantova
- Edgar Moreno Molina
- Marc Perez Arnaiz
- Aitor Zaragoza Galiana


## Requirements
We need to have python 3.7.2 installed and run the following command:
```bash
pip3 install -r requirements.txt  
```
For the part with docker-container we need to have installed the docker-engine, we can installed following this commands:
```bash
yum install docker-engine  
```
## Usage

- Django project: 

	First we’ll need to create a user who can login to the admin site and next step run the server. Run the following commands:
	
	```bash
	python3 manage.py createsuperuser
	python3 manage.py runserver 
	```
	and then for see if everything work open the [web](http://127.0.0.1:8000/login) and the application show up.
	
	
- Heroku implementation:

	For see the application implemened in Heroku click the [link](https://movieappwebproject.herokuapp.com/login).
	````
	User: admin	
	Password: admin123
	````

- Docker-container implementation:

	First of all we need to start the docker and enable with this commands:
	```
	systemctl start docker
	systemctl enable docker
	```
	next step is build the django project into docker:
	```
	docker build -t django_application_image .
	```
	
	and for running the docker we need to run this command:
	```
	docker run -p 8000:8000 -i -t django_application_image
	```
	
	Finally, go to the [browser](http://0.0.0.0:8000/login) for see the application web. The users for login is the same user you 		create for the django project.
