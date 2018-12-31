FROM node:8
WORKDIR /app
COPY src/package.json /app
RUN npm install
COPY . /app
#CMD node src/index.js
CMD npm start
EXPOSE 8888

#docker run  -it --name my_nodejs_container -d -p 8888:8888 -v src/:/app/   #image_id/image_name
