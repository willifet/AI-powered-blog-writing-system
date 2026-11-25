import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

load_dotenv()

llm = LLM(
    model=os.getenv("MODEL", "openai/gpt-4o-mini"),
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

@CrewBase
class BlogWritingCrew():
    """Blog Writing Crew"""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=llm,
            verbose=True
        )
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )
    
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            llm=llm,
            verbose=True
        )
    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            context=[self.research_task()]
        )
    
    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            llm=llm,
            verbose=True
        )
    
    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],
            context=[self.writing_task()],
            output_file='output/blog_post.md'
        )

    @agent
    def social_media_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_manager'],
            llm=llm,
            verbose=True
        )
    
    @task
    def social_media_task(self) -> Task:
        return Task(
            config=self.tasks_config['social_media_task'],
            context=[self.editing_task()],
            output_file='output/social_media_posts.md'
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )