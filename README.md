# 🧠 CrewAI Event Management Example

This is a simple multi-agent system using CrewAI. It includes 3 agents powered by different LLMs:

- GPT-3.5 (OpenAI)
- Claude (Anthropic)
- Mistral-7B (Mistral)

## 🚀 Run Instructions

1. Install requirements:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys.

3. Run the crew logic:

```bash
python crew_run.py
```

4. Optional: Run the web interface

```bash
streamlit run interface.py
```

## 📁 File Structure

- `.env`: API Keys
- `utils.py`: API loading functions
- `agents.py`: All LLM agents
- `tasks.py`: Simple example tasks
- `tools.py`: Tool used by agents
- `crew_run.py`: Links agents + tasks
- `interface.py`: Web UI
- `database.py`: Local DB for logging
