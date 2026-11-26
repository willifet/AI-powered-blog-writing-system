# Blog Writing Crew

A multi-agent blog-writing project powered by [CrewAI](https://crewai.com). The crew uses configurable agents and tasks to research a topic and create written content.

## Requirements

- Python **3.12**
- [uv](https://docs.astral.sh/uv/)
- An API key for the LLM provider you use, configured in `.env`

## Installation

Install `uv` if it is not already available:

```bash
pip install uv
```

From the project root, install the project and its dependencies:

```bash
crewai install
```

Add the required provider API key to your `.env` file before running the crew.

## Run the crew

Start the crew from the project root:

```bash
crewai run
```

By default, the crew runs with the topic **“How does population growth affect the economy?”**. The entry point is `src/blog_writing_crew/main.py`.

## Customize the crew

- Edit `src/blog_writing_crew/config/agents.yaml` to define the agents.
- Edit `src/blog_writing_crew/config/tasks.yaml` to define their tasks.
- Update `src/blog_writing_crew/crew.py` to change orchestration, tools, or agent settings.
- Update `src/blog_writing_crew/main.py` to change the default topic or inputs.

## Project structure

```text
src/blog_writing_crew/
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── crew.py
└── main.py
```

## Support

- [CrewAI documentation](https://docs.crewai.com)
- [CrewAI GitHub repository](https://github.com/crewAIInc/crewAI)
- [CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)
