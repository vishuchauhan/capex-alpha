class FinancialAgent:
    def analyze(self, company_data):
        score = 0
        reasons = []

        if company_data["cwip_growth"] > 0.2:
            score += 1
            reasons.append("High CWIP growth")

        if company_data["debt_increase"]:
            score += 1
            reasons.append("Debt raised")

        if company_data["capex_to_sales"] > 0.1:
            score += 1
            reasons.append("High Capex/Sales")

        return {"financial_score": score, "financial_reasons": reasons}