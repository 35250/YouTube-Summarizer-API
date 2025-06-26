# To run this code you need to install the following dependencies:
# pip install requests
 
import requests
import re
import json
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi import FastAPI
app= FastAPI()

# Your OpenRouter API key (replace this with your actual key)
API_KEY = "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"

# Choose a free model (like "mistralai/mistral-7b-instruct" or "meta-llama/llama-3-8b-instruct")
MODEL = "mistralai/mistral-7b-instruct"

def fetch_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([t['text'] for t in transcript])
        return full_text
    except Exception as e:
        print("Error fetching transcript:", e)
        return None

def summarize_with_openrouter(transcript):
    prompt = f"""Based on the following YouTube transcription, return a brief summary in this exact JSON format only:

{{
  "topic_name": "name of topic",
  "topic_summary": "summary of topic"
}}

Transcript:
{transcript}
"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("Error calling OpenRouter:", response.text)
        return None

def extract_youtube_id(url):
    if "youtube.com/watch?v="  in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")
    

def extract_youtube_id(url):
    """
    Extracts the YouTube video ID from various types of YouTube URLs.
    Supports normal, shortened, and Shorts URLs.
    """
    # Match for standard YouTube URLs
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")    
    


def parse_json_response(response_str):
    try:
        # Remove leading/trailing whitespace just in case
        cleaned_str = response_str.strip()
        
        # Parse it into a Python dictionary
        parsed_json = json.loads(cleaned_str)
        return parsed_json
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return None


def generate():
    video_id = extract_youtube_id(url= "https://www.youtube.com/shorts/DEuIqiWCG6M") 
    transcript = fetch_youtube_transcript(video_id)
    if transcript:
        summary = summarize_with_openrouter(transcript)
        print("\nSummary:\n", summary)


@app.get("/summarize")
def get_summary(url:str):
    video_id= extract_youtube_id(url)
    transcript= fetch_youtube_transcript(video_id)
    if transcript:
        summary= summarize_with_openrouter(transcript) 
        print ("summary:", summary)
        return parse_json_response(summary)
    else:
        return {"Error": "Transcript not found. This may happen if the video has no captions or is restricted."} 
