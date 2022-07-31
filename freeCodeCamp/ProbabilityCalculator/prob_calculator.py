import copy
import random

class Hat:
  def __init__(self, **balls):
    contents = []
    for color, count in balls.items():
      while count > 0:
        contents.append(str(color))
        count -= 1
    self.contents = contents

  def draw(self, count):
    balls = []
    for pull in range(0, min(len(self.contents), count)):
      ball = random.choice(self.contents)
      balls.append(ball)
      self.contents.pop(self.contents.index(ball))
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for experiment in range(0,num_experiments):
    true_count = 0
    hat_copy = copy.deepcopy(hat)
    balls = hat_copy.draw(num_balls_drawn)
    for color, count in expected_balls.items():
      if balls.count(color) >= count:
        true_count += 1
      else:
        break
    if true_count == len(expected_balls):
        success += 1                    
  return success / num_experiments
