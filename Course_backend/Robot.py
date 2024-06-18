import math
from typing import Tuple
from matplotlib import patches


class EmptyRobot:
  
  def __init__(self) -> None:
    self.laser = Laser()
    # Robots position
    self.x:float = 2
    self.y:float =  8
    self.orientation:float = math.pi # degrees
    # Robots velocity
    self.linear_vel = 0
    self.angular_vel = 0

  def show(self,ax) -> None:
    self.draw_circle_with_radius(ax,(self.x,self.y),0.4,self.orientation)
  
  
  def draw_circle_with_radius(self,ax, center, radius, angle_degrees) -> None:
    self.circle = patches.Circle(center, radius, edgecolor='black', facecolor='gray')
    ax.add_patch(self.circle)

    # Calculate the end point of the radius line based on the angle

    x_end = center[0] + radius * math.sin(self.orientation)
    y_end = center[1] + radius * math.cos(self.orientation)
    
    # Draw the radius line
    ax.plot([center[0], x_end], [center[1], y_end], color='black')

  def run(self) -> Tuple[float,float]:
    return (0,1.5)

    
class Laser:
  
  def __init__(self) -> None:
    pass
  
  def get_scan(self) -> None:
    pass