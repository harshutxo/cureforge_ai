from .worker_agent import WorkerAgent

class DomainSupervisorAgent:
    """
    Layer 2 - Domain Supervisor Agent
    Manages a specific scientific domain and spawns/retires specialized workers.
    """
    def __init__(self, domain_name: str):
        self.domain_name = domain_name
        self.workers = []

    def spawn_worker(self, name: str, specialization: str):
        worker = WorkerAgent(name, specialization, self.domain_name)
        self.workers.append(worker)
        print(f"[{self.domain_name} Supervisor] Spawned worker: {name} ({specialization})")
        return worker

    def retire_worker(self, name: str):
        self.workers = [w for w in self.workers if w.name != name]
        print(f"[{self.domain_name} Supervisor] Retired worker: {name}")

    def manage_domain_research(self, sub_topic: str):
        print(f"[{self.domain_name} Supervisor] Managing research on: {sub_topic}")
        if not self.workers:
            self.spawn_worker(f"Literature-Miner-1", "data_ingestion")
            self.spawn_worker(f"Hypothesis-Tester-1", "hypothesis_generation")
            
        results = []
        for worker in self.workers:
            # Task distribution based on worker specialization (simplistic)
            results.append(worker.execute_task(sub_topic))
            
        return {
            "domain": self.domain_name,
            "worker_outputs": results,
            "summary": f"Aggregated findings from {len(self.workers)} workers in {self.domain_name}."
        }
