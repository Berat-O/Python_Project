#!/bin/bash
# Magic 8 Ball - Startup Script

echo "🎱 Magic 8 Ball - Startup"
echo "========================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "✨ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt --quiet

# Run tests
echo "🧪 Running tests..."
pytest tests/ -v --tb=short

# Start the server
echo ""
echo "🚀 Starting Magic 8 Ball server..."
echo "   📍 URL: http://localhost:8000"
echo "   🛑 Press Ctrl+C to stop"
echo ""

python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
