class Wall:
  
  def __init__(self,strt,end) -> None:
    self.start = strt
    self.end = end
    
  def colliding(self,other_pos) -> bool:
    return other_pos[0] > min(self.start[0],self.end[0]) and other_pos[0] < max(self.start[0],self.end[0]) and other_pos[1] > min(self.start[1],self.end[1]) and other_pos[1] < max(self.start[1],self.end[1])
  
  def show(self,ax) -> None:
    ax.plot([self.start[0],self.end[0]],[self.start[1],self.end[1]],color='black',linewidth=4)
    
base_map: list[Wall] = [Wall((0,0),(0,10)),Wall((0,10),(10,10)),Wall((10,10),(10,0)),Wall((10,0),(0,0)),Wall((3.33,10),(3.33,5)),Wall((6.66,5),(6.66,0))]