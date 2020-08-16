## Notes
### Basic Auth
Simple method of authentication, but has various issues:
* needs secure communication channel (uses reversible Base64 encoding instead of hashing)
* natively doesn't support logout mechanism, one of workarounds is to send "401 Unathorized" response to clear browser cache https://stackoverflow.com/questions/233507/how-to-log-out-user-from-web-site-using-basic-authentication

### API key
https://medium.com/data-rebels/fastapi-authentication-revisited-enabling-api-key-authentication-122dc5975680

### Client-side vs Server-side vs Pre-rendering for Web Apps
https://www.toptal.com/front-end/client-side-vs-server-side-pre-rendering

### Javascript frameworks to learn in 2020
https://towardsdatascience.com/top-10-javascript-frameworks-to-learn-in-2020-a0b83ed3211b
https://hackr.io/blog/best-javascript-frameworks

### Nice Docker, FastAPI, Vue.js tutorial
https://medium.com/@bruno.fosados/simple-learn-docker-fastapi-and-vue-js-first-part-docker-setup-a8e4c09ef9c4
#### How to load database credentials from OS environment variables
in docker-compose.yml
```yaml
environment:
      - MONGO_INITDB_ROOT_USERNAME
      - MONGO_INITDB_ROOT_PASSWORD
```
then in the terminal
```bash
$ export MONGO_INITDB_ROOT_USERNAME="tancho_usuer"
$ export MONGO_INITDB_ROOT_PASSWORD="4dm1n4dm1n"
```
#### How to attach to container's terminal
tancho is the name of the Docker container

```bash
docker-compose exec tancho /bin/bash
```

#### Running standalone MongoDB instance using docker
to run
```bash
sudo docker run --name mongo -d -p 27017:27017 mongo
```
to remove all docker containers
```bash
sudo docker rm -f $(docker ps -a -q)
sudo service docker restart
```
to check which containers are currently running
```bash
sudo docker ps
```