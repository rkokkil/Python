### Instructions
Build an image from Dockerfile

```
docker build -t companies_crud .
``` 

Check if an image is created 

```
docker images
```

Start a container

```
docker run -d -p 5000:5000 companies_crud
```

Right 5000 is application's port inside a docker container. Left 5000 is application's port inside host machine (on which docker container started) and is mapped with docker's port. 
Whatever traffic (web calls) reaches port 5000 inside host are redirected to 5000 inside docker.

Invoke URL if application is running

```
http://localhost:5000/companies
```

==As Flask doesn't work in Production mode, I made code to work in debug mode.==
```
api.run(host="0.0.0.0", port=int("5000"), debug=True)
```


