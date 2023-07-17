[![Python](https://img.shields.io/badge/-Python_3.9.10-464646??style=flat-square&logo=Python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django](https://img.shields.io/badge/-Django_rest_framework_3.12.4-464646??style=flat-square&logo=Django)](https://www.django-rest-framework.org)
[![Django](https://img.shields.io/badge/-Nginx-464646??style=flat-square&logo=Nginx)](https://nginx.org/ru/)
[![Django](https://img.shields.io/badge/-gunicorn-464646??style=flat-square&logo=gunicorn)](https://gunicorn.org/)
<br>

# infra_sprint1 (Kittygram)

Kittygram — социальная сеть для обмена фотографиями любимых питомцев. 

**_Деплой учебного проекта._**

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/devlili/infra_sprint1.git
```

```
cd infra_sprint1
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
