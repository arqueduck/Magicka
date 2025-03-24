# 🎮 Magicka

**Magicka** is a 2D action game developed as a college project to explore the capabilities of the [Pygame](https://www.pygame.org/) library. The game was built to test concepts such as sprite animation, collision detection, game states (pause, game over, score), audio handling, and basic integration with a SQLite database for high score tracking.

---

## 🧪 About the Project

This project was developed for educational purposes as part of a college course, focusing on:

- Mastering the Pygame framework
- Structuring game loops and logic
- Handling input, rendering, music, and UI
- Implementing pause menus and countdown timers
- Saving and retrieving high scores using SQLite
- Building and distributing the game as a standalone `.exe`

---

## 🕹️ How to Play

- **Arrow keys or WASD** — Move the character  
- **Spacebar** — Attack  
- **ESC** — Pause the game  
- While paused:  
  - **ESC** to resume  
  - **Space** to quit to the main menu

---

## 📦 Features

- Fully animated player and enemy sprites
- Responsive movement and attack logic
- Pause menu with translucent overlay
- Game over screen with score display
- Score system based on survived and defeated enemies
- Time-limited gameplay (20 seconds)
- SQLite integration for saving and viewing high scores
- Clean main menu with navigation support

---

## 💾 Requirements (Dev)

To run the project from source:

```bash
pip install pygame
Python 3.10+ is recommended. The game uses only Pygame and SQLite3, no extra dependencies required.

---

## 🛠️ Build & Distribution
This game was successfully compiled into a standalone .exe using:

pyinstaller --noconfirm --windowed main.py --add-data "assets;assets"

Assets are stored in a folder named assets located beside the .exe for portability.

---

## 📁 Project Structure
Magicka/
├── assets/                # Game images, music and sprites
├── code/                  # All game logic (player, enemy, menu, level...)
├── main.py                # Entry point
├── README.md              # This file

---

## 🎨 Assets & Credits
All assets used in this project are available under free or permissive licenses for non-commercial use. Full credit to the original creators:

### 🔊 Sound & Music
"Cinematic Menu Loop" by Gregor Quendel
freesound.org link

"Arcade Punch FX" by Ilariio
freesound.org link

### 🧙‍♂️ Sprites & Visuals
Bat Sprite Pack by Elthen

Hero Knight sprite by Sventhole

Fantasy Battleground Backgrounds by Free Game Assets

These assets were used solely for educational and demonstrative purposes.

---

## 🎓 License
This project was developed strictly for learning purposes and is not intended for commercial distribution. All third-party assets are used under their respective licenses for non-commercial or educational use only.

---

🙌 Credits
Developed by Arqueduck
Game powered by Pygame
