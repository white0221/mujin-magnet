FROM python:3.6-alpine3.6

WORKDIR /app

ENV http_proxy http://proxy.noc.kochi-tech.ac.jp:3128
ENV https_proxy http://proxy.noc.kochi-tech.ac.jp:3128

RUN pip install --upgrade pip

RUN apk update && \
    apk upgrade && \
    apk add musl \
            linux-headers \
            gcc \
            g++ \
            make \
            gfortran \
            openblas-dev 

COPY ./requirements.txt /app
      
RUN pip install -r requirements.txt --proxy=$http_proxy && \
    pip3 install RPi.GPIO --proxy=$http_proxy 
    
CMD ["python", "app.py"]
