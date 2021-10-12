FROM node:16.10.0-slim

WORKDIR /app
COPY dist /app

EXPOSE 5000

CMD yarn && yarn global add serve && serve -s "/app"