class Ship:
    def __init__(self, area):
        self.area = area  # tuple in (tl_x, tl_y, br_x, br_y)
        self.life = {}  # every ship grid has one life point
        self._create_life()

    def _create_life(self):
        # points_in_area
        area = self.area
        x = area[2] - area[0]
        y = area[3] - area[1]
        for i in range(x+1):
            for j in range(y+1):
                self.life[(area[0] + i, area[1] + j)] = 1

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
        area = (ship_area[0][0], ship_area[0][1],
                ship_area[1][0], ship_area[1][1])
        ship = Ship(area)
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