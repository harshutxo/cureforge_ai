import time
import random

class WorkerAgent:
    """
    Layer 3 - Research Worker Agent
    Performs specific tasks like data ingestion, dataset analysis, etc.
    """
    def __init__(self, name: str, specialization: str, domain: str="General"):
        self.name = name
        self.specialization = specialization
        self.domain = domain

    def execute_task(self, topic: str):
        print(f"[{self.name} | {self.specialization}] Executing task for {topic}...")
        time.sleep(0.5)
        
        if self.specialization == "data_ingestion":
            return self.data_ingestion(topic)
        elif self.specialization == "hypothesis_generation":
            return self.generate_hypothesis(topic)
        else:
            return self.perform_general_research(topic)

    def data_ingestion(self, topic: str):
        # Step 1 logic
        return f"Ingested 15 papers and 3 datasets related to '{topic}'."

    def generate_hypothesis(self, topic: str):
        # Step 3 logic
        return f"Hypothesized a novel pathway modulation target for '{topic}' with high plausibility."

    def perform_general_research(self, topic: str):
        findings = f"General findings on {topic}. Confidence: {random.uniform(0.7, 0.99):.2f}"
        return findings
