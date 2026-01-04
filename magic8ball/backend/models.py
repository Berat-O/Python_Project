"""Pydantic models for request/response validation"""
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime


class QuestionRequest(BaseModel):
    """Request model for asking a question"""
    question: str = Field(..., min_length=1, max_length=500, description="The question to ask")
    response_pack: Optional[str] = Field("default", description="Response pack: default, funny, serious, motivational")
    
    @field_validator('question')
    @classmethod
    def question_not_empty(cls, v: str) -> str:
        """Validate question is not just whitespace"""
        if not v.strip():
            raise ValueError('Question cannot be empty or just whitespace')
        return v.strip()


class AnswerResponse(BaseModel):
    """Response model for answer"""
    answer: str = Field(..., description="The Magic 8 Ball answer")
    answer_type: str = Field(..., description="Type: positive, negative, neutral, easter_egg")
    response_pack: str = Field(..., description="Response pack used")
    timestamp: datetime = Field(default_factory=datetime.now)
    question: Optional[str] = Field(None, description="Echo of the question")


class HistoryEntry(BaseModel):
    """A single history entry"""
    id: int
    question: str
    answer: str
    answer_type: str
    timestamp: datetime
    is_favorite: bool = False


class Achievement(BaseModel):
    """Achievement model"""
    id: str = Field(..., description="Achievement ID")
    name: str = Field(..., description="Achievement name")
    description: str = Field(..., description="Achievement description")
    icon: str = Field(..., description="Achievement emoji icon")
    unlocked: bool = False
    unlocked_at: Optional[datetime] = None


class UserSettings(BaseModel):
    """User settings"""
    theme: str = "classic"
    sound_enabled: bool = True
    animation_speed: float = 1.0


class ThemeInfo(BaseModel):
    """Theme information"""
    id: str
    name: str
    description: str
    colors: dict


class ErrorResponse(BaseModel):
    """Error response"""
    error: str = Field(..., description="Error message")
    status_code: int = Field(..., description="HTTP status code")
    timestamp: datetime = Field(default_factory=datetime.now)
