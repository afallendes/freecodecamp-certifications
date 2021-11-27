from collections import Counter
import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents += [ color for _ in range(quantity) ]
    
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        choices = []
        for _ in range(num_balls):
            choices.append(
                self.contents.pop(
                    # Recalculate len for indexes
                    random.randrange(len(self.contents))
                )
            )
        return choices


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_occurrences = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn_balls = Counter(new_hat.draw(num_balls_drawn))

        # Is a match if expected ball if drawn at least once
        matches = 0
        for c, q in expected_balls.items():
            if drawn_balls.get(c, 0) >= q:
                matches += 1
        
        if  matches == len(expected_balls):
            num_occurrences += 1
    return num_occurrences / num_experiments