#Create volume and persist data
#docker volume create virtualenv
#docker volume inspect virtualenv


FROM python:3.7
WORKDIR /app
ADD . /app
RUN pip install virtualenv
CMD ["python", "./main.py"]

#docker build -t docker-data-persistence .
#docker run  --mount source=virtualenv,target=/root/.virtualenv  docker-data-persistence
#docker run -it  --mount source=virtualenv,target=/root/.virtualenv docker-data-persistence  find /root/.virtualenv/my_env/bin
#docker volume rm virtualenv
