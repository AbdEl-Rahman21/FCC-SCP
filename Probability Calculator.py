import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for color, number_of_balls in kwargs.items():
            for _ in range(number_of_balls):
                self.contents.append(color)

    def draw(self, number_of_balls):
        drawn_balls = []

        if number_of_balls >= len(self.contents):
            drawn_balls = self.contents[:]

            self.contents.clear()
        else:
            for _ in range(number_of_balls):
                ball_to_draw = random.randrange(len(self.contents))

                drawn_balls.append(self.contents.pop(ball_to_draw))

        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    number_of_successes = 0

    for _ in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        drawn_balls = test_hat.draw(num_balls_drawn)

        if all(drawn_balls.count(color) >= number_of_balls for color, number_of_balls in expected_balls.items()):
            number_of_successes += 1

    return number_of_successes / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2,'green':1}, num_balls_drawn=5, num_experiments=2000)
