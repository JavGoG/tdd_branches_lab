def latest(scores):
    return scores[-1]


def personal_best(scores):
    sorted_scores = sorted(scores)
    return sorted_scores[-1]


def personal_top_three(scores):
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[0:3]

def ordered_highest(scores):
    sorted_scores = sorted(scores, reverse=True)
    last_score = 100 #Highest possible score is 99
    for score in sorted_scores:
        if score < last_score:
            last_score = score
            pass
        else:
            return False
    return True