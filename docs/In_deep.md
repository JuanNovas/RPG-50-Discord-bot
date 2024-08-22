# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:
RPG 50 is an interactive, text-based role-playing game (RPG) bot designed for Discord. It allows players to immerse themselves in a rich fantasy world where they can engage in battles ⚔️, trade resources 💰, upgrade equipment 🛠️, and experience exciting adventures, either solo or with friends.

## Project Overview 🌟
The project is structured into several directories, each handling a specific aspect of the game:

### project.py
The central script for the bot. It handles the conection and load of all the commands.

### cogs/commands
Contains all the bot commands, wich are dividid in 7 directories, combat, equipment, help, heroes, resources, stats and zones, depending on its functionalities.

### cogs/game
Contains important information for the functionalities of the game. This directory is divided in characters, items and zones.
#### Caracters
Contains hero and enemy scripts.
#### Items
Contains Equipment related scripts.
#### Zones
Contains Zones related scripts such as the encounter generator.

### cogs/tests
Contains a test command to test load function.

### cogs/utils
Contains important functions wich are used in varios scripts all over the project. Including, for example, the battle system, the database connection or the hero creation.

### Data
Contains the .SQL database inicialization script.

### Docs
Contains documentation of the project.

## Design Choices and Challenges 🛠️
