FROM python:3.8-slim

MAINTAINER Ishan K (ik1304@nyu.edu)

RUN apt-get update
RUN apt-get install -y wget 
RUN apt-get install -y build-essential


RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y

EXPOSE 5000

COPY Code /tmp/Code

# Installing the requirements
WORKDIR /tmp/Code
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ] 

CMD [ "front_end.py" ]