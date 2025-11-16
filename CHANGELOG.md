# Changelog

All notable changes to the AI Lesson Planner project will be documented in this file.

## [2.0.0] - 2024

### Added
- 🏠 Home page with dashboard and quick actions
- 🎨 Enhanced UI with modern, professional design
- 🌙 Dark mode toggle button in navigation bar
- 📥 PDF export functionality
- 📘 Word document export
- 📚 Notes & Quiz generator
- 🔍 Advanced search and filter in My Plans
- 📊 Statistics dashboard
- 🏗️ Professional project structure with modular code
- 📞 Social links in footer (LinkedIn, GitHub, Email, Portfolio)
- 🔗 Quick links in footer
- 📖 Comprehensive documentation
- ⚙️ Settings page with preferences
- 🎓 Extended grade levels (Associate, Bachelor's, Master's, PhD)

### Changed
- Restructured repository for production-ready organization
- Moved utilities to `src/utils/` module
- Moved configuration to `src/config/` module
- Enhanced footer with social links and quick navigation
- Improved mobile responsiveness
- Better error handling and user feedback

### Fixed
- MongoDB connection error handling
- Authentication error messages
- UI responsiveness issues
- Export functionality reliability

## [1.0.0] - Initial Release

### Added
- Basic lesson plan generation
- User authentication system
- MongoDB integration
- Dark/Light mode (sidebar radio)
- Markdown export

---

## How to Update Social Links

To update your social links in the footer:

1. Open `src/config/settings.py`
2. Update the following variables:
   ```python
   LINKEDIN_URL = "https://www.linkedin.com/in/your-actual-profile"
   GITHUB_URL = "https://github.com/your-actual-username"
   EMAIL = "your.actual.email@example.com"
   PORTFOLIO_URL = "https://your-actual-portfolio.com"
   ```
3. Restart the application

The footer will automatically display your updated links.

