"""Comprehensive tests for Magic 8 Ball backend"""
import pytest
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from magic8ball import Magic8Ball, AnswerType
from models import QuestionRequest, AnswerResponse


@pytest.fixture
def magic_ball():
    """Create Magic 8 Ball instance for testing"""
    return Magic8Ball()


@pytest.fixture
def responses_file(tmp_path):
    """Create temporary responses file"""
    responses = {
        "positive": ["Yes", "Definitely"],
        "negative": ["No", "Never"],
        "neutral": ["Maybe", "Ask again"],
        "easter_eggs": ["🎱"]
    }
    file_path = tmp_path / "test_responses.json"
    with open(file_path, 'w') as f:
        json.dump(responses, f)
    return file_path


class TestMagic8BallCore:
    """Test core Magic 8 Ball functionality"""
    
    def test_initialization(self, magic_ball):
        """Test Magic 8 Ball initializes correctly"""
        assert magic_ball is not None
        assert magic_ball.easter_egg_chance == 0.05
        assert len(magic_ball.responses) == 4
        assert all(
            answer_type in magic_ball.responses 
            for answer_type in [
                AnswerType.POSITIVE, 
                AnswerType.NEGATIVE, 
                AnswerType.NEUTRAL,
                AnswerType.EASTER_EGG
            ]
        )
    
    def test_load_responses(self, responses_file):
        """Test loading custom responses"""
        ball = Magic8Ball(str(responses_file))
        assert len(ball.responses[AnswerType.POSITIVE]) == 2
        assert "Yes" in ball.responses[AnswerType.POSITIVE]
    
    def test_responses_not_empty(self, magic_ball):
        """Test all response types have answers"""
        for answer_type in [
            AnswerType.POSITIVE, 
            AnswerType.NEGATIVE, 
            AnswerType.NEUTRAL,
            AnswerType.EASTER_EGG
        ]:
            assert len(magic_ball.responses[answer_type]) > 0
    
    def test_ask_valid_question(self, magic_ball):
        """Test asking a valid question"""
        answer, answer_type = magic_ball.ask("Will I succeed?")
        
        assert isinstance(answer, str)
        assert len(answer) > 0
        assert isinstance(answer_type, AnswerType)
        assert answer_type in [
            AnswerType.POSITIVE, 
            AnswerType.NEGATIVE, 
            AnswerType.NEUTRAL,
            AnswerType.EASTER_EGG
        ]
    
    def test_ask_empty_question(self, magic_ball):
        """Test empty question raises error"""
        with pytest.raises(ValueError):
            magic_ball.ask("")
        
        with pytest.raises(ValueError):
            magic_ball.ask("   ")
    
    def test_ask_invalid_response_pack(self, magic_ball):
        """Test invalid response pack raises error"""
        with pytest.raises(ValueError):
            magic_ball.ask("Will I win?", "invalid_pack")
    
    def test_all_response_packs(self, magic_ball):
        """Test all response packs work"""
        question = "Am I awesome?"
        packs = magic_ball.get_available_packs()
        
        for pack in packs:
            answer, answer_type = magic_ball.ask(question, pack)
            assert isinstance(answer, str)
            assert len(answer) > 0
    
    def test_randomness(self, magic_ball):
        """Test answer variation"""
        question = "Is this random?"
        answers = set()
        
        for _ in range(20):
            answer, _ = magic_ball.ask(question)
            answers.add(answer)
        
        assert len(answers) > 1
    
    def test_get_available_packs(self, magic_ball):
        """Test getting available packs"""
        packs = magic_ball.get_available_packs()
        assert isinstance(packs, list)
        assert len(packs) >= 4
        assert "default" in packs
        assert "funny" in packs
        assert "serious" in packs
        assert "motivational" in packs
    
    def test_get_response_count(self, magic_ball):
        """Test response counts"""
        counts = magic_ball.get_response_count()
        
        assert isinstance(counts, dict)
        for key in ["positive", "negative", "neutral", "easter_eggs"]:
            assert key in counts
            assert counts[key] > 0


