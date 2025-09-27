# 🌐 AI Agent: Browser Automation

[![Streamlit](https://img.shields.io/badge/Streamlit-FF6B35?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Browser--Use-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://github.com/browser-use/browser-use)

## Overview

**AI Agent: Browser Automation** revolutionizes web automation by allowing you to control browsers using natural language instructions. Instead of writing complex scripts, simply describe what you want to accomplish, and the AI agent will navigate websites, perform searches, extract data, and complete tasks automatically.

Perfect for web scraping, e-commerce research, competitive analysis, and automating repetitive browser tasks without any coding knowledge.

### 🚀 Key Features

- **Natural Language Control**: Describe browser tasks in plain English
- **Intelligent Navigation**: AI understands and executes complex web interactions
- **Real-time Automation**: Watch as the agent performs tasks in a live browser session
- **Data Extraction**: Automatically extract and format structured data from websites
- **Interactive Dashboard**: Streamlit-based UI for task management and result visualization
- **Headless & GUI Modes**: Run with or without visible browser window
- **Multi-site Support**: Works across different websites and platforms
- **Command Line Interface**: Standalone script execution for automated workflows
- **Result Formatting**: Export data in tables, JSON, or Markdown formats

### 🎯 Perfect For

- **E-commerce Research**: Compare prices, check product availability, monitor competitors
- **Data Collection**: Gather information from multiple websites automatically
- **Market Analysis**: Track trends, monitor social media, analyze content
- **Quality Assurance**: Automated testing of web applications and user flows
- **Business Intelligence**: Regular data extraction and reporting tasks

## 🏗️ Architecture

The system combines AI reasoning with browser automation for intelligent web interactions:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Natural       │ ──▶│   AI Agent       │ ──▶│   Browser       │
│   Language      │    │   (Nebius AI)    │    │   Automation    │
│   Instructions  │    │                  │    │                 │
│                 │    │ • Task Planning  │    │ • Navigation    │
│ "Search for     │    │ • Decision Making│    │ • Interaction   │
│  laptops and    │    │ • Error Handling │    │ • Data Extract  │
│  get prices"    │    │ • Result Format  │    │ • Screenshots   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                               │
                               ▼
                       ┌──────────────────┐
                       │   Streamlit UI   │
                       │                  │
                       │ • Task Input     │
                       │ • Live Preview   │
                       │ • Results View   │
                       │ • Export Options │
                       └──────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Chrome browser (automatically managed)
- Nebius AI API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdullahRasheed45/ai-agent-browser-agent.git
   cd ai-agent-browser-agent
   ```

2. **Set up your environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   # Using uv (recommended - faster)
   pip install uv
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

4. **Configure your API key:**
   ```bash
   # Create .env file
   echo "NEBIUS_API_KEY=your_api_key_here" > .env
   ```

### Launch the Application

**Interactive UI Mode:**
```bash
streamlit run app.py
```
Access the web interface at `http://localhost:8501`

**Command Line Mode:**
```bash
uv run main.py
# Or: python main.py
```

## 💡 Usage Examples

### E-commerce Price Research
```
Task: "Go to Flipkart, search for 'wireless headphones under 2000', 
sort by customer rating, and get the name and price of the top 3 products"
```

### Stock Market Monitoring
```
Task: "Navigate to Google Finance, search for Tesla stock, 
and extract the current price, daily change, and market cap"
```

### Competitive Analysis
```
Task: "Visit Amazon and eBay, search for 'iPhone 15', 
compare prices from the first 5 results on each site"
```

### Social Media Research
```
Task: "Go to LinkedIn, search for 'AI engineers in San Francisco', 
and collect the names and companies of the first 10 profiles"
```

### Form Automation
```
Task: "Fill out the contact form on example.com with: 
Name: John Doe, Email: john@example.com, Message: Hello World"
```

## 📊 Features in Detail

### Natural Language Processing
- Understands complex, multi-step instructions
- Handles conditional logic ("if price is above $100, then...")
- Supports task chaining and workflow automation
- Learns from context and previous actions

### Browser Automation Capabilities
- **Navigation**: Go to URLs, click links, use browser back/forward
- **Search**: Enter queries in search boxes, apply filters
- **Data Extraction**: Get text, prices, images, links, tables
- **Form Interaction**: Fill forms, select options, upload files
- **Dynamic Content**: Handle JavaScript-heavy sites and AJAX loading
- **Screenshot Capture**: Visual documentation of automation steps

### Result Processing
- **Structured Output**: Automatically format data into tables
- **Export Options**: JSON, CSV, Markdown, or plain text
- **Data Validation**: Verify extracted information accuracy
- **Error Recovery**: Handle missing elements and page changes

## ⚙️ Configuration

### Environment Variables
```env
# Required
NEBIUS_API_KEY=your_nebius_api_key_here

# Optional Browser Settings
HEADLESS_MODE=true                    # Run without GUI
BROWSER_TIMEOUT=30                    # Page load timeout
WINDOW_SIZE=1920x1080                # Browser window size
USER_AGENT=custom_agent_string       # Custom user agent
```

### Advanced Configuration
```python
# In main.py - customize browser options
browser_config = {
    "headless": True,              # GUI vs headless mode
    "viewport": {"width": 1920, "height": 1080},
    "timeout": 30000,              # Timeout in milliseconds
    "screenshot_on_error": True,   # Capture errors visually
}
```

## 🛠️ Troubleshooting

### Common Issues

**"API Key Error"**
- Verify your Nebius AI API key is correct
- Ensure `.env` file is in the project root
- Check API key has sufficient credits/permissions

**"Browser Launch Failed"**
- Chrome browser is required (auto-installed by browser-use)
- Try running in headless mode: set `HEADLESS_MODE=true`
- Check system permissions for browser automation

**"Task Execution Timeout"**
- Increase timeout values for slow-loading sites
- Simplify complex tasks into smaller steps
- Check internet connection stability

**"Element Not Found"**
- Website structure may have changed
- Try rephrasing instructions more specifically
- Use element descriptions rather than exact selectors

**"Rate Limited by Website"**
- Add delays between requests
- Consider using different user agents
- Respect website terms of service

### Performance Optimization

**Speed Improvements:**
- Use headless mode for faster execution
- Minimize screenshot capture frequency
- Batch similar tasks together
- Cache frequently accessed data

**Reliability Enhancements:**
- Add error recovery instructions to tasks
- Use specific element descriptions
- Test tasks on stable internet connection
- Validate extracted data formats

## 🤝 Contributing

We welcome contributions to enhance browser automation capabilities!

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Install development dependencies: `uv sync --dev`
4. Make your changes and add tests
5. Run tests: `pytest tests/`
6. Commit and push: `git commit -m 'Add amazing feature'`
7. Open a Pull Request

### Contribution Ideas

- Support for additional browsers (Firefox, Safari)
- Advanced data parsing and validation
- Integration with popular APIs (Slack, email, databases)
- Enhanced error handling and recovery mechanisms
- Mobile browser automation support
- Performance monitoring and optimization tools

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[browser-use](https://github.com/browser-use/browser-use)** for excellent browser automation framework
- **[Nebius AI](https://nebius.ai/)** for powerful language model capabilities
- **[Streamlit](https://streamlit.io/)** for rapid web application development
- **Open Source Community** for tools and inspiration

## 📞 Contact

**Muhammad Abdullah Rasheed**
- 🌐 Portfolio: [techvibes360.com](https://techvibes360.com)
- 💼 LinkedIn: [abdullah-rasheed](https://www.linkedin.com/in/abdullahrasheed-/)
- 📧 Email: abdullahrasheed45@gmail.com

---

*Built with ❤️ by Muhammad Abdullah Rasheed. Ready to automate your web browsing with AI?*
