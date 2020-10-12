# Snake Eyes SaaS Project

Snake Eyes online gambling game, implemented as a SaaS (Software-as-a-Service) app with Flask, Docker, Docker Compose, Stripe, Redis, PostgreSQL, Celery, Gunicorn, and nginx.

## Setup

In order to run with Docker Compose locally, you will need a .env file in the main folder with the following environment variables:

NOTE: Redis and PostgreSQL are containers, however in a real production app, they should be separate, and use something like AWS RDS and AWS ElastiCache.
In order to do this, remove the redis and postgres services from the Docker Compose file, and set the redis and postgres environment variables to those of your external services.

## Build and Run

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

## Testing

NOTE: Make sure that you are running the app with Docker Compose

To run all unit tests:

    $ docker-compose exec website py.test snakeeyes/tests

Create coverage report:

    $ docker-compose exec website py.test --cov-report term-missing --cov snakeeyes

Check code quality with flake8:

    $ docker-compose exec website flake8 . --exclude __init__.py

## Click CLI

The snackeeyes Click CLI is used to make commands easier to run.

Create egg.info file:

    $ pip install --editable .

NOTE: this is include in the repository

### Testing Commands

View all CLI commands:

    $ docker-compose exec website snakeeyes

Test:

    $ docker-compose exec website snakeeyes test

Coverage:

    $ docker-compose exec website snakeeyes cov

flake8:

    $ docker-compose exec website snakeeyes flake8
    $ docker-compose exec website snakeeyes flake8 --no-skip-init

Help:

    $ docker-compose exec website snakeeyes <command> --help

Example:

    $ docker-compose exec website snakeeyes flake8 --help

### Database Commands

See all database commands:

    $ docker-compose exec website snakeeyes db

Initialize database (or re-initialize):

    $ docker-compose exec website snakeeyes db init

Add seed data to database:

    $ docker-compose exec website snakeeyes db seed

Reset database by initializing and seeding:

    $ docker-compose exec website snakeeyes db reset

OR, with option:

    $ docker-compose exec website snakeeyes db reset --with-testdb

### Generating Fake Data

Check all add commands:

    $ docker-compose exec website snakeeyes add

Generate all fake data (100 users, numerous invoices, numerous bets):

    $ docker-compose exec website snakeeyes add all

Generate fake users:

    $ docker-compose exec website snakeeyes add users

Generate fake invoices:

    $ docker-compose exec website snakeeyes add invoices

Generate fake bets:

    $ docker-compose exec website snakeeyes add bets

### Generating Secure Tokens

Generate a secure token with 128 bytes:

    $ docker-compose exec website snakeeyes secret

You can also specify number of bytes you want for the secret:

    $ docker-compose exec website snakeeyes secret [num_bytes]

### Viewing All Route Endpoints

    $ docker-compose exec website snakeeyes routes

### Breaking Down Lines of Code in App

    $ docker-compose exec website snakeeyes loc

### Stripe

Sync Stripe plans from the config/settings.py file:

    $ docker-compose exec website snakeeyes stripe sync_plans

List all of the Stripe plans:

    $ docker-compose exec website snakeeyes stripe list_plans

Delete a Stripe plan:

    $ docker-compose exec website snakeeyes stripe delete_plans [plan_name]

NOTE: You can delete multiple plans at once, just separate the names with spaces.

### Translations with Babel

Extract translations from files into pot file:

     $ docker-compose exec --user "$(id -u):$(id -g)" website snakeeyes babel extract

Update translations:

    $ docker-compose exec --user "$(id -u):$(id -g)" website snakeeyes babel update

Compile new translations:

    $ docker-compose exec --user "$(id -u):$(id -g)" website snakeeyes babel compile

Crete new languages:

    $ docker-compose exec --user "$(id -u):$(id -g)" website snakeeyes babel init --language [language_code]

## Testing with Stripe

Use the following fake cards to test the Stripe setup.

### Visa:

    Name: any name
    Card number: 4242 4242 4242 4242
    Expiry date: any date
    CCV: 123

### MasterCard:

    Name: any name
    Card number: 5555 5555 5555 4444
    Expiry date: any date
    CCV: 123

## ngrok For Stripe Webhooks:

You will need an ngrok account.

Download: https://ngrok.com/download

Connect your account:

    $ ./ngrok authtoken [your_auth_token]

Help:

    $ ./ngrok help

Fire it up:

    $ ./ngrok http localhost:8000

Add the HTTP Forwarding address to the SERVER_NAME setting in config/settings.py file.

### Set up the webhook on Stripe:

Go to Developers -> Webhooks -> Endpoints -> Add endpoint

For endpoint address use: http://[your_ngok_address]/stripe_webhook/event

Event types: invoice.created

## Database Migrations:

Create a migration manually with Alembic:

    $ docker-compose exec --user "$(id -u):$(id -g)" website alembic revision -m "[description]"

Run migration upgrade:

    $ docker-compose exec website alembic upgrade head

Downgrade migration by one:

    $ docker-compose exec website alembic downgrade -1

Get the current revision:

    $ docker-compose exec website alembic current

Get revision history:

    $ docker-compose exec website alembic history --verbose

Auto-generate migration scripts:

    $ docker-compose exec --user "$(id -u):$(id -g)" website alembic revision --autogenerate -m "[description]"

## Deploy to AWS Elastic Beanstalk

Initialize Elastic Beanstalk Application:

    $ eb init

NOTE: For the Platform, make sure to choose: Docker running on 64bit Amazon Linux 2. Amazon Linux 2 can build the containers using Docker Compose.

Initialize Elastic Beanstalk Environment:

    $ eb create

Add the environment variables from the .env file to the environment variables in environment configuration. Make sure these are your production environment variables, not the local ones.

Deploy Updates to Elastic Beanstalk:

    $ eb deploy

Check status:

    $ eb status --verbose

View and/or modify config

    $ eb config

In order to get the Postgres database initialized, you will need to login to the server and run the following command in the /var/app/current folder:

    $ docker-compose exec website snakeeyes db reset

And if you want to add seed data:

    $ docker-compose exec website snakeeyes add all

In order for the app emails to be sent, you will need to use AWS SES, instead of Gmail, since Gmail blocks any mail sent from AWS EC2.
