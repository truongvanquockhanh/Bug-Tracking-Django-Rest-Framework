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
python manage.py migrate
python manage.py runserver
```
