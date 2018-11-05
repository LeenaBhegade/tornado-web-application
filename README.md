Tornado Web Application 
===============================================================================

## Description

This is a tornado web application. 

## Directory Structure

    tornado-web-app/
        alembic/
            versions/
                8ce64cdc03a4_create_word_table.py
            env.py
            script.py.mako
        handlers/
            admin
            home
        media/
            css/
                style.css
            js/
                vd3.layout.cloud.js
            images/
                favicon.ico
        models/
            word.py
        templates/
        tests/
            test_request_handlers.py
            test_utils.py
        utils/
            crawler.py
            crypto.py
            hashing.py
        alembic.ini
        app.py
        docker-compose.yml
        Dockerfile
        entrtpoint.sh
        README.me
        requirements.txt
        runtime.txt
        settings.py
        urls.py

### alembic
Alembic is the used for managing automated database migrations. In the versions folder we currently have  two functions namely upgrade (create a table) and downgrade (drop a table). Every time we start a docker container we specify almebic command in the entrypoint.sh to create the table in the database.

### handlers

All of your Tornado RequestHandlers go in this directory.

### media

A subfolder each for CSS, Javascript (third party) and images. 

### requirements

pip requirements files contains all the list of libraries required to run the application

### templates

This includes a `base.html` template that correponds to the home page and 
`admin.html` template that corresponds to the admin page.

### utils

#### crawler

This file has a function that accepts url and uses beautiful soup to fetch all words from this url. The return value will be an array of word tuples with the frequency of the word occurance.

#### hashing

This file has a hash function that perform sha256 hash with a salt on a input word. SALT is retrieved from environment variable

#### crypto

This files includes three functions namely get_keys, encrypt_data, decrypt_data. The get_keys function returns the requested key and the encrypt_data and decrypt_data functions will do encryption and decryption respectively

When you get keys for the first time and if keys are not created they will get created inside the running process and will be saved as private.pem and public.pem files. At the moment I have not specified the path as I am not mounting any volume in the container.

 I could have created keys seperately and copied the keys on the predefined path but I wanted the process to create it automatically so that the keys won't be exposed to anything outside the process.

 Every time a new word is about to be saved to the database, the public key is fetched through get_keys and encrypt_function is called to encrypt the word. Similarly when a word is retrieved from database get_keys is called to fetch the private key and then decrypt_data is called to decrypt the data.

### Files

#### .env
This file is not added to git but please make sure you add the required environment variables in it.Make sure you add below variable in that file
SALT=xxxxxxxxx
DATABASE_URL=xxxxxxx
POSTGRES_PASSWORD=xxx
POSTGRES_USER=xxx
POSTGRES_DB=xxx


#### app.py

The main Tornado application, and also a runnable file that starts the Tornado
server

#### settings.py

A place to collect application settings.


### To run the application locally using docker-compose
After git cloning this project make sure you have created a .env file in your root folder and you have added all the necessary environment variables. 
Run below commands on the terminal in root folder of the project:
docker-compose build
docker-compose up

### To run tests locally
Make sure you installed pytest locally or in your virtual environment before firing pytest in the root folder of your application. 
