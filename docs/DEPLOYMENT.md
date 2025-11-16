# Deployment Guide

This guide covers deploying the AI Lesson Planner application to various platforms.

## Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (or local MongoDB)
- Groq API key
- Git installed

## Deployment Options

### 1. Streamlit Cloud (Recommended - Free)

Streamlit Cloud offers free hosting for Streamlit applications.

#### Steps:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `streamlit.py`
   - Add secrets:
     - `key`: Your Groq API key
     - `MONGODB_URI`: Your MongoDB connection string
   - Click "Deploy"

3. **Access Your App**
   - Your app will be available at: `https://your-app-name.streamlit.app`

### 2. Heroku

1. **Install Heroku CLI**
   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Procfile**
   ```
   web: streamlit run streamlit.py --server.port=$PORT --server.address=0.0.0.0
   ```

3. **Deploy**
   ```bash
   heroku create your-app-name
   heroku config:set key=your_groq_api_key
   heroku config:set MONGODB_URI=your_mongodb_uri
   git push heroku main
   ```

### 3. Docker

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.10-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and Run**
   ```bash
   docker build -t ai-lesson-planner .
   docker run -p 8501:8501 -e key=your_api_key -e MONGODB_URI=your_uri ai-lesson-planner
   ```

### 4. Local Deployment

1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/ai-lesson-planner.git
   cd ai-lesson-planner
   ```

2. **Setup Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Add your API keys

4. **Run Application**
   ```bash
   streamlit run streamlit.py
   ```

## Environment Variables

Required environment variables:
- `key`: Groq API key
- `MONGODB_URI`: MongoDB connection string (optional, defaults to localhost)

## Security Best Practices

1. **Never commit `.env` file** - It's in `.gitignore`
2. **Use environment variables** for secrets in production
3. **Enable MongoDB IP whitelist** in MongoDB Atlas
4. **Use strong passwords** for database users
5. **Regularly update dependencies**

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change port: `streamlit run streamlit.py --server.port=8502`

2. **MongoDB connection failed**
   - Check IP whitelist in MongoDB Atlas
   - Verify connection string format

3. **API key not found**
   - Ensure environment variables are set correctly
   - Check `.env` file exists and is properly formatted

## Monitoring

- Monitor application logs
- Set up error tracking (e.g., Sentry)
- Monitor API usage and costs
- Track user activity

## Updates

To update the application:
1. Pull latest changes: `git pull origin main`
2. Update dependencies: `pip install -r requirements.txt --upgrade`
3. Restart the application

