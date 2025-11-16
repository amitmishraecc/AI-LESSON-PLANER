# MongoDB Atlas Authentication Troubleshooting

## Authentication Error Fix

If you're getting: `bad auth : Authentication failed`

### Step 1: Verify Database User in MongoDB Atlas

1. Go to https://cloud.mongodb.com/
2. Log in to your account
3. Select your cluster
4. Click **"Database Access"** in the left sidebar
5. Check if a user named `StudentDB` exists
6. If it doesn't exist, create it:
   - Click **"Add New Database User"**
   - Choose **"Password"** authentication
   - Username: `StudentDB`
   - Password: `StudentDB123` (or create a new one)
   - Database User Privileges: **"Atlas admin"** or **"Read and write to any database"**
   - Click **"Add User"**

### Step 2: Reset Password (If Needed)

1. In **Database Access**, find your user
2. Click the **"Edit"** button (pencil icon)
3. Click **"Edit Password"**
4. Set a new password (remember it!)
5. Click **"Update User"**

### Step 3: Update Connection String

After resetting or verifying the password, update your `.env` file:

```env
MONGODB_URI=mongodb+srv://StudentDB:YOUR_NEW_PASSWORD@studentdb.avc3vyq.mongodb.net/?appName=StudentDB
```

**Important:** Replace `YOUR_NEW_PASSWORD` with the actual password.

### Step 4: URL Encode Special Characters (If Needed)

If your password contains special characters, encode them:
- `@` → `%40`
- `#` → `%23`
- `$` → `%24`
- `%` → `%25`
- `&` → `%26`
- `+` → `%2B`
- `=` → `%3D`
- `?` → `%3F`

**Example:**
- Password: `MyP@ss#123`
- Encoded: `MyP%40ss%23123`
- Connection string: `mongodb+srv://StudentDB:MyP%40ss%23123@studentdb.avc3vyq.mongodb.net/?appName=StudentDB`

### Step 5: Verify IP Whitelist

1. In MongoDB Atlas, go to **"Network Access"**
2. Make sure your IP address is whitelisted
3. Or temporarily add `0.0.0.0/0` (allows all IPs - less secure, but good for testing)

### Step 6: Test Connection

After updating, restart your Streamlit app:
```bash
streamlit run streamlit.py
```

## Alternative: Get Fresh Connection String

1. In MongoDB Atlas, click **"Connect"** on your cluster
2. Choose **"Connect your application"**
3. Select **"Python"** and version **"3.6 or later"**
4. Copy the connection string
5. Replace `<password>` with your actual password
6. Update your `.env` file with the new connection string

## Still Having Issues?

- Double-check username and password (case-sensitive!)
- Make sure there are no extra spaces in the connection string
- Try creating a new database user with a simple password (no special characters)
- Verify your cluster is running (not paused)

