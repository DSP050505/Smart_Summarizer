from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re
import torch
from flask_cors import CORS  # Import CORS
app = Flask(__name__)
CORS(app)

# Initialize the T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

@app.route('/')
def health_check():
    return "Health Check: Flask app is running!"

@app.route('/items', methods=['GET', 'POST'])
def manage_items():
    global items
    if request.method == 'GET':
        return jsonify(items)
    
    if request.method == 'POST':
        new_item = request.json.get('item')
        if new_item:
            items.append(new_item)
            return jsonify({"message": "Item added", "item": new_item}), 201
        return jsonify({"message": "Item content missing"}), 400

@app.route('/transcript/<video_id>', methods=['GET'])
def get_transcript(video_id):
    languages = ['en', 'hi']  # You can add more languages if needed
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        transcript_text = ' '.join([entry['text'] for entry in transcript])
        return jsonify({"transcript": transcript_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def chunk_text(text, chunk_size=512):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def summarize_text(text):
    input_text = "summarize: " + text
    inputs = tokenizer.encode(input_text, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=300,
        min_length=100,
        length_penalty=2.0,
        num_beams=8,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def extract_video_id(youtube_url):
    video_id = None
    regex_patterns = [
        r'(?<=v=)[^&#]+',
        r'(?<=be/)[^&#]+',
        r'(?<=embed/)[^&#]+',
        r'(?<=v/)[^&#]+',
        r'(?<=youtu.be/)[^&#]+',
        r'(?<=youtube.com/shorts/)[^&#]+'
    ]
    for pattern in regex_patterns:
        match = re.search(pattern, youtube_url)
        if match:
            video_id = match.group(0)
            break
    return video_id

@app.route('/api/summarize', methods=['GET'])
def api_summarize():
    youtube_url = request.args.get('youtube_url')
    if not youtube_url:
        return jsonify({"error": "youtube_url query parameter is required"}), 400
    
    video_id = extract_video_id(youtube_url)
    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400
    
    languages = ['en', 'hi']
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        transcript_text = ' '.join([entry['text'] for entry in transcript])
        
        chunks = chunk_text(transcript_text)
        summaries = [summarize_text(chunk) for chunk in chunks]
        
        final_summary = ' '.join(summaries)
        
        return jsonify({"summary": final_summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    items = []
    app.run(debug=True)
