import copy
import random
class Hat:
  def __init__(self,**balls):
    self.contents=[]
    for color, count in balls.items():
      self.contents.extend([color] * count)

  def draw(self,n_balls_to_draw):
    if n_balls_to_draw >= len(self.contents):
      drawn_balls = self.contents.copy()
      self.contents=[]
    else:
      drawn_balls=random.sample(self.contents, n_balls_to_draw)
      for ball in drawn_balls:
        self.contents.remove(ball)
    return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_successful_experiments=0
  
  for i in range(num_experiments):
    # Create a copy of the hat for each experiment
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    
    success = True
    
    for color, count in expected_balls.items():
      if drawn_balls.count(color) < count:
        success=False
        break
        
    if success:
      num_successful_experiments += 1
      
        
  probability = num_successful_experiments / num_experiments
  return probability

  
    
