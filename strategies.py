def moving_average_strategy(data):
    data["Signal"] = 0

    data.loc[
        data["MA20"] > data["MA50"],
        "Signal"
    ] = 1
    data["Position"] = data["Signal"].diff().fillna(0)
    
    return data