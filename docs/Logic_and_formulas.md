# Logic and Formulas


## Hero experience needed

### Description
Experience needed to level up scale exponentialy after each level.

### Experience needed scale formula
$6.5 \times (1.5 ^ {\text{Hero Level}})$
![Exponencial formula graph](images/logic_and_formulas/xp_needed_chart.png)

### Explanation
Each level xp needed is 50% more than the level before, starting from 10xp in level 1.


## Hero stats scale

### Description
All hero stats scale exponencialy except the mana.

### Stats scale formula
- Health
- Attack
- Defense
- Magic
- Magic resistance

$Base Stat \times (1.15 ^ {\text{Hero Level}})$

![Exponencial formula graph](images/logic_and_formulas/stats_progresion_chart.png)

- Mana

$Base Stat \times 1$
![Linear formula graph](images/logic_and_formulas/mana_progresion_chart.png)

### Explanation
Exponential stats grow makes that the difference beetween level 45-50 bigger than 20-25, rewarding the increase of xp needed on each level and helping to balance low level difference (making it not really important) and high level difference (making it harder to fight higher level enemies).
Mana stays the same because habilities mana cost never increase.

