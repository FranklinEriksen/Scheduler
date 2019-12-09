# Smart Schedule Installation Guide

## First make sure you have Pip installed (Current version is pip3)

```sudo apt-get install python3 python3-pip```

## Next Use Pip3 to install Django

```pip3 install Django```

## Clone this repository to your local system

```git clone https://github.com/FranklinEriksen/Scheduler.git```

## Finally launch Smart Schedule 

To do this navigate to the WebApp Folder in the Scheduler folder and run the following command

```python3 manage.py runserver```


## Extra information

Use these command to update DB <br/>
```python manage.py migrate --run-syncdb ```<br/>
```python manage.py makemigrations```

