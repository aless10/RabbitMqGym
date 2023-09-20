## RabbitMq Gym

This is an exercise I wanted to do to learn the basics of [RabbitMq](https://www.rabbitmq.com/).

### Requirements

Everything is in docker containers and it is run using the `docker compose` command.

### How to run the application

Run `docker compose up` in the terminal. You may want to add the `-d` flag if you don't want the verbosity of the logs.

### What's in the application

The docker compose file has 4 services:

- `rabbitmq`: this is the rabbitmq service that is accessible at `localhost:15673` (you can find username and password in the compose file)
- `producer`: this service generates the messages and it sends them to a rabbitmq topic
- `consumer_alpha` and `consumer_beta`: these services are listening on the topic and they receive the messages sent by the `producer` service
