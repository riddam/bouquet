# Bouquet Management

This console application takes designs and available flowers as input
The output will be a bouquet every time one can be created from the available
flowers:

## Installation
**Assumption: Docker is installed**

build docker image using docker build
```bash
docker build -t image_name .
```

## Tests
Command to run test cases:
```docker
docker run -e RUNTEST=yes flowers
```


## Usage

Run the program in docker using following command
```docker
docker run -ti image_name
```


