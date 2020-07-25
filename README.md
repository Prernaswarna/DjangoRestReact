# Bug Fix 

App to report issues.

## Description

Bug Fix is an application that lets you report issues with projects , assign them and add comments.

## Setup Instructions

* Clone the repository
* Use the following command to install all required dependencies
```bash
pip install -r requirements.txt
```
* Install Docker and run the following command
```bash
docker run -p 6379:6379 -d redis:5
```
* Create a Mysql database
* Run the following command
```bash 
cd assign
cp local_settings_template.py local_settings.py
```
Fill in proper values in the fields provided
* Run the following commands 
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```

Backend setup is complete !!
