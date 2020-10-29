FROM node:12.18.3
EXPOSE 3000

WORKDIR /

COPY package*.json ./
COPY . ./
ENV CI=true
ENV NODE_OPTIONS="--max-old-space-size=8192"
RUN npm config set unsafe-perm true
RUN npm install
RUN npm install react-scripts@3.4.3 -g

CMD ["npm", "start"]