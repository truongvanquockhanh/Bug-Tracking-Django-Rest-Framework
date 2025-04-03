## SET UP

**Set up virtualenv with pyenv**

```sh
$ brew install pyenv
```

install python 3.11

```sh
pyenv install 3.11.11
```

creater pyenv virtualenv

```sh
pyenv virtualenv 3.11.11 <name_virtualenv>
```

```sh
pyenv activate <name_virtualenv>
```

install requirement

```sh
pip install requirements.txt
```

## Run app

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Environment Variables

```sh
 POSTGRES_PASSWORD = "plan"
 SECRET_KEY = 'plan'
 POSTGRES_PORT = '5432'
 POSTGRES_HOST = 'localhost'
 OSTGRES_USER = 'postgres'
 POSTGRES_DB = 'postgres'
```

Example .env.example File

Here's an example .env file that you can use to set up your environment variables:

```
To use a different database, modify the DATABASE_URL environment variable.
To use a different settings module, modify the DJANGO_SETTINGS_MODULE environment variable.
To run the app on a different port, use the following command: python manage.py runserver 8080
I hope this helps! Let me know if you have any questions or need further clarification.
```

## Deployment with gunicorn and ngix

1. Install gunicorn, test gunicorn run app:

```sh
gunicorn --bind 0.0.0.0:8000 app.wsgi
```

2. Creating systemd Service Files for Gunicorn (in forder deployment)

- After that run gunicorn:

```sh
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```

If status is active, gunicorn had run in port 8000, if have any err search run gunicorn with services

3. Install nginx, and creater file .nginx

- Start by creating and opening a new server block in Nginx’s sites-available directory:

```sh
sudo vi /etc/nginx/sites-available/nginx
```

file nginx example in forder deployment

- Enable the file by linking it to the sites-enabled directory:

```sh
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```

- Test your Nginx configuration for syntax errors by typing:

```sh
sudo nginx -t
```

- Start nginx:

```sh
sudo systemctl restart nginx
```

Done!
