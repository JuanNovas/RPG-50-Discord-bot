import random

class BaseHero():
        
    def do_attack(self, enemy, power=10):
        CRIT_CHANCE = 0.05
        
        damage =  (((self.attack / enemy.defense) / 10) * power) * random.uniform(0.8, 1)
        if random.random() >= CRIT_CHANCE:
            damage *= 2
        enemy.hp -= damage
        return damage
    
    def is_alive(self):
        return self.hp > 0