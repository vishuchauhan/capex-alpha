from agents.financial_agent import FinancialAgent
from agents.nlp_agent import NLPAgent
from agents.industry_agent import IndustryAgent
from agents.strategy_agent import StrategyAgent

class CoordinatorAgent:
    def __init__(self):
        self.fin = FinancialAgent()
        self.nlp = NLPAgent()
        self.ind = IndustryAgent()
        self.strat = StrategyAgent()

    def run_multiple(self):

        companies = [
            {
                "name": "Reliance",
                "data": {"cwip_growth": 0.35, "debt_increase": True, "capex_to_sales": 0.18},
                "text": "Announced new plant and capacity expansion",
                "peers": [{"capex": True}, {"capex": True}, {"capex": False}]
            },
            {
                "name": "Tata Steel",
                "data": {"cwip_growth": 0.25, "debt_increase": True, "capex_to_sales": 0.12},
                "text": "Expansion in steel production capacity",
                "peers": [{"capex": True}, {"capex": True}, {"capex": True}]
            },
            {
                "name": "Infosys",
                "data": {"cwip_growth": 0.05, "debt_increase": False, "capex_to_sales": 0.03},
                "text": "Focus on digital services growth",
                "peers": [{"capex": False}, {"capex": False}]
            }
        ]

        results = []

        for company in companies:

            fin = self.fin.analyze(company["data"])
            nlp = self.nlp.analyze(company["text"])
            ind = self.ind.analyze(company["peers"])
            strat = self.strat.analyze(ind["industry_signal"])

            score = (
                fin["financial_score"] * 0.3 +
                nlp["nlp_score"] * 0.25 +
                strat["strategy_score"] * 0.45
            )

            results.append({
                "company": company["name"],
                "score": round(score, 2),
                "strategy": strat["strategy_type"],
                "industry_signal": ind["industry_signal"],
                "financial_score": fin["financial_score"],
                "nlp_score": nlp["nlp_score"]
            })

        # 🔥 SORT by score (important)
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        return results