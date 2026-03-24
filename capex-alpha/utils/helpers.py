import csv
import os

def save_results(results, filename="output/results.csv"):
    os.makedirs("output", exist_ok=True)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Company",
            "Score",
            "Strategy",
            "Industry Signal",
            "Financial Score",
            "NLP Score"
        ])

        for r in results:
            writer.writerow([
                r["company"],
                r["score"],
                r["strategy"],
                r["industry_signal"],
                r["financial_score"],
                r["nlp_score"]
            ])


def print_results(results):
    print("\n===== CAPEX RANKING =====\n")

    for r in results:
        print(f"{r['company']} → Score: {r['score']} | Strategy: {r['strategy']}")

    print("\n=========================\n")