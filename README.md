# AI Blog Writing Crew

An autonomous, multi-agent AI content generation system built with Python, CrewAI and OpenAI. The application uses specialised AI agents to research topics, write engaging blog articles, review content and generate social media posts.

The project demonstrates how agentic AI systems can collaborate through task delegation, sequential orchestration and shared context to automate a real-world content creation workflow.

## Project Overview

The AI Blog Writing Crew automates the process of transforming a topic into a researched, structured and edited blog article, alongside ready-to-use social media content.

Rather than relying on a single LLM prompt, the application uses four specialised AI agents, each responsible for a specific stage of the content creation process.

## Key Features

* **Multi-agent orchestration:** Four specialised agents collaborate to complete the content generation workflow.

* **Automated research:** The Researcher gathers relevant information about the requested topic.

* **AI-powered writing:** The Writer transforms research into a structured and engaging blog article.

* **Content quality assurance:** The Editor reviews and improves the generated article.

* **Social media content generation:** The Social Media Manager creates promotional content based on the final blog.

* **Sequential task execution:** CrewAI manages task dependencies and passes relevant context between agents.

* **API-ready architecture:** The crew can be exposed through FastAPI for programmatic access.

## Architecture and Workflow

The system follows a sequential multi-agent architecture:

1. **Researcher:** Investigates the topic and gathers relevant information.

2. **Writer:** Produces the first draft using the research findings.

3. **Editor:** Reviews the draft for quality, clarity, structure and accuracy.

4. **Social Media Manager:** Creates engaging social media content based on the final article.


## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python 3.12 | Core programming language |
| CrewAI | Multi-agent orchestration |
| OpenAI GPT-4o-mini | LLM powering the agents|
| YAML | Agent and task configuration |
| uv | Python package and environment management |
| FastAPI | REST API layer |
| Uvicorn | ASGI application server |
| Pydantic | Request validation |


## Project Structure

```
blog_writing_crew/
│
├── src/
│   └── blog_writing_crew/
│       ├── __init__.py
│       ├── crew.py
│       ├── main.py
│       └── api.py
│
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
│
├── output/
│   ├── blog_post.md
│   └── social_posts.md
│
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

_Note: Adapt the structure above if your configuration files are located inside the Python package._

## Getting Started

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-blog-writing-crew.git
cd ai-blog-writing-crew

### 2. Install uv
If you do not already have uv installed
curl -LsSf https://astral.sh/uv/install.sh | sh

### 3. Install dependencies 
uv sync
If FastAPI is npt already included:

uv add fastapi "uvicorn[standard]"

### 4. Configure environment variables

Create a .env file in the project root.

OPENAI_API_KEY=your_openai_api_key
MODEL=openai/gpt-4o-mini

Never commit your actual .env file or API credentials to GitHub.

### 5. Run the crew

uv run run_crew

Alternatively, use the Python entry point:

uv run python -m blog_writing_crew.main

Use the entry point supported by your actual project configuration.

## Generated Outputs

After successful execution, the application generates:

### 1. Blog article

output/blog_post.md

Contains the researched, written and edited blog article.

### 2. Social media content

output/social_posts.md

Contains promotional social media content generated from the final blog article.

## Running the FastAPI Application2=

Start the API server:

uv run uvicorn blog_writing_crew.api:app --reload --app-dir src

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

### Available Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /health | Checks API availability |
| POST | /generate-blog | Starts the blog generation workflow |

Example request:

{
  "topic": "The Impact of Artificial Intelligence on Healthcare"
}

### Future Improvements

* Deploy the application to a cloud platform.

* Introduce persistent storage for generated articles.

* Implement asynchronous background job processing.

* Add authentication and API rate limiting.

* Integrate additional LLM providers.

* Introduce automated testing and CI/CD pipelines.

* Build a frontend interface for interacting with the AI crew.


### Learning Outcomes

This project demonstrates practical experience with:

* Agentic AI and multi-agent systems.

* LLM integration and prompt engineering.

* Sequential task orchestration.

* Python application development.

* REST API development using FastAPI.

* Environment and dependency management.

* Preparing AI applications for deployment.


### Security

API credentials are managed through environment variables. The repository includes an .env.example template rather than actual API credentials.

### Author

Developed as part of my journey into AI Engineering, exploring practical applications of autonomous agents and LLM-powered systems.





