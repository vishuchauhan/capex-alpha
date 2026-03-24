class StrategyAgent:
    def analyze(self, industry_signal):
        if industry_signal == "sector_expansion":
            return {
                "strategy_type": "coordinated_growth",
                "strategy_score": 2
            }
        else:
            return {
                "strategy_type": "risk_taking",
                "strategy_score": 1
            }