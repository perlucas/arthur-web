FROM node:24-alpine

WORKDIR /home/app

RUN yarn global add vite

COPY frontend/package.json /home/app/package.json
COPY frontend/yarn.lock /home/app/yarn.lock
RUN yarn install --production=false

COPY frontend/ /home/app/

EXPOSE 3000

