# Magic 8 Ball - API Documentation

## Base URL
```
http://localhost:8000
```

## Endpoints

### 1. Serve Homepage
```http
GET /
```

**Response:** HTML file

---

### 2. Ask the Magic 8 Ball
```http
POST /ask
Content-Type: application/json

{
  "question": "Will I succeed?",
  "response_pack": "default"
}
```

**Parameters:**
- `question` (string, required): The question to ask (1-500 characters)
- `response_pack` (string, optional): Response pack type
  - `default` - Standard responses
  - `funny` - Humorous responses
  - `serious` - Serious, factual responses
  - `motivational` - Encouraging responses

**Success Response (200):**
```json
{
  "answer": "Yes, definitely",
  "answer_type": "positive",
  "response_pack": "default",
  "timestamp": "2024-01-04T12:34:56.789Z",
  "question": "Will I succeed?"
}
```

**Answer Types:**
- `positive` - Affirmative answer (40% probability)
- `negative` - Negative answer (40% probability)
- `neutral` - Non-committal answer (20% probability)
- `easter_egg` - Special rare answer (5% probability)

**Error Response (400):**
```json
{
  "error": "Question cannot be empty",
  "status_code": 400,
  "timestamp": "2024-01-04T12:34:56.789Z"
}
```

---

### 3. Get All Themes
```http
GET /themes
```

**Response (200):**
```json
{
  "themes": [
    {
      "id": "classic",
      "name": "Classic",
      "description": "Timeless Magic 8 Ball look",
      "colors": {
        "bg": "#1a1a2e",
        "primary": "#0f3460",
        "accent": "#e94560",
        "text": "#eaeaea",
        "secondary": "#16213e"
      }
    }
  ]
}
```

**Available Themes:**
1. `classic` - Blue and red classic look
2. `neon` - Cyberpunk neon aesthetic
3. `galaxy` - Cosmic purple and pink
4. `cute` - Pastel yellow and pink
5. `dark` - Dark mode with blue accents
6. `light` - Light mode with blue accents

---

### 4. Get Specific Theme
```http
GET /themes/{theme_id}
```

**Example:**
```
GET /themes/neon
```

**Response (200):**
```json
{
  "id": "neon",
  "name": "Neon",
  "description": "Cyberpunk neon aesthetic",
  "colors": {
    "bg": "#0a0e27",
    "primary": "#00ff88",
    "accent": "#ff006e",
    "text": "#00ff88",
    "secondary": "#00ffff"
  }
}
```

**Error Response (404):**
```json
{
  "error": "Theme 'invalid' not found",
  "status_code": 404,
  "timestamp": "2024-01-04T12:34:56.789Z"
}
```

---

### 5. Get Response Packs
```http
GET /response-packs
```

**Response (200):**
```json
{
  "packs": ["default", "funny", "serious", "motivational"],
  "counts": {
    "default": {
      "positive": 15,
      "negative": 15,
      "neutral": 15,
      "easter_eggs": 11
    },
    "funny": {
      "positive": 6,
      "negative": 6,
      "neutral": 6,
      "easter_eggs": 4
    }
  }
}
```

---

### 6. Get Achievements
```http
GET /achievements
```

**Response (200):**
```json
{
  "achievements": [
    {
      "id": "first_question",
      "name": "First Question",
      "description": "Ask your first question",
      "icon": "🎱"
    },
    {
      "id": "curious_mind",
      "name": "Curious Mind",
      "description": "Ask 10 questions",
      "icon": "🤔"
    }
  ]
}
```

**All Achievements:**
1. `first_question` (🎱) - Ask 1 question
2. `curious_mind` (🤔) - Ask 10 questions
3. `oracle_seeker` (🔮) - Ask 50 questions
4. `master_questioner` (👑) - Ask 100 questions
5. `devoted_believer` (✨) - Ask 250 questions
6. `wisdom_collector` (🌟) - Ask 500 questions
7. `easter_egg_hunter` (🥚) - Find an easter egg

---

### 7. Health Check
```http
GET /health
```

**Response (200):**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-04T12:34:56.789Z",
  "service": "Magic 8 Ball"
}
```

---

### 8. App Information
```http
GET /info
```

**Response (200):**
```json
{
  "name": "Magic 8 Ball",
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
```

---

## Error Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request (invalid input) |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## CORS

All endpoints support CORS. Requests from any origin are allowed.

---

## Rate Limiting

Not implemented. Future enhancement for production.

---

## WebSocket

Not implemented. Future enhancement for real-time features.

---

## Example Usage

### JavaScript (Fetch API)

```javascript
// Ask a question
const response = await fetch('http://localhost:8000/ask', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    question: 'Will I succeed?',
    response_pack: 'motivational'
  })
});

const data = await response.json();
console.log(data.answer);  // Output: "You've got this!"
```

### Python (Requests)

```python
import requests

response = requests.post(
    'http://localhost:8000/ask',
    json={
        'question': 'Is this test working?',
        'response_pack': 'funny'
    }
)

print(response.json()['answer'])  # Output: Random funny response
```

### cURL

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Will I win?", "response_pack": "default"}'
```

---

## Notes

- All timestamps are in ISO 8601 format (UTC)
- Question input is automatically trimmed of whitespace
- Response selection is pseudo-random
- Easter eggs have ~5% occurrence rate
- All responses are cached in memory (no database queries)
