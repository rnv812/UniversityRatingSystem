# University Rating System

## Introduction

### Objective
The objective of the "University Rating System" is to stimulate the growth of qualifications, professionalism, productivity of pedagogical, scientific and other kinds of activities.

### Task
The main task of the project is creation the inforamtion system that has:
- ability to manage and to store information about different kinds of activities of educators (also about departments and faculties subsequently) within the university;
- tools for analysys of storing information;
- possibility of integration with external services;

## Terms
**Report** - form that the educator fills up with his  current **indicator values**.

**Indicator** - parameter representing the effectiveness of the educator in a particular task.

**Criterion** - indicator that belongs to specific **partition** and has some weight of rating impact.

**Partition** - named group of criterions related to a similar thematics.

## Roles and permissions

Start implementation supposes the following human roles: 
- **Educator**:
  - creates own forms;
  - edits own forms;
  - browses own forms.
- **Forms controller**:
  - has forms possibilities of all educators on department which he is assigned to;
  - examines and approves available forms.
- **Administartor**:
  - asigns roles and perform CRUD operations with any resource.

## Deployment
### Prerequisites
Deployement requires [Docker](https://www.docker.com/) installed.

### Environment variables
Repository provides templates of env variables in the `env` directory. To use it you can just rename `dev.template/` to `dev/` and `prod.template/` to `prod/`.  

### Run using shell script
If you are using Linux system, you can run `deploy.sh` script.

```sh
deploy.sh <dev|prod> [docker compose flags] 
```

### Run using docker-compose
Or use docker-compose util directly specifying the yaml file:
- `docker-compose.dev.yaml` - for development
- `docker-compose.prod.yaml` - for production

```sh
docker-compose -f docker-compose.<dev|prod>.yaml
```

### Auxiliary scripts
- `container-shell.sh <container name> <user>` - attach terminal to container as specific user. 

#### API scripts
- `load-fixture.sh <file id>` - load fixture from google drive and install it to database;
- `localize.sh` - compile and switch to provided localization;
- `source activate.sh` - activate project virtual environment.

## Available endpoints
- `localhost:8000` - API root;
- `localhost:8000/swagger` - API swagger;
- `localhsot:8000/redoc` - API redoc;
- `localhost:8000/admin` - API admin panel;
- `localhsot:3000/` - client;
