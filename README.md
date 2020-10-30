# Weather map
![Github Actions CI](https://github.com/equinor/gathering-persephone/workflows/Python%20application/badge.svg)

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

## What we have achieved:
- [x] Authentication
- [x] Unit tests
- [x] Equinor API strategy
- [x] code review
- [x] Alot of pair programming
- [x] Social activities
- [ ] EDS components

Project Detail:

| > | v| 
|---|---|
Project | Weather Forecast


Team Detail:
| > | v| 
|---|---|
1 | Arnt Erik Stene
2 | Aisha AKram
3 | Haoyuan Zhang
4 | Li Deng
5 | Kristian Reed
6 | Lars Petter Øren Hauge
7 | Shikha Mishra
