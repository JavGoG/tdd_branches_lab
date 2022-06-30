def get_result(final_score):
    if final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    if final_score["home_score"]   > final_score["away_score"]:
        return "Home win"
    if final_score["home_score"] == final_score["away_score"]:
        return "Draw"

def get_results(final_scores):
    all_results = []

    for score in final_scores:
        all_results.append(get_result(score))

    return all_results