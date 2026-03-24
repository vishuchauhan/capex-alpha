class IndustryAgent:
    def analyze(self, peer_data):
        expanding = sum([1 for p in peer_data if p["capex"]])

        if expanding > len(peer_data) / 2:
            return {"industry_signal": "sector_expansion"}
        else:
            return {"industry_signal": "isolated_expansion"}