from .domain_supervisor import DomainSupervisorAgent

class GlobalDirectorAgent:
    """
    Layer 1 - Global Director Agent
    Coordinates system-wide priorities, resource allocation, and discovery strategy.
    """
    def __init__(self):
        self.domains = {
            "neurodegeneration": DomainSupervisorAgent("Neurodegeneration"),
            "metabolic_aging": DomainSupervisorAgent("Metabolic Aging"),
            "immune_aging": DomainSupervisorAgent("Immune Aging"),
            "cardiovascular_aging": DomainSupervisorAgent("Cardiovascular Aging")
        }

    def direct_research(self, topic: str):
        print(f"[Global Director] Directing research on overarching topic: {topic}")
        # Simplistic routing: assign to a relevant domain supervisor, or all if broad
        routing_key = "metabolic_aging" # Default placeholder
        for key in self.domains.keys():
            if key.split('_')[0] in topic.lower():
                routing_key = key
                break
                
        print(f"[Global Director] Routing '{topic}' to {self.domains[routing_key].domain_name} supervisor.")
        return self.domains[routing_key].manage_domain_research(topic)
