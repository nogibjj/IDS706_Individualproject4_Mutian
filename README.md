# Individual Project 4
## Goal
build a publicly accessible auto-scaling container using Azure App Services and Flask

Functionality within Docker

Hosting functioning container on DockerHub

Successfully deploying your container via Azure Web App to a public endpoint

## Overview

This app utilizes some LLM apis to achieve a function like chatgpt. 

Users can ask what they wanna know to the app chat box and get answer from the LLM.


## Steps

### Local Set up


1. Create a flask app called `main.py`
   
  <img width="954" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/c179baf3-4cac-4441-bfe5-96417e5d935e">
  
Here I defined two functions. The index() function is the home page for the app in which users can ask their questions. And then it will call the process_form() function which get the responses from LLM to generate a html file to the user.



2. Create a dockerfile
   
<img width="728" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/2623e6fc-89c4-4bdc-b7a8-53ae78718098">

To build a docker image: 
```
docker build -t <your app name> .
```

3. (Optional) Create a docker-compose.yml
  
<img width="521" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/fa32b3f1-7f36-4cdb-8e04-4a9645a07750">

it's super eazy to deploy mutiple applications through a compose.yml file, all you need to start the app is `docker-compose up`. It will automatically build && run the image.

### Docker Hub Push

1. Create a new repository.
  <img width="1535" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/c825eaf0-c37d-49b5-a2a2-56a4155582f4">

my repository name is liam9907/flaskapp and I named the app the same as my repository.

2. Set up a sh script to push my image

   <img width="732" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/3d48186c-2b77-4ed3-aea8-dd3d4c708779">
Once I update a new image, then I will type `bash pushdocker.sh` to upload my latest image.

### Azure Setup
1. Create a Web App and Deploy through docker hub image

In the Web App's settings, we can find the section for deployment, often labeled as "Deployment Center". Choose the option to deploy a container from Docker Hub

<img width="1802" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/f700dda1-96b9-4c31-9348-01864587a805">

2. Set up in the deployment center
   
   <img width="1162" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/e2fc221f-12f3-4774-bb21-b3ecbffd4962">


### Result

Running app:
<img width="933" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/f0dfcd72-e55e-446d-9fe2-b44937042e96">

index.html:  

<img width="952" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/aeb5c906-ec52-430d-abea-12145223819a">

<img width="567" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/b59e3b28-94dd-4a4c-83d2-0903898d6a21">

result.html:
Because the api is from the Baidu LLM, the answer is in simplified chinese.
<img width="1915" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/9720d4a6-d8df-4627-b393-bf545f640c9d">


Azure deployment:

we can check the log in the deployment center. Here is the running log.
<img width="1834" alt="image" src="https://github.com/nogibjj/IDS706_Individualproject4_Mutian/assets/108935314/fe14b343-8192-4984-872a-6b8d50fe51a1">


### Demo video
https://youtu.be/B1PzgF2kFe0
