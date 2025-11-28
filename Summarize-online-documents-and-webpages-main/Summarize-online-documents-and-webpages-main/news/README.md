# AI Document Summarizer

A modern, professional web application that transforms lengthy documents and web articles into concise summaries using Google's Gemini AI.

![AI Document Summarizer](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.121.1-green)
![Python](https://img.shields.io/badge/Python-3.11+-blue)

## ✨ Features

- **Text Summarization** - Paste any text and get an instant AI-powered summary
- **URL Summarization** - Extract and summarize content from web URLs
- **Multiple URL Support** - Process multiple URLs simultaneously
- **Modern UI** - Clean, professional interface with smooth animations
- **Fast & Efficient** - Powered by Google's Gemini 2.5 Flash model
- **RESTful API** - JSON API endpoints for integration

## 🚀 Demo

The application provides two input modes:
1. **Text Input** - Direct text summarization
2. **URL Input** - Web scraping and summarization

## 📋 Prerequisites

- Python 3.11 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd news
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Google API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the application**
   
   Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## 📦 Dependencies

- **FastAPI** - Modern web framework
- **Uvicorn** - ASGI server
- **Google Generative AI** - Gemini API client
- **BeautifulSoup4** - Web scraping
- **Jinja2** - Template engine
- **python-dotenv** - Environment variable management
- **python-multipart** - Form data handling

## 🎨 UI Design

The application features a modern, professional design with:
- Clean typography using Inter font
- Subtle shadows and smooth transitions
- Responsive layout
- Professional blue accent colors
- Intuitive tab-based interface

## 🔧 API Endpoints

### `GET /`
Serves the main web interface

### `POST /api/summarize`
JSON API for text and URL summarization

**Request Body:**
```json
{
  "type": "text",
  "content": "Your text here..."
}
```

or for URLs:

```json
{
  "type": "urls",
  "content": ["https://example.com/article1", "https://example.com/article2"]
}
```

**Response:**
```json
{
  "summary": "Generated summary text..."
}
```

## 📁 Project Structure

```
news/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
├── services/
│   ├── __init__.py
│   ├── summarizer.py      # Text summarization logic
│   ├── llm_groq.py        # Gemini API integration
│   └── comparator.py      # Text comparison (future)
├── templates/
│   └── index.html         # Main web interface
└── static/
    └── style.css          # Additional styles (optional)
```

## 🔐 Security Notes

- Never commit your `.env` file
- Keep your API keys secure
- The `.gitignore` file is configured to exclude sensitive data
- Use environment variables for all secrets

## 🚀 Deployment

For production deployment:

1. Set `reload=False` in `uvicorn.run()` in `main.py`
2. Use a production ASGI server like Gunicorn
3. Set up proper environment variables
4. Consider using a reverse proxy (nginx)
5. Enable HTTPS

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- UI inspired by modern design principles

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note:** This application requires a Google Gemini API key to function. The API has usage limits on the free tier. Please refer to [Google's pricing](https://ai.google.dev/pricing) for details.
