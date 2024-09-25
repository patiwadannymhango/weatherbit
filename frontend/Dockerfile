# frontend/Dockerfile
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy rest of the application files
COPY . .

# Build the application
RUN npm run build

# Expose the app on port 3000
EXPOSE 3000

# Command to start the React app
CMD ["npm", "start"]
