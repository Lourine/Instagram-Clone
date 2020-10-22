# The Gram
## Author  
  
>[Lourine Millicent](https://github.com/Lourine)  
  
# Description  
This project allows a user to post different photos in his or her account. The user creates an account by registering and signing in. The images posted can be liked and commented on by other users. The User is also able to follow other app users and see their photos on his or her timeline.

## User Story  
  
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Lourine/Instagram-Clone
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Instagram-Clone pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3.8 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python3.8 manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python3.8 manage.py migrate 
```
##### Run the application  
 ```bash 
 python3.8 manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python3.8 manage.py server 
```
##### Testing the application  
 ```bash 
 python3.8 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.1.2](https://docs.djangoproject.com/en/3.1/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [lourine.millicent@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Lourine/Instagram-Clone/blob/master/LICENSE)  
* Copyright (c) 2020 **Lourine Millicent**