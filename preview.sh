#!/bin/bash
# Quick demo page preview script

echo "🚀 Starting StepFlow Demo Page..."
echo ""
echo "Opening demo page in browser..."
echo "URL: http://localhost:8000/index.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo "---"
echo ""

cd /data/papers/demo
python3 -m http.server 8000
