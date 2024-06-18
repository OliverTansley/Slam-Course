
import math
from random import random
from typing import List, Tuple
from Course_backend.Robot import EmptyRobot
from Course_backend.obstacles import Wall,base_map
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


global DELTA_TIME
DELTA_TIME = 100


def simulate_robot(robot:EmptyRobot,robot_map:List[Wall] = base_map,total_time = 15, noise_strength = 0.1) -> FuncAnimation:
  
  robot.x,robot.y = 2,8
  
  fig, ax = plt.subplots(figsize=(4, 4),dpi=100)
  plt.close()
  
  def update_sim(frame) -> None:

    # Display environment
    ax.cla()
    for wall in robot_map:
      wall.show(ax)
    robot.show(ax)
    
    # Update environment
    wheel_speeds: Tuple[float, float] = robot.run()
    left_wheel_change = wheel_speeds[0] * DELTA_TIME/1000 
    right_wheel_change = wheel_speeds[1] * DELTA_TIME/1000 
    
    average_change = (left_wheel_change + right_wheel_change)/2
    bearing_change = (right_wheel_change - left_wheel_change)/0.4
    
    robot.orientation += 360 * bearing_change/2*math.pi # robot orientation is stored in degrees
    
    if bearing_change != 0:
      R = average_change/bearing_change
      delta_x = R * (math.cos(2*math.pi*robot.orientation/360) - math.cos(2*math.pi*robot.orientation/360 - 360 * bearing_change/2*math.pi)) + random()/10 * noise_strength
      delta_y = -R * (math.sin(2*math.pi*robot.orientation/360) - math.sin(2*math.pi*robot.orientation/360 - 360 * bearing_change/2*math.pi)) + random()/10 * noise_strength
    else:
      delta_x = average_change*math.cos(2*math.pi*robot.orientation/360 - 360 * bearing_change/2*math.pi) + random()/10 * noise_strength
      delta_y = average_change*math.sin(2*math.pi*robot.orientation/360 - 360 * bearing_change/2*math.pi) + random()/10 * noise_strength
    
    robot.x += delta_x
    robot.y += delta_y
    
    ax.set_title(f"Time: {frame*DELTA_TIME/1000:05.2f} seconds")
     
     
  sim_animation = FuncAnimation(fig=fig,func=update_sim, frames=int(total_time * int(1000/DELTA_TIME)),interval=int(DELTA_TIME))
  return sim_animation
  