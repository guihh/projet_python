FROM python:3.5

RUN apt-get update && apt-get install -y \ 
netcat 

RUN mkdir /web_geoalchemy
WORKDIR /web_geoalchemy
ADD requirements.txt /web_geoalchemy/
RUN pip install -r requirements.txt


    
