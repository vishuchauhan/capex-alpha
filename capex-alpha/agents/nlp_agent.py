class NLPAgent:
    def analyze(self, text):
        keywords = ["expansion", "capacity", "capex", "plant", "investment"]

        score = 0
        found = []

        for word in keywords:
            if word in text.lower():
                score += 1
                found.append(word)

        return {"nlp_score": score, "nlp_keywords": found}