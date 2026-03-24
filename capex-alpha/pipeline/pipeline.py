from agents.coordinator_agent import CoordinatorAgent
from utils.helpers import save_results, print_results

def run_pipeline():
    coordinator = CoordinatorAgent()

    results = coordinator.run_multiple()

    print_results(results)
    save_results(results)