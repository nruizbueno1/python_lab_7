FROM python:3.8

WORDDIR /code

# RUN pip install -r requirements.txt

COPY . . #this command puts my local files in the docker file

