from src.enemy import Enemy

class Level:
    def __init__(self):
        self.level = level
        self.qtd_monster = 0
        self.enemy = Enemy(self.qtd_monster, self.level)

    def execute(self):
        self.monster.run()