class TestPydanticModels:
    """Test Pydantic validation models"""
    
    def test_question_request_valid(self):
        """Test valid question request"""
        req = QuestionRequest(question="Will I be happy?")
        assert req.question == "Will I be happy?"
        assert req.response_pack == "default"
    
    def test_question_request_with_pack(self):
        """Test question with response pack"""
        req = QuestionRequest(
            question="Am I cool?",
            response_pack="funny"
        )
        assert req.response_pack == "funny"
    
    def test_question_whitespace_stripped(self):
        """Test whitespace stripping"""
        req = QuestionRequest(question="   Will I win?   ")
        assert req.question == "Will I win?"
    
    def test_question_empty_fails(self):
        """Test empty question fails"""
        with pytest.raises(ValueError):
            QuestionRequest(question="")
    
    def test_question_too_long_fails(self):
        """Test max length validation"""
        long_question = "a" * 501
        with pytest.raises(ValueError):
            QuestionRequest(question=long_question)
    
    def test_answer_response(self):
        """Test answer response model"""
        resp = AnswerResponse(
            answer="Yes",
            answer_type="positive",
            response_pack="default",
            question="Will I succeed?"
        )
        
        assert resp.answer == "Yes"
        assert resp.answer_type == "positive"


class TestBalancedDistribution:
    """Test answer distribution balance"""
    
    def test_distribution(self):
        """Test balanced distribution"""
        ball = Magic8Ball()
        distribution = {
            AnswerType.POSITIVE: 0,
            AnswerType.NEGATIVE: 0,
            AnswerType.NEUTRAL: 0,
            AnswerType.EASTER_EGG: 0
        }
        
        trials = 1000
        for _ in range(trials):
            _, answer_type = ball.ask("Test?")
            distribution[answer_type] += 1
        
        positive_ratio = distribution[AnswerType.POSITIVE] / trials
        negative_ratio = distribution[AnswerType.NEGATIVE] / trials
        
        assert 0.3 < positive_ratio < 0.5
        assert 0.3 < negative_ratio < 0.5


class TestResponsePacks:
    """Test response packs"""
    
    def test_all_packs_have_all_types(self):
        """Test pack completeness"""
        ball = Magic8Ball()
        
        for pack_name in ball.get_available_packs():
            pack = ball.response_packs[pack_name]
            assert AnswerType.POSITIVE in pack
            assert AnswerType.NEGATIVE in pack
            assert AnswerType.NEUTRAL in pack
            assert AnswerType.EASTER_EGG in pack
    
    def test_funny_pack(self):
        """Test funny response pack"""
        ball = Magic8Ball()
        answer, _ = ball.ask("Is this funny?", "funny")
        assert isinstance(answer, str)
    
    def test_serious_pack(self):
        """Test serious response pack"""
        ball = Magic8Ball()
        answer, _ = ball.ask("Is this serious?", "serious")
        assert isinstance(answer, str)
    
    def test_motivational_pack(self):
        """Test motivational response pack"""
        ball = Magic8Ball()
        answer, _ = ball.ask("Am I motivated?", "motivational")
        assert isinstance(answer, str)


class TestEdgeCases:
    """Test edge cases"""
    
    def test_unicode_questions(self):
        """Test unicode support"""
        ball = Magic8Ball()
        answer, _ = ball.ask("Will I find 💎? 🎱")
        assert isinstance(answer, str)
    
    def test_long_question(self):
        """Test long questions"""
        ball = Magic8Ball()
        long_question = "Is this a very long question? " * 10
        answer, _ = ball.ask(long_question[:500])
        assert isinstance(answer, str)
    
    def test_special_characters(self):
        """Test special characters"""
        ball = Magic8Ball()
        answer, _ = ball.ask("Will I win @#$%? (!@#$)")
        assert isinstance(answer, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
