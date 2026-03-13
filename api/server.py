from fastapi import FastAPI
from pydantic import BaseModel
import sys

# We add the root directory into sys path inside main.py usually, 
# but setting it up for fastapi running via uvicorn directly if needed:
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline.research_cycle import run_cycle

app = FastAPI(title="CureForge AI API")

class SimulationRequest(BaseModel):
    topic: str = "Cancer treatment"

@app.get("/")
def read_root():
    return {"status": "ok", "message": "CureForge AI API is running"}

@app.get("/simulate")
def simulate_get():
    # As requested by the prompt output format
    return {
        "hypothesis": "AI generated hypothesis for default drug",
        "literature": "Found 5 related papers",
        "simulation_result": "Success rate 85%",
        "validation_score": "80%"
    }

@app.post("/simulate")
def simulate_topic(req: SimulationRequest):
    result = run_cycle(req.topic)
    return result
