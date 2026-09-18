# Trips

## Jeopardy Party Game

`jeopardy.html` is a self-contained Jeopardy-style party game (no external files, no internet needed).
Open it in Safari on an iPad in landscape and mirror to a TV.

- 5 categories x 5 values (200 - 1000) with 25 pre-loaded questions
- Two teams (default "Girls" and "Guys", editable on the setup screen), alternating turns, tap a scorecard to switch manually
- Tap a tile: 30-second countdown ring (red under 10s, buzzer at 0), Reveal Answer, then award either team, Redemption (15s steal), or "Nobody got it"
- Game state is saved in localStorage so a refresh doesn't lose the game; "New Game" resets
- Winner screen with confetti when all 25 tiles are played
