class BaseHero():
        
    def do_attack(self, enemy, power=10):
        damage =  ((self.attack / enemy.defense) / 10) * power
        enemy.hp -= damage
        return damage
    
    def is_alive(self):
        return self.hp > 0