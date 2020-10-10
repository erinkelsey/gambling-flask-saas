# Snake Eyes SaaS Project

Snake Eyes online gambling game, implemented as a SaaS (Software-as-a-Service) app with Flask, Docker, Docker Compose, Stripe, Redis, PostgreSQL, Celery, Gunicorn, nginx and AWS Elastic Beanstalk.

Hosted example:

### Setup

### Build and Run

    $ docker-compose up --build

### Stop

    $ docker-compose stop

### Check Currently Running Images

    $ docker-compose ps

### Remove Docker Containers

    $ docker-compose rm -f

To remove all stopped containers:

    $ docker rm $(docker ps -a -q)

Remove all dangling images:

    $ docker rmi -f $(docker images -qf dangling=true)

### Remove Images

    $ docker image prune -a

### Testing

NOTE: Make sure that you are running the app with Docker Compose

To run all unit tests:

    $ docker-compose exec website py.test snakeeyes/tests

Create coverage report:

    $ docker-compose exec website py.test --cov-report term-missing --cov snakeeyes

Check code quality with flake8:

    $ docker-compose exec website flake8 . --exclude __init__.py

### Deploy to AWS Elastic Beanstalk

Initialize Elastic Beanstalk Application:

    $ eb init

NOTE: For the Platform, make sure to choose: Docker running on 64bit Amazon Linux 2. Amazon Linux 2 can build the containers using Docker Compose.

Initialize Elastic Beanstalk Environment:

    $ eb create

Deploy Updates to Elastic Beanstalk:

    $ eb deploy
