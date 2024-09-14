# Use the official Node.js image.
FROM node:18

# Set the working directory inside the container.
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) first to leverage Docker cache.
COPY package*.json ./

# Install dependencies.
RUN npm install

# Copy the rest of your application code to the container.
COPY . .

# Build the Svelte app.
RUN npm run build

# Expose the port your app runs on.
EXPOSE 4173

# Command to run the app.
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0"]
