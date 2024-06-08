
from typing import List
from Course_backend.Robot import Robot
from Course_backend.obstacles import Wall,base_map
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


global DELTA_TIME
DELTA_TIME = 100

def simulate_robot(robot:Robot = Robot(),robot_map:List[Wall] = base_map,total_time = 15):
  
  robot.x,robot.y = 2,2
  
  fig, ax = plt.subplots(figsize=(4, 4),dpi=100)
  plt.close()
  
  def update_sim(frame) -> None:

    # Display environment
    ax.cla()
    for wall in robot_map:
      wall.show(ax)
    
    robot.show(ax)
    # Update environment
    robot.x += 0.01
    
    ax.set_title(f"Time: {frame*DELTA_TIME/1000:05.2f} seconds")
     
     
  sim_animation = FuncAnimation(fig=fig,func=update_sim, frames=int(total_time * int(1000/DELTA_TIME)),interval=int(DELTA_TIME))
  return sim_animation
  
if __name__ == "__main__":
  simulate_robot(total_time=5)