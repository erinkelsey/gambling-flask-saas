# Snake Eyes SAAS Project

Snake Eyes online gambling game, implemented as a SAAS (Software-as-a-Service) app with Flask, Docker, Docker Compose, Stripe, Redis, PostgreSQL, Celery, and Gunicorn.

Hosted example:

### Setup

### Build and Run

    $ docker-compose up --build

### Check Currently Running Images

    $ docker-compose ps

### Remove Docker Containers

    $ docker-compose rm -f

To remove all containers:

    $ docker-compose rm --all

Remove all dangling images:

    $ docker rmi -f $(docker images -qf dangling=true)

### Deploy
