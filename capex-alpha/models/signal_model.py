import pandas as pd

def detect_capex_signals(df):
    df["cwip_growth"] = df["cwip"].pct_change()
    df["capex_flag"] = df["cwip_growth"] > 0.2
    return df