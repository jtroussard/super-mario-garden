class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement execute()")

class MoveLeftCommand(Command):
    def __init__(self, player):
        self.player = player
    
    def execute(self):
        self.player.move_left()

class MoveRightCommand(Command):
    def __init__(self, player):
        self.player = player
    
    def execute(self):
        self.player.move_right()

class FireCommand(Command):
    def __init__(self, player):
        self.player = player
    
    def execute(self):
        if not self.player.is_paused:
            self.player.fire()
