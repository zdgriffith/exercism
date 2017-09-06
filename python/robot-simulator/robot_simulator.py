NORTH = 'NORTH'
EAST  = 'EAST'
SOUTH = 'SOUTH'
WEST  = 'WEST'

class Robot(object):
    def __init__(self, *args):
        self.directions  = [NORTH,EAST,SOUTH,WEST]

        if len(args) == 0:
            self.bearing     = NORTH
            self.coordinates = (0,0)
        elif len(args) == 3:
            if type(args[0]) != str or type(args[1]) != int or type(args[2]) != int:
                raise TypeError("Accepted argument types are (str,int,int)")
            else:
                if args[0] not in [NORTH,SOUTH,EAST,WEST]:
                    raise ValueError('Valid bearings are [NORTH,SOUTH,EAST,WEST]')
                else:
                    self.bearing     = args[0]
                    self.coordinates = (args[1],args[2])
        else:
            raise ValueError("Must initialize with 0 (default settings) or 3 (bearing, N-S position, E-W position) arguments")
        return

    def turn_right(self):
        new_index    = self.directions.index(self.bearing)+1
        if new_index == 4:
            new_index = 0
           
        self.bearing =  self.directions[new_index]
        return

    def turn_left(self):
        new_index    = self.directions.index(self.bearing)-1
        if new_index == -1:
            new_index = 3
           
        self.bearing =  self.directions[new_index]

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1]+1) 
        if self.bearing == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1]-1) 
        if self.bearing == EAST:
            self.coordinates = (self.coordinates[0]+1, self.coordinates[1]) 
        if self.bearing == WEST:
            self.coordinates = (self.coordinates[0]-1, self.coordinates[1]) 
        return

    def simulate(self, order):
        for move in order:
            if move == 'L':
                self.turn_left()
            elif move == 'R':
                self.turn_right()
            elif move == 'A':
                self.advance()
            else:
                raise ValueError("This is not a valid order! Character Options:  L(eft),R(ight),A(dvance)")
        return
