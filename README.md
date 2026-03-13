# cureforge_ai
CureForge AI

Autonomous research agents that analyze clinical trial simulations to generate cure hypotheses.

Architecture:
- Director Agent
- Domain Supervisor Agents
- Research Worker Agents

Capabilities:
• clinical trial simulation
• LLM reasoning
• literature mining
• hypothesis generation
• dynamic agent spawning

Tech Stack:
Python
FastAPI
Docker
Vector Search
LLM integration

Run locally:

pip install -r requirements.txt
python main.py

Features Implemented

- Autonomous AI research agents
- Clinical trial simulation engine
- LLM-powered hypothesis generation
- FastAPI server
- Docker deployment
-----------------------------------
           Director Agent
                |
      -----------------------
      |         |           |
Supervisor  Supervisor  Supervisor
      |         |           |
   Worker     Worker      Worker
------------------------------------
   Example Output

GET /simulate

{
 "hypothesis": "Drug X may improve survival",
 "confidence": 0.72
}
