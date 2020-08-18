class Ship:
  def __init__(self, *body):
    self.life = {}
    for point in body:
      self.life[point] = 1

  def recieve_attack(self, point):
    if point in self.life and self.life[point] > 0:
      self.life[point] -= 1
      return True
    return False

  def is_alive(self):
    return sum(self.life.values()) > 0
  
  def is_attacked(self):
    # assume every point is life value 1
    return sum(self.life.values()) < len(self.life)
    
def mark_to_coordinate(mark):
  # coordinate system from (0,0)
  return int(mark[0]) - 1, ord(mark[1]) - 65
  
def points_in_area(left_top, bottom_right):
  x = bottom_right[0] - left_top[0]
  y = bottom_right[1] - left_top[1]
  for i in range(x+1):
    for j in range(y+1):
      yield (left_top[0] + i, left_top[1] + j)

def one_round(N, S, T):
    ship_marks = []
    for mark in S.split(','):
      if mark:
        ship_marks.append(mark)
    ship_areas = []
    for mark in ship_marks:
      ship_areas.append([mark_to_coordinate(m) for m in mark.split()])

    ships = []
    for ship_area in ship_areas:
      ship_body = points_in_area(ship_area[0], ship_area[1])
      ship = Ship(*ship_body)
      ships.append(ship)
    
    for attack in T.split():
      attack_point = mark_to_coordinate(attack)
      for ship in ships:
        if ship.recieve_attack(attack_point):
          break

    # evaluate result
    sunk = 0
    for ship in ships:
      if not ship.is_alive():
        sunk += 1
    attacked_but_alive = 0
    for ship in ships:
      if ship.is_alive() and ship.is_attacked():
        attacked_but_alive += 1

    return '{},{}'.format(sunk, attacked_but_alive)