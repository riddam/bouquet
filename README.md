# Bouquet Management

This console application takes designs and available flowers as input
The output will be a bouquet every time one can be created from the available
flowers:

## Installation
**Prerequisite: Docker is installed**

Build docker image using docker build command
```shell
$ docker build -t image_name .
```

## Tests
Command to run application test cases:
```shell
$ docker run -e RUNTEST=yes flowers
```


## Usage

Run the command line application in Docker using following command:
```shell
$ docker run -ti image_name
```

## Assumptions:
- Design format includes flower size only once and it defines the size for all flowers in the given design (i.e. a large design can only
have large flowers).
- The flower species are listed in alphabetic order and only appear once.
- The flower max quantities are always larger than 0. The flower min quantities are implicit and always equal to 1 (for all
specified species).
- The total quantity of flowers can be smaller than the sum of the flower max quantities - allowing for some variation between
required flower species.
- Bouquet format includes flower size only once and it defines the size of all flowers in the given bouquet (i.e. a large bouquet can
only have large flowers).
- The flower species are listed in alphabetic order and only appear once.
- The flower quantities are always larger than 0.

## Example:
Command line application running in Docker
```shell
$ docker run -ti  flowers
---------Welcome to Bouquet Shop----------
Please provide bouquet designs(or blank to exit): 
AS2a2b3
BL2a2

Provide flower availability(or blank to exit): 
aL
bS
aS
bS
Available Bouquet: AS1a2b
aS
aL
Available Bouquet: BL2a
aS
bS
Available Bouquet: AS2a1b
```

