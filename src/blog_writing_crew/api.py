
from datetime import datetime
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from blog_writing_crew.crew import BlogWritingCrew


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create FastAPI application
app = FastAPI(
    title="AI Blog Writing API",
    description="An API powered by a multi-agent CrewAI workflow.",
    version="1.0.0"
)


# Define the incoming request structure
class BlogRequest(BaseModel):
    topic: str = Field(
        min_length=5,
        max_length=300,
        description="The topic for the blog post"
    )


# Define the API endpoint
@app.post("/generate-blog")
def generate_blog(request: BlogRequest):

    try:
        logger.info("Starting blog generation")

        # Create and execute the CrewAI workflow
        crew_instance = BlogWritingCrew().crew()

        result = crew_instance.kickoff(
            inputs={
                "topic": request.topic,
                "current_year": datetime.now().year
            }
        )

        # Retrieve individual task outputs
        task_outputs = result.tasks_output

        return {
            "status": "success",
            "topic": request.topic,
            "research": task_outputs[0].raw,
            "blog_post": task_outputs[2].raw,
            "social_media_content": task_outputs[3].raw
        }

    except Exception:
        logger.exception("Blog generation failed")

        raise HTTPException(
            status_code=500,
            detail="Blog generation failed. Please try again."
        )


# Health-check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Blog Writing API is running"
    }
