# 📚 AI Lesson Planner

An AI-powered web application built with Streamlit that helps educators generate detailed, interactive lesson plans using Groq's LLM API. Create comprehensive lesson plans with YouTube links, study notes, quizzes, and multiple export formats.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.39.0%2B-red)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 🤖 **AI-Powered Generation** - Generate comprehensive lesson plans with AI assistance
- 📚 **Notes & Quiz Generator** - Automatically create study notes and quizzes
- 📥 **Multiple Export Formats** - Export as PDF, Word, or Markdown
- 🎓 **All Education Levels** - From Kindergarten to PhD
- 🔍 **Smart Search & Filter** - Easily find and organize your plans
- 💾 **Cloud Storage** - All plans safely stored in MongoDB
- 🎨 **Dark/Light Mode** - Beautiful UI with theme switching
- 📱 **Mobile-Friendly** - Responsive design for all devices
- 🔐 **User Authentication** - Secure login and signup system

## 🏗️ Project Structure

```
ai-lesson-planner/
├── src/
│   ├── app/              # Application modules (future)
│   ├── config/           # Configuration settings
│   │   ├── __init__.py
│   │   └── settings.py   # App settings and social links
│   └── utils/            # Utility functions
│       ├── __init__.py
│       ├── export.py     # PDF/Word export functions
│       └── llm.py        # LLM integration
├── docs/                 # Documentation
│   ├── CONTRIBUTING.md
│   ├── ENHANCEMENTS.md
│   ├── MONGODB_TROUBLESHOOTING.md
│   └── QUICKSTART.md
├── tests/                # Test files
├── scripts/              # Helper scripts
│   └── run.py           # Run script
├── .streamlit/          # Streamlit configuration
│   └── config.toml
├── streamlit.py         # Main application entry point
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup
├── pyproject.toml      # Modern Python project config
├── LICENSE             # MIT License
└── README.md          # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- MongoDB (Local or Atlas)
- Groq API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-lesson-planner.git
   cd ai-lesson-planner
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   - Copy `.env.example` to `.env` (or create `.env` file)
   - Add your Groq API key: `key=your_groq_api_key_here`
   - Add MongoDB URI (optional): `MONGODB_URI=your_mongodb_connection_string`

5. **Update social links (optional):**
   - Edit `src/config/settings.py`
   - Update LinkedIn, GitHub, Email, and Portfolio URLs

6. **Run the application:**
   ```bash
   streamlit run streamlit.py
   ```

## 📖 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Groq API Key (Required)
key=your_groq_api_key_here

# MongoDB Connection (Optional - defaults to localhost)
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/?appName=StudentDB
```

### Social Links Configuration

Edit `src/config/settings.py` to update your social links:

```python
# Social Links
LINKEDIN_URL = "https://www.linkedin.com/in/amitmishrajnp"
GITHUB_URL = "https://github.com/amitmishraecc"
EMAIL = "mishraamit7348@gmail.com.com"
PORTFOLIO_URL = "https://basic-portfolio-xi.vercel.app/"
```

## 🎯 Usage

1. **Sign Up/Login** - Create an account or login
2. **Create Lesson Plan** - Fill in subject, topic, grade level, and learning objectives
3. **Generate** - AI creates a comprehensive lesson plan with YouTube links
4. **Generate Notes & Quiz** - Create study materials automatically
5. **Export** - Download in PDF, Word, or Markdown format
6. **Save & Organize** - Save plans and access them anytime

## 📚 Documentation

- [Quick Start Guide](docs/QUICKSTART.md)
- [MongoDB Setup](docs/MONGODB_TROUBLESHOOTING.md)
- [Enhancements & Features](docs/ENHANCEMENTS.md)
- [Contributing Guidelines](docs/CONTRIBUTING.md)

## 🛠️ Development

### Running in Development Mode

```bash
streamlit run streamlit.py
```

### Project Structure

The project follows a modular structure:
- `src/config/` - Configuration and settings
- `src/utils/` - Utility functions (export, LLM)
- `streamlit.py` - Main application (can use modular imports)

### Adding New Features

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes
3. Test thoroughly
4. Submit pull request

## 🧪 Testing

```bash
pytest tests/
```

## 📦 Deployment

### Local Deployment
```bash
streamlit run streamlit.py
```

### Cloud Deployment
- **Streamlit Cloud**: Connect your GitHub repo
- **Heroku**: Use Procfile with `streamlit run streamlit.py`
- **Docker**: Build and deploy container

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Amit Mishra**
- LinkedIn: [Amit Mishra](https://www.linkedin.com/in/mishraamitjnp/)
- GitHub: [@amitmishraecc](https://github.com/amitmishraecc)
- Email: mishraamit7348@gmail.com
- Portfolio: [Portfolio Website](https://basic-portfolio-xi.vercel.app/)

## 🙏 Acknowledgments

- Groq for providing the LLM API
- Streamlit for the amazing framework
- MongoDB for database services
- All the educators using this tool

## 📝 Changelog

### Version 2.0.0
- ✨ Added Home page with dashboard
- 🎨 Enhanced UI with modern design
- 🌙 Dark mode toggle in navigation bar
- 📥 PDF and Word export functionality
- 📚 Notes & Quiz generator
- 🔍 Advanced search and filter
- 📊 Statistics dashboard
- 🏗️ Professional project structure

### Version 1.0.0
- Initial release
- Basic lesson plan generation
- User authentication
- MongoDB integration

---

Made with ❤️ for educators worldwide
