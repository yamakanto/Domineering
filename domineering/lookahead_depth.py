class ConstantLookaheadDepth:
    def __init__(self, depth):
        self.depth = depth

    def __call__(self, turn):
        return self.depth


class ProgressiveLookaheadDepth:
    def __init__(self, depths, thresholds):
        self.depths = depths
        self.thresholds = thresholds

    def __call__(self, turn):
        correct_thresh = max([t for t in self.thresholds if t <= turn])
        index = self.thresholds.index(correct_thresh)
        return self.depths[index]
