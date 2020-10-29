# SI Gathering Challenge: Template

## Running the project locally
The easiest way to run the project is using docker-compose. Ensure docker and docker-compose has already been installed.
```
docker-compose up --build
```
Note: You may skip `--build` if you have already built the images.

If you don't want to use docker-compose:

API:
```
docker build -t <name> .
docker run -p 8000:8000 <name>
```

Frontend:
```
cd frontend
docker build -t <name> .
docker run -p 3000:3000 <name>
```
