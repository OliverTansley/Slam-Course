import math
from typing import Tuple
from matplotlib import patches

class Robot:
  
  def __init__(self) -> None:
    self.laser = Laser()
    self.x:float = 2
    self.y:float =  2
    self.orientation:float = 0 # degrees
    

  def show(self,ax):
    self.draw_circle_with_radius(ax,(self.x,self.y),0.4,self.orientation)
  
  
  def draw_circle_with_radius(self,ax, center, radius, angle_degrees):
    self.circle = patches.Circle(center, radius, edgecolor='black', facecolor='gray')
    ax.add_patch(self.circle)

    # Calculate the end point of the radius line based on the angle
    angle_radians = math.pi * angle_degrees/180 
    x_end = center[0] + radius * math.sin(angle_radians)
    y_end = center[1] + radius * math.cos(angle_radians)
    
    # Draw the radius line
    ax.plot([center[0], x_end], [center[1], y_end], color='black')

  def run(self) -> Tuple[float,float]:
    return (1,1)

    
class Laser:
  
  def __init__(self) -> None:
    pass
  
  def get_scan(self) -> None:
    pass