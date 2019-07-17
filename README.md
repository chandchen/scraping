# Scraping

This project is mainly for data management for daily use and extracting the data from other websites. It's build with django framework.

## Getting Started

Get you a copy of the project up and running on your local machine for development and testing.

### Prerequisites

1. Clone this project

```
$ git clone git@github.com:chandchen/scraping.git
```

2. Go to the directory where you cloned the project

```
$ cd scraping
```

### Installing

Get a development env running, we use `buildout` for isolated environment, and automated build the requirements

```
$ python3.6 bootstrap.py

$ ./bin/buildout
```

## Setup the database

1. Download Postgres and create a new database for your local

```
$ sudo apt-get install postgresql postgresql-contrib
```

2. Create `local_settings.py` in django directory for local development

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebaydb',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. Run the migrations

```
$ ./bin/django migrate

$ ./bin/django makemigrations  # Make data migration tables
```

## Running the server

1. Run the server

```
$ ./bin/django runserver
```

2. Run the automated tests:

```
./bin/django test
```

3. Run the scrapyd server:

```
./bin/scrapyd
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python 3.6](https://docs.python.org/3.6/) - Basic language used
* [Django 2.2](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Scrapy 1.6](https://docs.scrapy.org/en/1.6/) - Collaborative framework for extracting the data

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
