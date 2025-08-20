# Game Description

"Dust to Ash" is a turn-based roguelike game. Each run will start with the player choosing one of three characters, each with their own attacks, resistances, and weaknesses.

Combat is done in waves, with a Major Boss at the end of each wave. Like the player characters, each enemy has its own set of attacks, resistances, and weaknesses. Defeating the Major Boss will grant the player an item that persists between runs, regardless of the chosen character. Dying at any point resets the run; all items but ones earned by Major Bosses will be lost.

## Roadmap

### Phase 0: Skeleton COMPLETE

- Initialize folders and respective files

### Phase 1: MVP (1 char vs. 1 enemy + Major Boss)

**Goal**: end-to-end loop to validate roguelike structure

- Single playable character with 3 moves
- One enemy + 1 Major Boss
- **Stats**: HP, ATK, DEF, SPD.
- Fixed 2-wave run: enemy -> MB.
    - Defeating MB 'grants' item (no persistence)
- Generate seed for testing
- **Terminal-run only**; choose move by number, enemy picks move at random

**Win Conditions**: each run produces consistent outcomes given a seed

### Phase 2: Core Combat (Weakness/Resistance + Status Effects)

**Goal**: math and timing order, minimal work

#### Implementation

- Type tags (e.g., FIRE, POISON), tag characters and enemies
- Simple status effects (POISON: lower damage, attack, FIRE: post-turn damage, SHOCK: chance of turn being skipped)
- Turn order = SPD -> active entity picks action -> damage/effect -> status tick -> death check -> next entity
- Clear text combat log

**Win Conditions**: passing unit tests for damage, status stack effect (freeze rule in 'docs/design.md).
