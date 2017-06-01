FROM python:3.5
ENV PYTHONUNBUFFERED 1
# install geo libraries and libjpeg for PIL support 
RUN apt-get update && apt-get install -y \ 
libgdal-dev \ 
libgeos-dev \ 
libjpeg62 \ 
libproj-dev \
apache2 \
netcat \
apache2-dev

RUN mkdir /geodjango
WORKDIR /geodjango    
ADD requirements.txt /geodjango
RUN pip install -r requirements.txt


