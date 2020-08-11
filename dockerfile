FROM python:3.7-alpine                       

LABEL architecture="Yi-Gaoqiao"               

ENV PYTHONUNBUFFERD 1                        

COPY ./requirements.txt /requirements.txt    
RUN pip install -r /requirements.txt     

RUN mkdir /sample-api                     
WORKDIR /sample-api                          
COPY ./sample-api /sample-api                  

RUN adduser -D user                          
USER user  