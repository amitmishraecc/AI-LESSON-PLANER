# Quick Start: Upload to GitHub

## Fast Track (5 Minutes)

### 1. Create GitHub Repository
- Go to [github.com/new](https://github.com/new)
- Name: `ai-lesson-planner`
- Description: "AI-powered lesson planning application"
- Choose Public or Private
- **Don't** initialize with README
- Click "Create repository"

### 2. Upload via Command Line

Open PowerShell/Terminal in your project folder and run:

```bash
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Production-ready AI Lesson Planner"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-lesson-planner.git

# Push
git branch -M main
git push -u origin main
```

### 3. Done! ✅

Your repository is now live at:
`https://github.com/YOUR_USERNAME/ai-lesson-planner`

## What's Included

✅ Production-ready code structure
✅ Comprehensive documentation
✅ GitHub Actions workflow
✅ Issue templates
✅ Proper .gitignore
✅ MIT License
✅ Professional README

## Next Steps

1. **Add Repository Description** on GitHub
2. **Add Topics**: `streamlit`, `ai`, `education`, `python`
3. **Update Social Links** in `src/config/settings.py` (already done!)
4. **Deploy to Streamlit Cloud** (see `docs/DEPLOYMENT.md`)

## Need Help?

See detailed guide: `docs/GITHUB_SETUP.md`

