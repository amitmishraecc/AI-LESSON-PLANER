# Quick Start Guide

## Prerequisites Checklist

- [ ] Python 3.8+ installed
- [ ] MongoDB installed and running
- [ ] Groq API key (get from https://console.groq.com/)

## Step-by-Step Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create .env File

Create a file named `.env` in the project root:

```
# Groq API Key (Required)
key=your_groq_api_key_here

# MongoDB Atlas Connection (Optional - use this for cloud MongoDB)
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

**Or use the setup script:**
- Windows: Run `setup_env.bat`
- Linux/Mac: Run `chmod +x setup_env.sh && ./setup_env.sh`

### 3. Setup MongoDB

**Option A: MongoDB Atlas (Recommended - Cloud)**

1. Sign up at https://www.mongodb.com/cloud/atlas (free tier available)
2. Create a free cluster (M0)
3. Create a database user: **Database Access** → **Add New Database User**
4. Whitelist your IP: **Network Access** → **Add IP Address** → **Add Current IP Address** (or use `0.0.0.0/0` for all IPs - less secure)
5. Get connection string: Click **"Connect"** → **"Connect your application"** → Copy the connection string
6. Replace `<password>` with your database user password
7. Add to `.env` file: `MONGODB_URI=your_connection_string_here`

**Option B: Local MongoDB**

**Windows:**
- Open Services and start MongoDB, or
- Run `mongod` in a terminal

**macOS (Homebrew):**
```bash
brew services start mongodb-community
```

**Linux:**
```bash
sudo systemctl start mongod
```

*Note: If using local MongoDB, you don't need to set `MONGODB_URI` in `.env` (it defaults to localhost)*

### 4. Run the Application

```bash
streamlit run streamlit.py
```

The app will open automatically in your browser at `http://localhost:8501`

## First Use

1. Click "Signup" in the sidebar
2. Create an account with username and password
3. Login with your credentials
4. Fill in lesson details and generate your first lesson plan!

## Troubleshooting

**MongoDB Connection Error:**
- **For Local MongoDB:** Verify MongoDB is running: `mongosh` or `mongo` should connect
- **For MongoDB Atlas:** 
  - Check your connection string in `.env` file (MONGODB_URI)
  - Verify your IP is whitelisted in Atlas Network Access
  - Make sure username and password are correct
  - Check that you replaced `<password>` in the connection string

**API Key Error:**
- Verify `.env` file exists and contains `key=your_api_key`
- Check API key is valid at https://console.groq.com/

**Import Errors:**
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`
- Make sure virtual environment is activated

