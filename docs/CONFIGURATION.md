# Configuration Guide

This guide explains how to configure the AI Lesson Planner application.

## Environment Variables

### Required Variables

#### Groq API Key
```env
key=your_groq_api_key_here
```
- **Required**: Yes
- **Description**: Your Groq API key for LLM access
- **Get it from**: https://console.groq.com/
- **Location**: `.env` file

### Optional Variables

#### MongoDB Connection String
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/?appName=StudentDB
```
- **Required**: No (defaults to `mongodb://localhost:27017/`)
- **Description**: MongoDB connection string
- **For Atlas**: Use your Atlas connection string
- **For Local**: Leave empty or use `mongodb://localhost:27017/`

## Social Links Configuration

Update your social links in `src/config/settings.py`:

```python
# Social Links
LINKEDIN_URL = "https://www.linkedin.com/in/your-profile"
GITHUB_URL = "https://github.com/your-username"
EMAIL = "your.email@example.com"
PORTFOLIO_URL = "https://your-portfolio-website.com"
```

These links will appear in the footer's "Support & Connect" section.

## Application Settings

Edit `src/config/settings.py` for other settings:

```python
# Database Settings
DATABASE_NAME = "StudentDB"
COLLECTION_USERS = "users"
COLLECTION_PLANS = "lesson_plans"

# API Settings
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_TEMPERATURE = 0.7

# App Settings
APP_NAME = "AI Lesson Planner"
APP_VERSION = "2.0.0"
```

## Streamlit Configuration

Edit `.streamlit/config.toml` for Streamlit-specific settings:

```toml
[theme]
primaryColor = "#6366f1"
backgroundColor = "#f8fafc"
secondaryBackgroundColor = "#ffffff"
textColor = "#1e293b"

[server]
port = 8501
headless = true
```

## Setup Steps

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file:**
   - Add your Groq API key
   - Add MongoDB URI (if using Atlas)

3. **Update social links:**
   - Edit `src/config/settings.py`
   - Update LinkedIn, GitHub, Email, Portfolio URLs

4. **Run the application:**
   ```bash
   streamlit run streamlit.py
   ```

## Verification

After configuration, verify:
- ✅ `.env` file exists with API key
- ✅ MongoDB connection works (check app startup)
- ✅ Social links updated in `src/config/settings.py`
- ✅ Application starts without errors

## Troubleshooting

### API Key Issues
- Check `.env` file exists
- Verify key is correct (no extra spaces)
- Ensure key has quotes if it contains special characters

### MongoDB Issues
- Verify connection string format
- Check IP whitelist (for Atlas)
- Ensure MongoDB service is running (for local)

### Social Links Not Showing
- Check `src/config/settings.py` is updated
- Restart the application
- Clear browser cache

