class Players:
    Scores = {"X": 1, "O": -1, "tie": 0}

    def __init__(self, mark="X", scores=Scores):
        self.mark = mark
        self.scores = scores

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark
