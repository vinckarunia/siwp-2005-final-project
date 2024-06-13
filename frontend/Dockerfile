# Dockerfile
FROM node:18.12.1-alpine AS build
# RUN mkdir -p /usr/src/nuxt-app
WORKDIR /app
# update and install dependency
RUN apk update && apk upgrade
# copy the app, note .dockerignore
COPY . /app
RUN npm install
RUN npm run build

FROM node:18.12.1-alpine AS run
WORKDIR /app

RUN npm install nuxt

COPY --from=build /app/.output ./.output/
COPY --from=build /app/package.json ./

EXPOSE 3000

CMD exec npm run serve
