# GitHub Setup Guide

Complete guide to upload and manage your AI Lesson Planner project on GitHub.

## Prerequisites

- Git installed on your system
- GitHub account
- Project ready for upload

## Step 1: Initialize Git Repository

If you haven't initialized git yet:

```bash
cd D:\AI-Lesson-Planner-master\AI-Lesson-Planner-master
git init
```

## Step 2: Create GitHub Repository

1. **Go to GitHub**
   - Visit [github.com](https://github.com)
   - Sign in to your account

2. **Create New Repository**
   - Click the "+" icon in the top right
   - Select "New repository"
   - Repository name: `ai-lesson-planner` (or your preferred name)
   - Description: "AI-powered lesson planning application with Streamlit"
   - Choose **Public** or **Private**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

## Step 3: Add Files to Git

```bash
# Add all files
git add .

# Check what will be committed (optional)
git status

# Commit files
git commit -m "Initial commit: AI Lesson Planner production-ready version"
```

## Step 4: Connect to GitHub

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ai-lesson-planner.git

# Verify remote was added
git remote -v
```

## Step 5: Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main
```

If prompted for credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your GitHub password)
  - Generate token: GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Select scopes: `repo` (full control of private repositories)

## Step 6: Verify Upload

1. Go to your repository on GitHub
2. Check that all files are present
3. Verify `.env` is NOT in the repository (it should be ignored)

## Step 7: Add Repository Description

1. Go to your repository
2. Click the gear icon next to "About"
3. Add description: "AI-powered lesson planning application"
4. Add website: Your portfolio URL
5. Add topics: `streamlit`, `ai`, `education`, `lesson-planning`, `python`, `mongodb`

## Step 8: Update README with Your Info

Edit `README.md` and update:
- Author information
- Repository URLs
- Social links (already in `src/config/settings.py`)

## Step 9: Enable GitHub Pages (Optional)

1. Go to Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` / `root`
4. Save

## Step 10: Add Badges (Optional)

Add to README.md:
```markdown
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/ai-lesson-planner)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/ai-lesson-planner)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/ai-lesson-planner)
```

## Future Updates

To push updates:

```bash
# Check status
git status

# Add changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push origin main
```

## Branching Strategy

For new features:

```bash
# Create feature branch
git checkout -b feature/new-feature-name

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push branch
git push origin feature/new-feature-name

# Create Pull Request on GitHub
```

## Important Notes

1. **Never commit `.env` file** - Contains sensitive API keys
2. **Review changes before committing** - Use `git status` and `git diff`
3. **Write meaningful commit messages**
4. **Keep repository updated** - Regular commits and pushes

## Troubleshooting

### Authentication Issues
- Use Personal Access Token instead of password
- Enable 2FA if required

### Push Rejected
```bash
# Pull latest changes first
git pull origin main --rebase
# Then push again
git push origin main
```

### Large Files
- Ensure `.gitignore` is working
- Check file sizes before committing

## Repository Settings

Recommended settings:
- ✅ Issues enabled
- ✅ Wiki disabled (use docs folder)
- ✅ Projects enabled
- ✅ Discussions enabled (optional)

## Next Steps

1. Add collaborators (Settings → Collaborators)
2. Set up GitHub Actions (already configured)
3. Add repository to your portfolio
4. Share on social media!

