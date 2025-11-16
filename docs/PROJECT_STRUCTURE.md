# Project Structure

This document describes the professional, production-ready structure of the AI Lesson Planner project.

## Directory Structure

```
ai-lesson-planner/
├── .streamlit/              # Streamlit configuration
│   └── config.toml         # Streamlit app configuration
├── .gitignore              # Git ignore rules
├── docs/                   # Documentation
│   ├── CONTRIBUTING.md    # Contribution guidelines
│   ├── ENHANCEMENTS.md    # Feature enhancements
│   ├── MONGODB_TROUBLESHOOTING.md  # MongoDB help
│   ├── PROJECT_STRUCTURE.md  # This file
│   └── QUICKSTART.md      # Quick start guide
├── scripts/                # Helper scripts
│   └── run.py            # Application runner
├── src/                   # Source code
│   ├── __init__.py       # Package init
│   ├── app/              # Application modules (future expansion)
│   ├── config/           # Configuration
│   │   ├── __init__.py
│   │   └── settings.py   # Settings and social links
│   └── utils/            # Utilities
│       ├── __init__.py
│       ├── export.py     # Export functions (PDF, Word)
│       └── llm.py        # LLM integration
├── tests/                # Test files
├── venv/                 # Virtual environment (gitignored)
├── .env                  # Environment variables (gitignored)
├── .env.example         # Environment template
├── LICENSE              # MIT License
├── pyproject.toml      # Modern Python project config
├── README.md           # Main documentation
├── requirements.txt    # Python dependencies
├── setup.py           # Package setup
├── setup_env.bat      # Windows setup script
├── setup_env.sh       # Linux/Mac setup script
└── streamlit.py       # Main application entry point
```

## Module Descriptions

### `src/config/settings.py`
- Application settings and configuration
- MongoDB connection settings
- API keys and model configuration
- **Social links** (LinkedIn, GitHub, Email, Portfolio)
- Settings validation

### `src/utils/export.py`
- PDF generation using ReportLab
- Word document generation using python-docx
- Markdown formatting utilities

### `src/utils/llm.py`
- LLM setup and configuration
- Prompt generation
- Notes and quiz generation

### `streamlit.py`
- Main application entry point
- UI components and pages
- User authentication
- Session management

## Configuration Files

### `.env`
Environment variables (not in git):
- `key` - Groq API key
- `MONGODB_URI` - MongoDB connection string

### `.streamlit/config.toml`
Streamlit app configuration:
- Theme settings
- Server configuration
- Browser settings

### `pyproject.toml`
Modern Python project configuration:
- Package metadata
- Dependencies
- Build system

## Best Practices

1. **Configuration**: All configurable values in `src/config/settings.py`
2. **Modularity**: Utilities separated into modules
3. **Documentation**: Comprehensive docs in `docs/`
4. **Testing**: Tests in `tests/` directory
5. **Scripts**: Helper scripts in `scripts/`

## Updating Social Links

To update your social links in the footer:

1. Edit `src/config/settings.py`
2. Update the following variables:
   ```python
   LINKEDIN_URL = "https://www.linkedin.com/in/your-profile"
   GITHUB_URL = "https://github.com/your-username"
   EMAIL = "your.email@example.com"
   PORTFOLIO_URL = "https://your-portfolio-website.com"
   ```
3. Restart the application

The footer will automatically use these links.

