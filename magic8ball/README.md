# ✨ Magic 8 Ball - Production-Ready Web Game

A beautiful, smooth, and engaging Magic 8 Ball web application built with FastAPI and vanilla JavaScript. Features multiple themes, achievements, history tracking, and delightful animations.

## 🎮 Features

### Core Game
- ✅ Smooth shake animation with anticipation delay
- ✅ Balanced answer distribution (positive, negative, neutral, easter eggs)
- ✅ Multiple response packs (default, funny, serious, motivational)
- ✅ Configurable responses (JSON file, easily upgradable to database)
- ✅ Graceful input validation and error handling

### User Experience
- ✅ 6 Beautiful themes (Classic, Neon, Galaxy, Cute, Dark, Light)
- ✅ Smooth 60 FPS animations (CSS3)
- ✅ Mobile-first responsive design
- ✅ Dark/Light mode support
- ✅ Accessible fonts and high-contrast colors
- ✅ Sound effects toggle with Web Audio API

### Engagement Features
- ✅ Question history with search
- ✅ Favorite answers marking
- ✅ Achievement system (7 achievements)
- ✅ Daily question counter
- ✅ Total questions statistics
- ✅ Share results functionality
- ✅ Local storage persistence

### Technical
- ✅ FastAPI async backend
- ✅ Pydantic validation
- ✅ Comprehensive unit tests (25+ tests)
- ✅ Clean architecture (separation of concerns)
- ✅ Proper error handling
- ✅ CORS support
- ✅ Production-ready logging

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or poetry

### Installation

```bash
# Clone or navigate to project directory
cd magic8ball

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Start the server
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000` in your browser.

## 📁 Project Structure

```
magic8ball/
├── backend/
│   ├── __init__.py
│   ├── config.py              # Settings & configuration
│   ├── magic8ball.py          # Core game logic (Magic8Ball class)
│   ├── models.py              # Pydantic validation models
│   ├── main.py                # FastAPI application
│   └── responses.json         # Responses configuration
├── frontend/
│   ├── index.html             # Single-page app
│   ├── styles.css             # Themes & animations
│   ├── api.js                 # API client
│   ├── game.js                # Game state & logic
│   └── ui.js                  # UI interactions
├── tests/
│   └── test_backend.py        # Comprehensive test suite
├── requirements.txt           # Python dependencies
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

### Core Game
- `GET /` - Serve homepage
- `POST /ask` - Ask the Magic 8 Ball
  ```json
  {
    "question": "Will I succeed?",
    "response_pack": "default"
  }
  ```
- `GET /response-packs` - Get available response packs
- `GET /themes` - Get all themes
- `GET /themes/{theme_id}` - Get specific theme
- `GET /achievements` - Get all achievements

### System
- `GET /health` - Health check
- `GET /info` - App information

## 🎨 Themes

- **Classic** - Timeless Magic 8 Ball look (blue/red)
- **Neon** - Cyberpunk aesthetic (neon green/pink)
- **Galaxy** - Cosmic vibes (purple/pink)
- **Cute** - Pastel aesthetic (yellow/pink)
- **Dark** - Easy on eyes dark mode
- **Light** - Clean light mode

Themes automatically persist to localStorage.

## 🏆 Achievements

1. **First Question** - Ask your first question
2. **Curious Mind** - Ask 10 questions
3. **Oracle Seeker** - Ask 50 questions
4. **Master Questioner** - Ask 100 questions
5. **Devoted Believer** - Ask 250 questions
6. **Wisdom Collector** - Ask 500 questions
7. **Easter Egg Hunter** - Find an Easter egg

## 🧪 Testing

Run the comprehensive test suite:

```bash
pytest tests/ -v
pytest tests/test_backend.py::TestMagic8BallCore -v
pytest tests/test_backend.py::TestBalancedDistribution -v
```

Coverage includes:
- Core game logic (Magic8Ball class)
- Pydantic validation models
- Answer distribution balance
- Response packs
- Edge cases (unicode, special characters, etc.)

## 🔊 Sound Effects

The app includes Web Audio API-generated sound effects:
- **Shake Sound** - Low rumble when ball is shaking
- **Reveal Sound** - Ascending tone when answer appears
- **Click Sound** - Subtle feedback on interactions

Sound can be toggled on/off (preference saved locally).

## 💾 Data Persistence

- **History** - Stored in localStorage (browser)
- **Achievements** - Stored in localStorage
- **Theme preference** - Stored in localStorage
- **Sound setting** - Stored in localStorage
- **Animation speed** - Stored in localStorage

**Note:** Data persists per browser/device. Ready for backend database upgrade.

## 🚀 Deployment

### Docker

```bash
docker build -t magic8ball .
docker run -p 8000:8000 magic8ball
```

### Render / Railway / Heroku

1. Create `.env` file with `DEBUG=false`
2. Push to Git repository
3. Deploy using platform-specific instructions

The app is cloud-ready with:
- Environment variable support
- Proper logging
- Health check endpoint
- Graceful error handling

## 📱 Mobile Optimization

- One-hand friendly layout
- Touch-optimized buttons
- Responsive animations
- Mobile-first CSS design
- Proper viewport meta tags

## ♿ Accessibility

- Semantic HTML
- ARIA labels
- High contrast colors
- Respects `prefers-reduced-motion`
- Keyboard navigation support
- Clear focus states

## 🔮 Future Enhancements

- [ ] User accounts with login
- [ ] Cloud sync for history & achievements
- [ ] Multiplayer mode
- [ ] Custom response packs upload
- [ ] Analytics dashboard
- [ ] Mobile app (Native)
- [ ] PWA support
- [ ] Multi-language support (i18n)
- [ ] Social media integrations
- [ ] Backend database (PostgreSQL)

## 📝 Code Quality

- Clean, readable code
- Comprehensive docstrings
- Type hints throughout
- Separation of concerns
- Production-ready error handling
- Proper logging
- Extensible architecture

## 📄 License

MIT License - Feel free to use for personal or commercial projects.

## 👨‍💻 Author

Built with ✨ magic ✨ as a demonstration of production-ready game development principles.

---

**Questions?** Ask the Magic 8 Ball! 🎱
