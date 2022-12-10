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

### POST `/api-dump` 
```json
{
  "user_data":
    {
      "age": 20,
      "flying_exp_mins": 30,
      "gender": "m",
      "license": "A1 & A3" 
    },
  "map": "Intruder",
  "summary": 
    {
      "time_overflying_people_ms": 34,
      "number_overflown_people": 399,
      "min_dist_to_nearest_structure": 60.4,
      "min_dist_to_nearest_person": 50.3,
      "avg_dist_to_intruder": 39.4,
      "max_dist_to_start": 150.67,
      "gated_vul_points": 4
    },
  "vectors": [
    {
      "time_ms": 0,
      "px": 0,
      "py": 0,
      "pz": 0
      "vx": 0,
      "vy": 0,
      "vz": 0
    },
    {
      "time_ms": 5,
      "px": 0,
      "py": 0,
      "pz": 0
      "vx": 0,
      "vy": 0,
      "vz": 0
    },
    {
      "time_ms": 10,
      "px": 0,
      "py": 0,
      "pz": 0
      "vx": 0,
      "vy": 0,
      "vz": 0
    }
  ]
}
```

#### Response:
None
