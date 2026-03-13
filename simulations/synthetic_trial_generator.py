import pandas as pd
import numpy as np

class TrialSimulator:
    def __init__(self):
        pass

    def run_simulation(self, hypothesis, num_patients=100):
        # Generate synthetic data
        np.random.seed(42)
        ages = np.random.randint(20, 80, num_patients)
        efficacies = np.random.normal(0.6, 0.1, num_patients)
        
        df = pd.DataFrame({
            "patient_id": range(num_patients),
            "age": ages,
            "efficacy_score": efficacies
        })
        
        success_rate = (df['efficacy_score'] > 0.5).mean()
        return {
            "hypothesis": hypothesis,
            "success_rate": float(success_rate),
            "details": f"Simulated {num_patients} patients."
        }
