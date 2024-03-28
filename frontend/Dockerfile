FROM node:18.14.2-alpine AS build

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM node:18.14.2-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --production
COPY --from=build /app/build ./build
ENV NODE_ENV=production
ENTRYPOINT [ "node", "./build" ]