# siwp2005-final-project
### This project was created as a completion of the Object Oriented Programming final exam

## About This Project
### This repository consist backend micro-service design of UKRIDA's Portal System.
This project is designed using containerized development. The backend is implemented using Flask and utilizing a MongoDB database. The primary goal is to create a RESTful API that serves as an endpoint for a user interface (UI).

## The Developers
### Anggota Kelompok :
- Steven Wijaya (422023002)
- Vincent Karunia (422023012)
- Nayla Larasati Lizhar (422023013)
- Victorio Putra Saritan (422023022)

## What's In This Project
### This project consists of 13 endpoints:
- User
Endpoint for managing user. Consists of register user and login endpoint.

- Courses
Endpoint for managing courses. Consist of add course, get all courses, get course by ID, delete course by ID, and edit course.

- Bulletins
Endpoint for managing bulletins. Consist of add bulletin, get all bulletins, get bulletin by ID, delete bulletin by ID, and edit bulletin.

- Classes
Endpoint for managing classes. Consist of add classes, get all classes, get classes by ID, delete classes by ID, and edit class.

- Guidance
Endpoint for managing academic guidances. Consist of add guidance, get all guidance, get guidance by ID, delete guidance by ID, and edit guidance.

- Profile
Endpoint for managing profiles. Consist of add profile, get all profiles, get profile by ID, delete profile by ID, and edit profile.

- Billings
Endpoint for managing billings. Consist of add billings, get all billings, get billing by ID, delete billing by ID, and edit billing.

- Dashboard
Endpoint for managing dashboard. Consist of add dashboard data, get all dashboard data, get dashboard data by ID, delete dashboard data by ID, and edit dashboard data.

- News
Endpoint for managing news. Consist of add news, get all news, get news by ID, delete news by ID, and edit news.

- Exam
Endpoint for managing exams. Consist of add exam, get all exam, get exam by ID, delete exam by ID, and edit exam.

- CampusEvent
Endpoint for managing campus events. Consist of add campus event, get all campus event, get campus event by ID, delete campus event by ID, and edit campus event.

- InputKRS
Endpoint for managing input KRS. Consist of add KRS, get all KRS, get KRS by ID, delete KRS by ID, and edit KRS.

- Softskill
Endpoint for managing softskill (certificates). Consist of add softskill, get all softskills, get softskill by ID, delete softskill by ID, and edit softskill.


# How To Run

## Insallation

### Install Docker and Docker Compose

### Ubuntu

### Windows
> if you are using windows, you can run the ubuntu image using your windows `WSL` subsystem

## WSL 2 with Ubuntu Installation
### Enable wsl
- Open PowerShell as Administrator
- Enable WSL feature
    ```
      dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

    ```
- Enable Virtual Machine
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

    ```
    ![image](https://hackmd.io/_uploads/Hkps9rsV0.png)
- Restart your computer. 
> you need to restart your windows to see the effect whether you can run wsl on your windows
    
- Validate your wsl
    ```
    wsl --version
    ```
- ![image](https://hackmd.io/_uploads/HkL7oHiVC.png)
- set WSL 2 as default version
    ```
    wsl --set-default-version 2
    ```
![image](https://hackmd.io/_uploads/SyeviHsVR.png)


### Using Ubuntu on WSL 2

- check which linux distro are availables on your windows 
```
wsl --list --online
```
![image](https://hackmd.io/_uploads/SkS3aHs40.png)

- install ubuntu
```
wsl.exe --install -d <DistroName>
```
please change `<DistroName>` with the ubuntu distro list on your windows, we will use `Ubuntu-22.04`
`wsl.exe --install -d Ubuntu-22.04` then follow the instruction set ubuntu username and password

![image](https://hackmd.io/_uploads/ByBsy8iEA.png)

## Quick start

- To start and build the development flask backend:
```
docker compose -f docker-compose.yaml up --build -d
```
Note: `docker compose` command is used in `Compose V2`. Supoosedly your version is `Compose V1` replace `docker compose` with `docker-compose`

After successful run the dev server, you will be able to see all containers are running 
```shell
docker ps
```
check specific container
```shell
docker ps --filter name="name of the container" 
```
- To stop service
```
docker compose -f docker-compose.yaml down
```
*specify `-v` to remove the mongodb volume*

- To remove all container
```
docker system prune
```

## Tech stack
- Flask
- MongoDB
- Docker  

References
* flask_mongoengine -> MongoDB connector ([docs](https://docs.mongoengine.org/# "docs"))
  * flask_jwt_extended -> JWT Token
- MongoDB ([docs](https://github.com/docker-library/docs/tree/master/mongo "docs"))

- Marshmallow -> Schema Validator ([docs](https://marshmallow.readthedocs.io/en/stable/index.html "docs"))
- Docker


## Debugging
Debug via docker logs
```shell
docker logs 'container name'
```
