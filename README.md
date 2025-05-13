# Simple Platformer

A lightweight 2D platformer game built with Pygame where players navigate through multiple levels, collecting rewards and gaining points.

## Features

- **Multiple Levels**: Progress through 4 unique levels with increasing difficulty
- **Player Movement**: Control a character with keyboard inputs for left/right movement and jumping
- **Platforming Mechanics**: Navigate platforms with realistic gravity and collision detection
- **Collectible Rewards**: Gather rewards to increase your score and progress to the next level
- **Score System**: Earn points for collecting rewards, with higher levels yielding more points
- **Save/Load System**: Save your progress and continue your game later
- **User Interface**: Clean and intuitive UI with menus, pause functionality, and level transitions

## Requirements

- Python 3.6 or higher
- Pygame library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simple-platformer.git
cd simple-platformer
```

2. Install dependencies:
```bash
pip install pygame
```

3. Run the game:
```bash
python simple_platformer.py
```

## How to Play

- **Arrow Keys**: Move left/right
- **Space Bar**: Jump
- **Escape**: Pause game
- **Mouse**: Click buttons in menus

## Game Structure

The game follows this basic structure:

1. **Main Menu**: Choose to start a new game, load a saved game, or exit
2. **Gameplay**: Navigate through platforms to collect rewards
3. **Level Completion**: After collecting all rewards in a level, proceed to the next
4. **Game Completion**: After completing all levels, view your final score

## Implementation Details

### Classes and Components

- **Button Class**: Handles UI button rendering and interaction
- **Level Design**: Procedurally defined platform layouts for each level
- **Collision Detection**: Handles interactions between player, platforms, and rewards
- **Save/Load System**: Uses Python's pickle module to persist game state

### Game Flow

1. The game starts with the `main()` function which displays the menu
2. Player can choose to start a new game or load a saved game
3. The `game_loop()` function handles the core gameplay
4. Each level is loaded with appropriate platforms, rewards, and player starting position
5. When all rewards are collected, the level is completed and the next one loads
6. After all levels are completed, the game shows a congratulations screen and returns to the menu

## Code Structure

- **Initialization**: Sets up Pygame, window, colors, and fonts
- **UI Components**: Defines the Button class for interactive UI elements
- **Save/Load Functions**: Handles game state persistence
- **Level Design**: Functions to generate level layouts
- **Game Loop**: Main game logic controlling player movement, collisions, and progression
- **Main Function**: Entry point that manages the game flow

## Future Enhancements

Potential improvements for future versions:

- Add sound effects and background music
- Implement enemies and obstacles
- Create a level editor
- Add more player abilities (double jump, dash, etc.)
- Implement high score tracking
- Add more visual effects and animations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Pygame](https://www.pygame.org/) library for making game development in Python accessible
- Inspiration from classic platformer games

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
