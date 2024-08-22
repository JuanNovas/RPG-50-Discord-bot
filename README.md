# RPG 50 🎮🛡️
An interactive role-playing game for Discord where players can battle enemies ⚔️, trade resources 💰, upgrade equipment 🛠️, and much more. Experience a turn-based, single-player or cooperative adventure through interactive commands. This bot was developed as the final project for Harvard's CS50 Python course. 🎓


## Features ✨

- **Three Unique Classes:** 🛡️⚔️ Each class comes with special attacks and stats, allowing for diverse combat strategies.
- **Over 20 Unique Enemies:** 👹🐉 Face a wide variety of enemies, each with their own abilities, styles and challenges.
- **Cooperative Battle System:** 🤜🤛 Team up with friends to take down enemies together.
- **PvP Support:** 🗡️🔥 Challenge other players in player-versus-player combat.
- **Raid Battles:** ⚡🐲 Participate in epic raids against powerful enemies.
- **Customizable Builds:** 🛠️⚙️ Equip your heroes with different gear to tailor their abilities and strengths.
- **Multi-Hero System:** 🦸‍♂️🦸‍♀️ Control multiple heroes, each with their own unique skills and equipment.
- **Advancement System:** 📈🌟 Progress through the game with a comprehensive advancement system.
- **Dex Tracker:** 📖 Track your progress and the enemies you’ve encountered with the Dex tracker.
- **Five Unique Zones:** 🌍🌌 Explore five different zones, each with distinct enemies and loot.


## Documentation
- [Commands](docs/Commands.md)
- [Logic and Formulas](docs/Logic_and_formulas.md)
- [Database](docs/Database.md)
- [In deep](docs/In_deep.md)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/JuanNovas/Final-project.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Final-project
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

   - On Windows:
       ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
       ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
   ```

6. Create a Discord bot and get the token:
   1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   2. Click on "New Application" and give it a name.
   3. Under the "Bot" tab, click "Add Bot" and confirm.
   4. Copy the bot token from the "TOKEN" section and save it for later.

7. Invite the bot to your server:
   1. Go to the "OAuth2" tab in the Discord Developer Portal.
   2. Under "OAuth2 URL Generator," select "bot" in the scopes section.
   3. Under "Bot Permissions," select the permissions your bot needs (e.g., "Administrator").
   4. Copy the generated URL and open it in your browser to invite the bot to your server.

8. Configure the `.env` file with the necessary variables:

   Create a `.env` file in the root directory of the project with the following content:
    ```bash
    DISCORD_TOKEN=your_discord_bot_token
    ```

   Replace `your_discord_bot_token` with your actual Token.

9. Run the bot:
    ```bash
   python bot.py
    ```

