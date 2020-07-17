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
docker run -p 6000:5000 companies_crud
```

5000 is application's port inside a docker container. 6000 is application's port inside host machine (on which docker container started) and is mapped with 5000. 
Whatever traffic (web calls) reaches port 6000 are redirected to 5000.

Invoke URL if application is running

```
http://localhost:6000/companies
```



