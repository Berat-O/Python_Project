"""Core Magic 8 Ball game logic"""
import json
import random
from pathlib import Path
from datetime import datetime, date
from typing import Dict, List, Optional, Tuple
from enum import Enum


class AnswerType(str, Enum):
    """Types of answers"""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    EASTER_EGG = "easter_egg"


class Magic8Ball:
    """Core Magic 8 Ball game engine"""
    
    def __init__(self, responses_file: Optional[str] = None):
        """
        Initialize Magic 8 Ball
        
        Args:
            responses_file: Path to JSON file with responses. If None, uses default location.
        """
        self.responses: Dict[str, List[str]] = {}
        self.response_packs: Dict[str, Dict[str, List[str]]] = {}
        self._load_responses(responses_file)
        self._load_response_packs()
        self.easter_egg_chance = 0.05  # 5% chance of easter egg
        
    def _load_responses(self, responses_file: Optional[str] = None) -> None:
        """Load responses from JSON file"""
        if responses_file is None:
            responses_file = Path(__file__).parent / "responses.json"
        else:
            responses_file = Path(responses_file)
            
        with open(responses_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.responses = {
                AnswerType.POSITIVE: data.get("positive", []),
                AnswerType.NEGATIVE: data.get("negative", []),
                AnswerType.NEUTRAL: data.get("neutral", []),
                AnswerType.EASTER_EGG: data.get("easter_eggs", [])
            }
    
    def _load_response_packs(self) -> None:
        """Load response packs (funny, serious, motivational, etc.)"""
        self.response_packs = {
            "default": self.responses,
            "funny": {
                AnswerType.POSITIVE: [
                    "Heck yeah!", "You betcha!", "Duh, obviously",
                    "That's what I'm talking about!", "You're gonna crush it!",
                    "100% certified yes"
                ],
                AnswerType.NEGATIVE: [
                    "Nope nope nope", "Not happening, buddy",
                    "In your dreams", "Bro...", "Yeah, no",
                    "Absolutely not gonna happen"
                ],
                AnswerType.NEUTRAL: [
                    "Maybe? 🤷", "Ask again later, coward",
                    "I'm thinking...", "Flip a coin, I'm tired",
                    "Your guess is as good as mine", "42"
                ],
                AnswerType.EASTER_EGG: [
                    "The answer is yes but also no", "Plot twist: it's complicated",
                    "This is awkward...", "Error 404: Answer not found"
                ]
            },
            "serious": {
                AnswerType.POSITIVE: [
                    "Affirmative", "The data supports this",
                    "Logically sound", "All indicators suggest yes",
                    "Correct", "This is the way"
                ],
                AnswerType.NEGATIVE: [
                    "Negative", "Unlikely based on current conditions",
                    "Statistically improbable", "The evidence suggests otherwise",
                    "That's a hard no", "Incorrect"
                ],
                AnswerType.NEUTRAL: [
                    "Inconclusive", "Requires further analysis",
                    "Insufficient data", "Status: unknown",
                    "Variables are unclear", "Need more information"
                ],
                AnswerType.EASTER_EGG: [
                    "The universe remains silent",
                    "Forces of nature are indifferent",
                    "Quantum uncertainty principle applies"
                ]
            },
            "motivational": {
                AnswerType.POSITIVE: [
                    "You've got this!", "Absolutely, believe in yourself",
                    "Go for it!", "Your dreams are valid",
                    "Success is within reach",
                    "You're capable of amazing things"
                ],
                AnswerType.NEGATIVE: [
                    "Not now, but don't give up",
                    "Keep trying, the universe has timing",
                    "This setback is growth in disguise",
                    "Not yet, but you will get there",
                    "Learn from this and grow",
                    "Patience, your time will come"
                ],
                AnswerType.NEUTRAL: [
                    "The power is in your hands",
                    "Only you know what's best for you",
                    "Trust your intuition", "Listen to your heart",
                    "You have the answers within",
                    "Follow what feels right"
                ],
                AnswerType.EASTER_EGG: [
                    "You are stronger than you think",
                    "Every question brings you closer to wisdom",
                    "The fact that you're asking means you care"
                ]
            }
        }
    
    def ask(self, question: str, response_pack: str = "default") -> Tuple[str, AnswerType]:
        """
        Ask the Magic 8 Ball a question
        
        Args:
            question: The question to ask
            response_pack: Which response pack to use
            
        Returns:
            Tuple of (answer_text, answer_type)
            
        Raises:
            ValueError: If question is empty or response_pack is invalid
        """
        if not question or not question.strip():
            raise ValueError("Question cannot be empty")
        
        if response_pack not in self.response_packs:
            raise ValueError(f"Unknown response pack: {response_pack}")
        
        # Determine if this is an easter egg
        if random.random() < self.easter_egg_chance:
            answer_type = AnswerType.EASTER_EGG
        else:
            # 40% positive, 40% negative, 20% neutral
            answer_type = random.choices(
                [AnswerType.POSITIVE, AnswerType.NEGATIVE, AnswerType.NEUTRAL],
                weights=[40, 40, 20],
                k=1
            )[0]
        
        pack = self.response_packs[response_pack]
        answers = pack[answer_type]
        answer = random.choice(answers)
        
        return answer, answer_type
    
    def get_available_packs(self) -> List[str]:
        """Get list of available response packs"""
        return list(self.response_packs.keys())
    
    def get_response_count(self, response_pack: str = "default") -> Dict[str, int]:
        """Get count of responses by type"""
        if response_pack not in self.response_packs:
            raise ValueError(f"Unknown response pack: {response_pack}")
        
        pack = self.response_packs[response_pack]
        return {
            "positive": len(pack[AnswerType.POSITIVE]),
            "negative": len(pack[AnswerType.NEGATIVE]),
            "neutral": len(pack[AnswerType.NEUTRAL]),
            "easter_eggs": len(pack[AnswerType.EASTER_EGG])
        }
