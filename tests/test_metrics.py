from metrics import precision, recall

def test_precision_quiz_answer_1():
    assert precision(tp=5, fp=0) == 1.0

def test_recall_quiz_answer_1():
    assert recall(tp=5, fn=5) == 0.5

def test_precision_stops_nobody():
    assert precision(tp=0, fp=0) == 0.0
