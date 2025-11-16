# Contributing to AI Lesson Planner

Thank you for your interest in contributing to AI Lesson Planner! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/ai-lesson-planner.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Create a `.env` file with your API keys

## Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use type hints where possible
- Write docstrings for all functions and classes
- Keep functions focused and modular

### Testing
- Write tests for new features
- Ensure all tests pass before submitting PR
- Run: `pytest tests/`

### Commit Messages
- Use clear, descriptive commit messages
- Follow conventional commit format when possible

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test thoroughly
4. Update documentation if needed
5. Submit a pull request with a clear description

## Project Structure

```
ai-lesson-planner/
├── src/
│   ├── app/          # Main application code
│   ├── config/       # Configuration settings
│   └── utils/        # Utility functions
├── docs/             # Documentation
├── tests/            # Test files
├── scripts/          # Helper scripts
└── streamlit.py      # Main entry point
```

## Questions?

Feel free to open an issue or contact the maintainers.

