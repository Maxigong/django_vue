# Learn Django Vue

Clone this repo and practices how to work with Django and Vue.
The project is configured in a way that django can also serve vue templates in port 127.0.0.1:8000

The idea is comming from this repo

https://github.com/pymike00/QuestionTime

Which originally took the idea from this another repo

https://github.com/EugeneDae/django-vue-cli-webpack-demo

# Intructions

## 1. Clone de repo

## 2. Navegate inside the folder

Create virtual environment

```
python3 -m venv env  
```

## 3. Django

### Navegate inside the backend folder

Install requirements.txt

```
pip install -r requirements.txt
```

Migrate 
```
python manage.py migrate
```

Runserver

```
python manage.py runserver
```
## 4. Vue

### Navegate inside the frontend folder

Install dependecies

```
npm install
```
Run development server

```
npm run serve
```

Now you can see your project in localhost:8080 and 127.0.0.1:8000

## Django Admin as usual

127.0.0.1:8000/admin/

