DROP TABLE IF EXISTS hero;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS item_types;
DROP TABLE IF EXISTS advancements;
DROP TABLE IF EXISTS enemies;
DROP TABLE IF EXISTS dex;

CREATE TABLE hero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    class INTEGER NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    xp INTEGER NOT NULL DEFAULT 0,
    gold INTEGER NOT NULL DEFAULT 0,
    wood INTEGER NOT NULL DEFAULT 0,
    iron INTEGER NOT NULL DEFAULT 0,
    runes INTEGER NOT NULL DEFAULT 0,
    weapon_id INTEGER DEFAULT NULL,
    armor_id INTEGER DEFAULT NULL,
    zone_id INTEGER NOT NULL DEFAULT 1,
    active INTEGER NOT NULL,
    FOREIGN KEY (weapon_id) REFERENCES inventory(id),
    FOREIGN KEY (armor_id) REFERENCES inventory(id)
);

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hero_id INTEGER NOT NULL,
    type INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (hero_id) REFERENCES hero(id),
    FOREIGN KEY (type) REFERENCES item_types(id)
);

CREATE TABLE item_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL
);

CREATE TABLE advancements (
    hero_id INTEGER NOT NULL,
    kills INTEGER NOT NULL DEFAULT 0,
    upgrades INTEGER NOT NULL DEFAULT 0,
    gold_spent INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (hero_id) REFERENCES hero(id)
);

CREATE TABLE enemies (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    zone INTEGER NOT NULL
);

CREATE TABLE dex (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hero_id INTEGER NOT NULL,
    enemy_id INTEGER NOT NULL,
    FOREIGN KEY (hero_id) REFERENCES hero(id),
    FOREIGN KEY (enemy_id) REFERENCES enemies(id)
);


CREATE INDEX user_id_index ON hero(user_id);

-- Types INSERT
INSERT INTO item_types (type) VALUES ('weapon');
INSERT INTO item_types (type) VALUES ('armor');
-- Enemies INSERT
INSERT INTO enemies (id, name, zone) VALUES (1, 'Dummy', 0);
INSERT INTO enemies (id, name, zone) VALUES (2, 'Slime', 2);
INSERT INTO enemies (id, name, zone) VALUES (3, 'Lava Dragon', 2);
INSERT INTO enemies (id, name, zone) VALUES (4, 'Skeleton', 2);
INSERT INTO enemies (id, name, zone) VALUES (5, 'Goblin', 1);
INSERT INTO enemies (id, name, zone) VALUES (6, 'Crow', 1);
INSERT INTO enemies (id, name, zone) VALUES (7, 'Worm', 1);
INSERT INTO enemies (id, name, zone) VALUES (8, 'Shadow', 2);
INSERT INTO enemies (id, name, zone) VALUES (9, 'Rat', 2);
INSERT INTO enemies (id, name, zone) VALUES (10, 'Wolf', 3);
INSERT INTO enemies (id, name, zone) VALUES (11, 'Giant Goblin', 3);
INSERT INTO enemies (id, name, zone) VALUES (12, 'Bear', 3);
INSERT INTO enemies (id, name, zone) VALUES (13, 'Snake', 3);
INSERT INTO enemies (id, name, zone) VALUES (14, 'Mummy', 4);
INSERT INTO enemies (id, name, zone) VALUES (15, 'Scorpion', 4);
INSERT INTO enemies (id, name, zone) VALUES (16, 'Golem', 4);
INSERT INTO enemies (id, name, zone) VALUES (17, 'Scavengers', 4);
INSERT INTO enemies (id, name, zone) VALUES (18, 'Giant Frog', 5);
INSERT INTO enemies (id, name, zone) VALUES (19, 'King Hawk', 1);
INSERT INTO enemies (id, name, zone) VALUES (20, 'Mutant', 5);
INSERT INTO enemies (id, name, zone) VALUES (21, 'Forest Guardian', 3);
INSERT INTO enemies (id, name, zone) VALUES (22, 'God of Sand', 4);
INSERT INTO enemies (id, name, zone) VALUES (23, 'Mud Soldiers', 5);
INSERT INTO enemies (id, name, zone) VALUES (24, 'Witch', 5);


-- Triggers
CREATE TRIGGER create_advancements_entry AFTER INSERT ON hero
FOR EACH ROW
BEGIN
    INSERT INTO advancements (hero_id) VALUES (NEW.id);
END;

-- Views
DROP VIEW IF EXISTS clean_inventory;
DROP VIEW IF EXISTS clean_hero;


CREATE VIEW clean_inventory AS
SELECT 
    inventory.hero_id,
    hero.user_id,
    item_types.type,
    inventory.item_id,
    inventory.level
FROM 
    inventory
JOIN 
    hero ON inventory.hero_id = hero.id
JOIN 
    item_types ON inventory.type = item_types.id;


CREATE VIEW clean_hero AS
SELECT
    hero.id,
    hero.user_id,
    hero.active,
    hero.class,
    hero.level,
    hero.xp,
    hero.gold,
    hero.wood,
    hero.iron,
    hero.runes,
    hero.weapon_id,
    weapon_inventory.level AS weapon_level,
    hero.armor_id,
    armor_inventory.level AS armor_level
FROM
    hero
LEFT JOIN inventory AS weapon_inventory ON hero.weapon_id = weapon_inventory.id
LEFT JOIN inventory AS armor_inventory ON hero.armor_id = armor_inventory.id;