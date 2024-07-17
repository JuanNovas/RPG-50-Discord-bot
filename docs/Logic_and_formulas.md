# Logic and Formulas


## Hero experience needed
Experience needed to level up scale exponentialy after each level. (50 is the max level)

### Experience needed scale formula
$$6.5 \times (1.5 ^ {\text{Hero Level}})$$

![Exponencial formula graph](images/logic_and_formulas/xp_needed_chart.png)

### Explanation
Each level xp needed is 50% more than the level before, starting from 10xp in level 1.


## Hero stats scale
All hero stats scale exponencialy except the mana.

### Stats scale formula
- Health
- Attack
- Defense
- Magic
- Magic resistance

$$Base Stat \times (1.15 ^ {\text{Hero Level}})$$

![Exponencial formula graph](images/logic_and_formulas/stats_progresion_chart.png)

- Mana

$$Base Stat \times 1$$

![Linear formula graph](images/logic_and_formulas/mana_progresion_chart.png)

#### Arguments
- **BaseStat**: Depends on each class.
- **Hero Level**: Current level of the hero.

### Explanation
Exponential stats grow makes that the difference beetween level 45-50 bigger than 20-25, rewarding the increase of xp needed on each level and helping to balance low level difference (making it not really important) and high level difference (making it harder to fight higher level enemies).
Mana stays the same because habilities mana cost never increase.


## Damage calculation
Formula used when realising attacks(E.g.: "Hit").

### Damage calculation formula
$$
\left( \frac{Hero \ Attack^{1.5} \times Power}{Hero \ Attack + Enemy \ Defense + 10} \right) \times R \times C
$$

![Linear formula graph](images/logic_and_formulas/damage_increase_chart.png)

#### Arguments
- **Hero Attack**: Attack/Magic stat from the owner of the attack.
- **Enemy Degense**: Defense/Magic resistance of the target of the attack.
- **Power**: Power of the attack, default is 10, some weapon attacks change it.
- **R**: Range beetween 0.8 and 1. Makes each attack random and inconsistance to resamble rpg random fight type.
- **C**: Crit chance (1/20) to double the damage (Magic attacks do not have crit chance).

### Explanation
Making the damage scale exponential at equal damage and defense compensates Healt exponential grow.


## Equipment stats calculation
The way in which the statistics are calculated together with the equipments.

### How its calculated
First the stats base in the level, then the weapon stats and last the armor stats.

$$
\text{Normal Stat} \quad \rightarrow \quad \text{Weapon stats} \quad \rightarrow \quad \text{Armor stats}
$$

Equipment boost are plain and multi. First the plain ones are added and then the multi ones.

$$
\text{Weapon plain boost} \quad \rightarrow \quad \text{Weapon multi boost} \quad \rightarrow \quad \text{Armor plain boost } \quad \rightarrow \quad \text{Armor multi boost}
$$ 

The next operations are done with each stat with each equipment.

$$
NewHeroStat = HeroStat + EquipmentPlainBoost
$$

$$
NewHeroStat = HeroStat * EquipmentMultiBoost
$$

### Explanation
After the boost from the weapon the stat boosted will be used with the armor, so exponential boosts are more efective in armors. This is to balance the fact that weapons had a custom attack.


## Equipment stats scale
The way equipment stats are calculated, there is no diference in how the plain and multi boosts scale.

### Max level
Equipments are divided in 5 ranks (1 to 5 stars). Max level is calculated with this formula:

$$
MaxLevel = Rank \times 10
$$

### Stats formula
The stats are calculated with this exponential formula:

$$
Boost \times {1.2} ^ {(level - 1)}
$$

![Exponencial formula graph](images/logic_and_formulas/equipment_scale_chart.png)

### Explanation
**Level - 1** makes it that when the equipment is level 1 the boost multiplies itself by 1, so the final stats are the base stats.


## Enemy experience drop scale
Experience gained from defeating enemies scale.

### experience scale
$$
BaseXP \times 1.07 ^ {EnemyLevel}
$$

![Exponencial formula graph](images/logic_and_formulas/enemy_xp_scale_chart.png)


### Explanation
This exponential grow makes it more rewarfing to fight higher level enemies, but it grows slower than the xp needed to level up. Making it that, more monsters are needed to be beaten to level up each time.