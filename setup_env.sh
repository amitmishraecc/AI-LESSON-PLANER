#!/bin/bash

echo "Creating .env file..."
echo ""
echo "Please enter your Groq API key."
echo "You can get it from: https://console.groq.com/"
echo ""
read -p "Enter your Groq API key: " API_KEY
echo "key=$API_KEY" > .env
echo ""
echo ""
echo "MongoDB Setup:"
echo "Option 1: Use MongoDB Atlas (Cloud) - Enter your connection string"
echo "Option 2: Use Local MongoDB - Press Enter to skip"
echo ""
echo "MongoDB Atlas connection string format:"
echo "mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority"
echo ""
read -p "Enter MongoDB URI (or press Enter for localhost): " MONGODB_URI
if [ ! -z "$MONGODB_URI" ]; then
    echo "MONGODB_URI=$MONGODB_URI" >> .env
fi
echo ""
echo ".env file created successfully!"
echo ""

