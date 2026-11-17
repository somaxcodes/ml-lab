def precision(tp, fp):
    if tp + fp == 0:
        return 0.0
    return tp / (tp + fp)

def recall(tp, fn):
    if tp + fn == 0:
        return 0.0
    return tp / (tp + fn)

# Your two quiz answers, as code
print(precision(tp=5, fp=0), recall(tp=5, fn=5))      # question 1
print(precision(tp=10, fp=990), recall(tp=10, fn=0))  # question 2
