"""FastAPI main application for Magic 8 Ball"""
from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import logging
from datetime import datetime

from .config import settings
from .models import (
    QuestionRequest, AnswerResponse, ErrorResponse, 
    ThemeInfo, UserSettings, Achievement
)
from .magic8ball import Magic8Ball, AnswerType

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="A fun Magic 8 Ball web game with smooth animations",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (CSS, JS)
frontend_static_path = Path(__file__).parent.parent / "frontend"
if frontend_static_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_static_path)), name="static")

# Initialize Magic 8 Ball engine
magic8ball = Magic8Ball()

# Define themes
THEMES = {
    "classic": ThemeInfo(
        id="classic",
        name="Classic",
        description="Timeless Magic 8 Ball look",
        colors={
            "bg": "#1a1a2e",
            "primary": "#0f3460",
            "accent": "#e94560",
            "text": "#eaeaea",
            "secondary": "#16213e"
        }
    ),
    "neon": ThemeInfo(
        id="neon",
        name="Neon",
        description="Cyberpunk neon aesthetic",
        colors={
            "bg": "#0a0e27",
            "primary": "#00ff88",
            "accent": "#ff006e",
            "text": "#00ff88",
            "secondary": "#00ffff"
        }
    ),
    "galaxy": ThemeInfo(
        id="galaxy",
        name="Galaxy",
        description="Cosmic galaxy vibes",
        colors={
            "bg": "#0b0014",
            "primary": "#7209b7",
            "accent": "#f72585",
            "text": "#e0aaff",
            "secondary": "#5a189a"
        }
    ),
    "cute": ThemeInfo(
        id="cute",
        name="Cute",
        description="Pastel cute theme",
        colors={
            "bg": "#fef5e7",
            "primary": "#f8b739",
            "accent": "#ff85a2",
            "text": "#333333",
            "secondary": "#fcc5d8"
        }
    ),
    "dark": ThemeInfo(
        id="dark",
        name="Dark Mode",
        description="Easy on the eyes dark mode",
        colors={
            "bg": "#121212",
            "primary": "#1e88e5",
            "accent": "#1e88e5",
            "text": "#ffffff",
            "secondary": "#1f1f1f"
        }
    ),
    "light": ThemeInfo(
        id="light",
        name="Light Mode",
        description="Clean light mode",
        colors={
            "bg": "#ffffff",
            "primary": "#1976d2",
            "accent": "#d32f2f",
            "text": "#000000",
            "secondary": "#f5f5f5"
        }
    )
}

# Define achievements
ACHIEVEMENTS = {
    "first_question": Achievement(
        id="first_question",
        name="First Question",
        description="Ask your first question",
        icon="🎱"
    ),
    "curious_mind": Achievement(
        id="curious_mind",
        name="Curious Mind",
        description="Ask 10 questions",
        icon="🤔"
    ),
    "oracle_seeker": Achievement(
        id="oracle_seeker",
        name="Oracle Seeker",
        description="Ask 50 questions",
        icon="🔮"
    ),
    "master_questioner": Achievement(
        id="master_questioner",
        name="Master Questioner",
        description="Ask 100 questions",
        icon="👑"
    ),
    "devoted_believer": Achievement(
        id="devoted_believer",
        name="Devoted Believer",
        description="Ask 250 questions",
        icon="✨"
    ),
    "wisdom_collector": Achievement(
        id="wisdom_collector",
        name="Wisdom Collector",
        description="Ask 500 questions",
        icon="🌟"
    ),
    "easter_egg_hunter": Achievement(
        id="easter_egg_hunter",
        name="Easter Egg Hunter",
        description="Find an Easter egg",
        icon="🥚"
    )
}


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/", tags=["Root"])
async def serve_homepage():
    """Serve the main HTML page"""
    frontend_path = Path(__file__).parent.parent / "frontend" / "index.html"
    if frontend_path.exists():
        return FileResponse(frontend_path)
    return {"message": "Magic 8 Ball API running! Frontend files not found."}


@app.post("/ask", response_model=AnswerResponse, tags=["Game"])
async def ask_magic8ball(request: QuestionRequest):
    """
    Ask the Magic 8 Ball a question
    
    Returns a random answer based on the question and response pack.
    """
    try:
        answer, answer_type = magic8ball.ask(
            request.question,
            request.response_pack
        )
        
        logger.info(f"Question: {request.question[:50]}... -> {answer}")
        
        return AnswerResponse(
            answer=answer,
            answer_type=answer_type.value,
            response_pack=request.response_pack,
            timestamp=datetime.now(),
            question=request.question
        )
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@app.get("/themes", tags=["Themes"])
async def get_themes():
    """Get all available themes"""
    return {
        "themes": [
            {
                "id": theme.id,
                "name": theme.name,
                "description": theme.description,
                "colors": theme.colors
            }
            for theme in THEMES.values()
        ]
    }


@app.get("/themes/{theme_id}", response_model=ThemeInfo, tags=["Themes"])
async def get_theme(theme_id: str):
    """Get a specific theme by ID"""
    if theme_id not in THEMES:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Theme '{theme_id}' not found"
        )
    return THEMES[theme_id]


@app.get("/response-packs", tags=["Game"])
async def get_response_packs():
    """Get available response packs"""
    packs = magic8ball.get_available_packs()
    return {
        "packs": packs,
        "counts": {
            pack: magic8ball.get_response_count(pack)
            for pack in packs
        }
    }


@app.get("/achievements", tags=["Achievements"])
async def get_achievements():
    """Get all available achievements"""
    return {
        "achievements": [
            {
                "id": ach.id,
                "name": ach.name,
                "description": ach.description,
                "icon": ach.icon
            }
            for ach in ACHIEVEMENTS.values()
        ]
    }


@app.get("/health", tags=["System"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "service": settings.app_name
    }


@app.get("/info", tags=["System"])
async def app_info():
    """Get application information"""
    return {
        "name": settings.app_name,
        "version": "1.0.0",
        "features": [
            "Multiple response packs",
            "6 beautiful themes",
            "Easter eggs",
            "Smooth animations",
            "Responsive design",
            "Achievement system",
            "Question history",
            "Sound effects"
        ]
    }


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    """Handle ValueError exceptions"""
    return ErrorResponse(
        error=str(exc),
        status_code=400
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle all other exceptions"""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return ErrorResponse(
        error="An unexpected error occurred",
        status_code=500
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug
    )
