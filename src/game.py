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
    
def _mark_to_coordinate(mark):
  # coordinate system from (0,0)
  return int(mark[0]) - 1, ord(mark[1]) - 65
  
def _points_in_area(left_top, bottom_right):
  x = bottom_right[0] - left_top[0]
  y = bottom_right[1] - left_top[1]
  for i in range(x+1):
    for j in range(y+1):
      yield (left_top[0] + i, left_top[1] + j)

def create_ships(S):
  ship_marks = []
  for mark in S.split(','):
    if mark:
      ship_marks.append(mark)
  ship_areas = []
  for mark in ship_marks:
    ship_areas.append([_mark_to_coordinate(m) for m in mark.split()])

  ships = []
  for ship_area in ship_areas:
    ship_body = _points_in_area(ship_area[0], ship_area[1])
    ship = Ship(*ship_body)
    ships.append(ship)
  return ships

def create_attacks(T):
  attacks = []
  for attack in T.split():
      attacks.append(_mark_to_coordinate(attack))
  return attacks

def eval_game(ships, attacks):
  for a in attacks:
      for ship in ships:
        if ship.recieve_attack(a):
          break
  
  sunk = damaged = undamaged = 0
  for ship in ships:
    if ship.is_alive():
      if ship.is_attacked():
        damaged += 1
      else:
        undamaged += 1
    else:
      sunk += 1
  return {'sunk': sunk, 'alive': damaged, 'intact': undamaged}

def go_round(N, S, T):
    ships = create_ships(S)
    attacks = create_attacks(T)

    sunk = 0
    for ship in ships:
      if not ship.is_alive():
        sunk += 1

    result = eval_game(ships, attacks)

    return '{},{}'.format(result['sunk'], result['alive'])