# Snake Eyes SAAS Project

Snake Eyes online gambling game, implemented as a SAAS (Software-as-a-Service) app with Flask, Docker, Docker Compose, Stripe, Redis, PostgreSQL, Celery, Gunicorn, nginx and AWS Elastic Beanstalk.

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

### Deploy to AWS Elastic Beanstalk

Initialize Elastic Beanstalk Application:

    $ eb init

NOTE: For the Platform, make sure to choose: Docker running on 64bit Amazon Linux 2. Amazon Linux 2 can build the containers using Docker Compose.

Initialize Elastic Beanstalk Environment:

    $ eb create

Deploy Updates to Elastic Beanstalk:

    $ eb deploy
