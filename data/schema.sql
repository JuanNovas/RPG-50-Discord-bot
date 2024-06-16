DROP TABLE IF EXISTS hero;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS item_types;

CREATE TABLE hero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    class INTEGER NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    xp INTEGER NOT NULL DEFAULT 0,
    gold INTEGER NOT NULL DEFAULT 0,
    wood INTEGER NOT NULL DEFAULT 0,
    iron INTEGER NOT NULL DEFAULT 0,
    runes INTEGER NOT NULL DEFAULT 0,
    weapon_id INTEGER DEFAULT NULL,
    armor_id INTEGER DEFAULT NULL,
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


CREATE UNIQUE INDEX user_id_index ON hero(user_id);

-- Types
INSERT INTO item_types (type) VALUES ('weapon');
INSERT INTO item_types (type) VALUES ('armor');

-- Views
DROP VIEW IF EXISTS clean_inventory;

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