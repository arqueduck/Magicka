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
