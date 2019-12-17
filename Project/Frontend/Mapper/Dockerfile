# base image
FROM node:12.2.0-alpine as builder

# set working directory
WORKDIR /app/frontend

# Copy all important files for the installation
COPY package*.json ./
RUN npm ci
RUN npm install konva react-konva @material-ui/core
RUN npm audit fix
COPY . .
RUN npm run build

FROM node:12.2.0-alpine
RUN yarn global add serve
WORKDIR /app/frontend
COPY --from=builder /app/frontend/build .
EXPOSE 80
CMD ["serve", "-p", "80", "-s", "."]
