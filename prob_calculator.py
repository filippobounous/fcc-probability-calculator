import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, number in balls.items():
            for _ in range(number):
                self.contents.append(color)

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls_drawn)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if balls_drawn.count(color) < count:
                success = False
                break
        if success:
            success_count += 1
    return success_count / num_experiments