# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:
RPG 50 is an interactive, text-based role-playing game (RPG) bot designed for Discord. It allows players to become immersed in a comprehensive fantasy world, wherein they can engage in battles, trade resources, upgrade equipment, and experience exhilarating adventures, either independently or with companions.

## Features

- The game features three distinct classes, each with unique attributes and capabilities, offering a diverse range of combat strategies.
- The game features over 20 unique adversaries, each with distinct capabilities, tactics, and challenges.
- The game features a cooperative battle system, which allows players to team up with friends to take down enemies together.
- The game offers the option of player versus player (PvP) combat, which allows players to engage in combat with one another.
- The game features Raid Battles, which allow players to engage in formidable combat against formidable adversaries.
- Players have the option of equipping their heroes with different gear, allowing them to tailor their abilities and strengths.
- The game employs a multi-hero system, which enables players to possess multiple heroes, each with distinctive abilities and equipment.
- It also incorporates an advancement system that enables players to progress through the game.
- Additionally, the game includes a dex tracker, which allows players to track their progress and the enemies they've encountered.
- Furthermore, the game encompasses five unique zones, each with distinct enemies and loot.


## Repository Overview
The project is structured into several directories, each handling a specific aspect of the game:
### project.py
This is the primary script that controls the bot. It is responsible for establishing the initial connection and loading all subsequent commands.
### cogs/commands
The bot commands are divided into seven directories, each of which contains commands related to a specific functional area. These directories are as follows: combat, equipment, help, heroes, resources, stats, and zones.
### cogs/game
This directory contains essential information regarding the functionalities of the game. It is divided into three main sections: characters, items, and zones.
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

## Design Choices and Challenges 
One of the biggest Challenges was learning how to use the discord library. And in functionalities, the combat system and coop modes where the hardest to implement and the ones with the most challenges. This is because discord bots are not intend to be use in this way at first, so there are not a lot of built-in functionalyties to manage this type od events.

The enmies disign was another tedious work, creating more than 20 enemies with its unique stats and habilities is easier said than done, after then tenth is harder and harder to came up with a good and unique idea.

## Acknowledgements
This project was made by Juan Novas [(Linkedin profile)](https://www.linkedin.com/in/juan-novas/) and Juan Marcos [(Linkedin profile)](https://www.linkedin.com/in/juan-ignacio-marcos-b20789276/)