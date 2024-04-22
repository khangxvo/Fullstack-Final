###  ONE TIME SET UP ###
1) Clone this repo to your desired directory
2) Change directory to that cloned directory
3) Create a environment by this command: virtualenv [env] #change env to your desired environment name
4) Acticate your environment by: source [env]/bin/activate
5) Change directory to django_project
6) Intalled packages by command: pip install -r requirements.txt

### Initiate Server ###
1) Change your directory to Fullstack-Final
2) Activate the environment: source [env]/bin/activate
3) Change directory to django_project
4) Run server by: python manage.py runserver
5) Click on the link and you should see the website

### KeyError at /FindAudioBooks/ ###
This happened due to API token expired, let me know if this happened to you 
Need to find a way to auto refresh api token 
