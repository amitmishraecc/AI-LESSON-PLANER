# Contributing to AI Lesson Planner

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/ai-lesson-planner.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.env` file with your API keys (see `.env.example`)

## Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use type hints where possible
- Write docstrings for all functions and classes
- Keep functions focused and modular
- Maximum line length: 120 characters

### Commit Messages
- Use clear, descriptive commit messages
- Format: `[TYPE] Brief description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `[feat] Add dark mode toggle to navigation bar`
- `[fix] Resolve indentation error in login section`
- `[docs] Update README with deployment instructions`

### Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test thoroughly
4. Update documentation if needed
5. Commit your changes: `git commit -m "[feat] Description"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Submit a Pull Request with:
   - Clear description of changes
   - Screenshots (if UI changes)
   - Reference to related issues

## Project Structure

```
ai-lesson-planner/
├── src/
│   ├── app/          # Application modules
│   ├── config/       # Configuration settings
│   └── utils/        # Utility functions
├── docs/             # Documentation
├── tests/            # Test files
├── scripts/          # Helper scripts
└── streamlit.py      # Main entry point
```

## Testing

Before submitting:
- Test all new features
- Ensure no syntax errors
- Check for linting issues
- Verify on different screen sizes (mobile responsiveness)

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Update relevant docs in `docs/` folder
- Keep CHANGELOG.md updated

## Questions?

- Open an issue for questions
- Check existing issues first
- Be respectful and constructive

Thank you for contributing! 🎉

