# Focus Game (Domination)  
**Abstract Board Game Implementation in Python**  

This repository contains the implementation of the abstract board game **Focus/Domination**. The game supports two players and features core functionalities, including making moves, capturing pieces, managing reserves, and determining the winner.  

---

## Table of Contents  

- [About the Game](#about-the-game)  
- [Features](#features)  
- [Classes](#classes)  
- [Usage](#usage)  
- [Author](#author)  

---

## About the Game  

**Focus/Domination** is a two-player abstract strategy game involving stacking and capturing pieces. Players take turns making moves on a 6x6 board, attempting to capture their opponent's pieces while managing their own reserves. The game ends when a player captures more than five opponent pieces.  

---

## Features  

- **Dynamic Gameplay**: Supports movement, capturing, and stacking of pieces.  
- **Turn-based Logic**: Ensures players take turns and only valid moves are executed.  
- **Reserve Management**: Allows players to place pieces from their reserve onto the board.  
- **Victory Condition**: Declares the winner when the capture criteria are met.  

---

## Classes  

### `FocusGame`  
Handles the main game logic, including the board setup, moves, and captures.  

#### **Initialization**  
Creates a board and initializes players.  

#### **Key Methods**  
- `move_piece(name, start, end, num_pieces)` - Moves pieces on the board.  
- `show_pieces(position)` - Displays pieces at a specific board position.  
- `show_captured(player)` - Shows the pieces a player has captured.  
- `show_reserve(player)` - Shows the pieces in a player's reserve.  
- `reserved_move(player, location)` - Places a piece from the reserve onto the board.  

---

### `Player`  
Manages player-specific information like name, color, and stashes.  

#### **Initialization**  
Stores player details and stashes.  

#### **Key Methods**  
- `get_player_name()` - Returns the player's name.  
- `get_color()` - Returns the player's color.  
- `reserve_stash_add(piece)` - Adds a piece to the player's reserve stash.  
- `captured_stash_add(piece)` - Adds a piece to the player's captured stash.  
- `win_check()` - Checks if the player has won.  

---

## Usage  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/your-username/focus-game.git  
   cd focus-game
2. **Run the script**:
    ```bash
    python focus_game.py
## Example Gameplay  

```python  
# Initialize a new game  
game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))  

# Player A moves a piece  
print(game.move_piece('PlayerA', (0, 0), (0, 1), 1))  # Output: "successfully moved"  

# Display pieces at a position  
print(game.show_pieces((0, 1)))  # Output: ['R', 'R']  

# Show captured pieces for Player A  
print(game.show_captured('PlayerA'))  # Output: 0  

# Attempt a reserve move for Player A  
print(game.reserved_move('PlayerA', (0, 0)))  # Output: "No pieces in reserve"  




