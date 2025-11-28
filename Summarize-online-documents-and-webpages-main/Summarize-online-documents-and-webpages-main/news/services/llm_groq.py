import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_summary(text: str) -> str:
    """Summarize text using Google's Gemini API."""
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"Summarize this text concisely:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return f"Error: Could not generate summary. {str(e)}"

def extract_text_from_url(url):
    """Fetch and clean text from a URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        if 'application/pdf' in response.headers.get('content-type', ''):
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for element in soup(['script', 'style', 'nav', 'footer', 'iframe']):
            element.decompose()
        return ' '.join(soup.stripped_strings)
    
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def summarize_with_gemini(text, is_url=False):
    """Summarize text using Google's Gemini API."""
    if not text:
        return "Error: No content to summarize."
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"Summarize this text concisely in 3-5 bullet points:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error summarizing: {e}")
        return f"Error: Could not generate summary. {str(e)}"

def summarize_text(text):
    """Summarize raw text."""
    return summarize_with_gemini(text, is_url=False)

def summarize_url(url):
    """Summarize a URL."""
    text = extract_text_from_url(url)
    return summarize_with_gemini(text, is_url=True) if text else "Error: URL content unavailable."

def summarize_urls_parallel(urls, max_workers=5):
    """Process multiple URLs concurrently."""
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(summarize_url, urls))

if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog..."
    print("Text Summary:", summarize_text(text))
    
    print("URL Summary:", summarize_url("https://en.wikipedia.org/wiki/Large_language_model"))
    
    urls = [
        "https://www.nytimes.com/2024/06/01/technology/ai-meta-llama-3.html",
        "https://www.wired.com/story/groq-ai-chips-fast-llm-inference/"
    ]
    print("Parallel Summaries:", summarize_urls_parallel(urls))