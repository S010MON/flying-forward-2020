# Flying Forward 2020 Database and API

## Installation Guide

### Dependencies
Ensure that docker and docker-compose are installed

        docker version
        docker-compose --version
        
if not installed -> install ![docker](https://docs.docker.com/get-docker/) and ![docker-compose](https://docs.docker.com/compose/install/) for your OS

<br/>

### Run Server
Navigate to the `flying-forward-2020-api/` root directory
        
Run the container:
        
        sudo docker-compose up

Done!

## API Specification 

### POST `/user` 

#### Request:
```json
{
  "age": 20,
  "flying_minutes": 30,
  "gender": "m",
  "licences": "A1 & A3"
}
```
#### Response:
```json
{
  "user_id": 1
}
```

### POST `/data` 
```json
{
  "user_id": 1,
  "map": "Intruder",
  "positions": [
    {
      "time": 0,
      "x": 0,
      "y": 0,
      "z": 0
    },
    {
      "time": 1,
      "x": 1,
      "y": 2,
      "z": 3
    }, 
    {
      "time": 2,
      "x": 2,
      "y": 4,
      "z": 6
    }
  ]
}
```

#### Response:
None
