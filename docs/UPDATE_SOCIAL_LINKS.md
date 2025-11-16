# How to Update Social Links

## Quick Guide

To update your social links (LinkedIn, GitHub, Email, Portfolio) in the footer:

### Step 1: Open Settings File
Open `src/config/settings.py` in your editor.

### Step 2: Update the Links
Find the "Social Links" section and update with your actual links:

```python
# Social Links (Update these with your actual links)
LINKEDIN_URL = "https://www.linkedin.com/in/your-actual-profile"
GITHUB_URL = "https://github.com/your-actual-username"
EMAIL = "your.actual.email@example.com"
PORTFOLIO_URL = "https://your-actual-portfolio.com"
```

### Step 3: Save and Restart
1. Save the file
2. Restart your Streamlit application
3. The footer will now show your updated links!

## Example

**Before:**
```python
LINKEDIN_URL = "https://www.linkedin.com/in/your-profile"
```

**After:**
```python
LINKEDIN_URL = "https://www.linkedin.com/in/john-doe-123456"
```

## Location in Footer

The links appear in the "📞 Support & Connect" section of the footer on all pages:
- 💼 LinkedIn
- 🐙 GitHub  
- 📧 Email
- 🌐 Portfolio

## Notes

- Links open in new tabs (target="_blank")
- Email uses `mailto:` protocol
- All links are styled with the accent color
- Changes take effect after restarting the app

