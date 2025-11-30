# Copilot Instructions - Blackjack Game

## Project Overview
This is a beginner-level terminal-based Blackjack game built with Python for a CS 101 portfolio project. The codebase is in early development with foundational card and deck mechanics in place.

## Architecture & Key Components

### Current Structure
- **`black_jack.py`**: Main game file containing two classes:
  - `Cards`: Represents individual playing cards with suits and ranks
  - `Deck`: Manages a standard 52-card deck with shuffle and deal operations

### Design Patterns
The codebase uses a **class-based OOP approach** for representing game entities. Each class has a single responsibility:
- `Cards` encapsulates card data (suit/rank) without game logic
- `Deck` handles card collection operations (initialization, shuffling, dealing)

### Data Flow
1. `Deck` initialization creates all 52 cards by combining suits × ranks
2. Cards are shuffled in-place using `random.shuffle()`
3. Cards are dealt by popping from the cards list (removes from deck)

## Development Conventions

### Code Style
- Use clear, descriptive class names (e.g., `Cards`, `Deck`)
- Class attributes (e.g., `suits`, `ranks`) define game constants
- Import statements can appear inside methods when used conditionally (see `shuffle()`)

### Extending the Game
When adding new features, maintain this structure:
1. **Game Logic**: Create a `Game` or `Player` class to manage game state
2. **Card Valuation**: Add a method to `Cards` class to return card value (needed for blackjack hand calculations)
3. **Game Flow**: Orchestrate in a separate game loop function

### Next Logical Steps
Based on the incomplete feature list in README, expected additions include:
- Player hand management (list of Cards)
- Card value calculations (handle Ace flexibility: 1 or 11)
- Dealer logic and game rules enforcement
- Win/loss determination
- User input and game loop

## Critical Implementation Notes

### Card Values for Blackjack
When implementing scoring, remember:
- Number cards (2-10): Face value
- Face cards (Jack, Queen, King): 10 points
- Ace: 1 or 11 points (special handling required for hand totals)

### Deck Management
- Current `deal_card()` returns `None` when deck is empty—handle this gracefully
- Consider implementing deck reshuffle threshold for longer gameplay

## File Organization
```
black_jack.py          # All game logic (classes and game loop)
.github/               # AI agent and project guidance
README.md             # Project overview
.gitignore            # Git configuration
```

## Testing Approach
For a CS 101 portfolio project, focus on:
- Manual testing in terminal: create a `Deck`, verify shuffle works, deal cards
- Verify card counts (should be 52 initially)
- Test edge cases: empty deck, edge card values

## Running the Game
Currently, the game lacks a main entry point. When implementing the game loop:
```bash
python black_jack.py
```

Provide interactive prompts for player actions and display hand/dealer information.
