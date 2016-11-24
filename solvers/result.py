class Result(object):
    def __init__(self, source, actions, remainingInputs, remainingTargets):
        self.source = source
        self.actions = actions
        self.remainingInputs = remainingInputs
        self.remainingTargets = remainingTargets

    def solved(self):
        return not (self.remainingTargets or self.remainingInputs)

    def score(self):
        if len(self.remainingTargets) > 3:
            return 0
        else:
            # Fewer targets is better than more targets (1 action means 1 target):
            targetScore = 10*(len(self.actions))
            # Fewer high targets is better than fewer low targets:
            targetScore -= sum(self.remainingTargets)
            # Prioritize fewer leftover inputs:
            inputScore = (10-len(self.remainingInputs))
            return targetScore + inputScore

    def __str__(self):
        return "Solved ({}):\nLeftover inputs: {}\nLeftover targets: {}\nActions:\n  {}\n\n".format(
            self.source,
            ", ".join(str(i) for i in sorted(self.remainingInputs)),
            ", ".join(str(i) for i in sorted(self.remainingTargets)),
            "\n  ".join(self.actions))
