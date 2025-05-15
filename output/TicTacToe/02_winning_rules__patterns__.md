# Chapter 2: Winning Rules (Patterns)

Welcome back! In [Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md), we learned about the individual spots on our Tic Tac Toe board and how we can click on them to place 'X' or 'O'. We now know how to get marks onto the board.

But simply placing marks isn't enough to play the game! How does the game know when someone has actually *won*?

Think about playing Tic Tac Toe on paper. You win by getting three of your marks in a row, column, or diagonally. The game needs a way to know exactly *which* combinations of squares count as a win. This is where the concept of "Winning Rules" or "Patterns" comes in.

## What are Winning Rules (Patterns)?

A "Winning Pattern" is simply a list of three specific squares on the board that, if all contain the same player's mark ('X' or 'O'), mean that player has won.

In Tic Tac Toe, there are always the same ways to win:
*   The top row
*   The middle row
*   The bottom row
*   The left column
*   The middle column
*   The right column
*   The top-left to bottom-right diagonal
*   The top-right to bottom-left diagonal

That's a total of 8 different ways to win!

The game needs to know all of these 8 combinations so it can check after every move whether a player has completed one of them.

## Representing Winning Patterns in Our Code

Remember in [Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md) we talked about the 9 boxes? We can think of them as being numbered from 0 to 8:

```
  0 | 1 | 2
 ---|---|---
  3 | 4 | 5
 ---|---|---
  6 | 7 | 8
```

Using these numbers, we can describe each winning line:

*   The top row is squares 0, 1, and 2.
*   The middle column is squares 1, 4, and 7.
*   One of the diagonals is squares 0, 4, and 8.

In our code, we store all these winning combinations in a list. We use an array of arrays (a list of lists) where each inner list contains the numbers of the three squares that form a winning line.

Look at this part of our `app.js` file:

```javascript
const winPatterns = [
  [0, 1, 2], // Top Row
  [0, 4, 8], // Diagonal (top-left to bottom-right)
  [0, 3, 6], // Left Column
  [1, 4, 7], // Middle Column
  [2, 5, 8], // Right Column
  [2, 4, 6], // Diagonal (top-right to bottom-left)
  [3, 4, 5], // Middle Row
  [6, 7, 8], // Bottom Row
];
```

This `winPatterns` list is our "rulebook" for winning. Each small list inside it (like `[0, 1, 2]`) is one specific way to win the game.

*   `[0, 1, 2]` means if squares number 0, 1, and 2 all have the same mark ('X' or 'O') and are not empty, someone wins.
*   `[0, 4, 8]` means if squares number 0, 4, and 8 all have the same mark and are not empty, someone wins.
*   And so on for all 8 combinations.

This list is like giving the computer a map of all the possible winning lines on the board, using the numbers 0 through 8 to point to the specific squares.

## How Are These Patterns Used?

Okay, so we have this list of winning rules (`winPatterns`). What does the game do with it?

The main job of this list is for checking if someone has won *after* a move is made.

Here's the high-level idea:

1.  A player clicks on a square and places their mark ('X' or 'O'). (We learned about this in [Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md)).
2.  The game then needs to ask, "Did that last move create a winning line?"
3.  To answer this, the game looks at our `winPatterns` list.
4.  It goes through *each* pattern in the list (like checking the top row, then the middle row, etc.).
5.  For the current pattern it's checking (e.g., `[0, 1, 2]`), it looks at the actual squares on the board that correspond to those numbers (square 0, square 1, and square 2).
6.  It checks if those three squares are all filled (not empty) AND if they all have the *same* mark ('X' or 'O').
7.  If it finds *any* pattern where the squares meet these conditions, it knows there's a winner! If it checks all 8 patterns and none meet the condition, the game continues.

We'll dive into the code that actually performs this check in a later chapter ([Chapter 5: Winner Checker](05_winner_checker_.md)). For now, just understand that `winPatterns` is the *data* the game uses to know *what* constitutes a winning line.

## Where Does This List Live in the Code?

As we saw, the `winPatterns` list is defined right at the beginning of our `app.js` file:

```javascript
// ... other code ...

const winPatterns = [
  [0, 1, 2], // Top Row
  [0, 4, 8], // Diagonal (top-left to bottom-right)
  // ... other patterns ...
];

// ... rest of the code ...
```

It's declared using `const`, which means this list of winning patterns will not change throughout the game. It's a fixed rulebook!

This list needs to be available whenever the game needs to check for a winner, which is why it's placed globally at the top of the script.

## Putting it Together (Conceptually)

Imagine the computer playing Tic Tac Toe:

```
Computer: Okay, Player X just put their mark in square 4.
Computer: Now I need to check if X won.
Computer: I'll look at my "Winning Rules" list (`winPatterns`).
Computer: Rule 1 is [0, 1, 2] (top row). Are squares 0, 1, and 2 all 'X'? Let me check... No.
Computer: Rule 2 is [0, 4, 8] (diagonal). Are squares 0, 4, and 8 all 'X'? Let me check... Hmm, square 4 is X, but what about 0 and 8? Not all X yet.
Computer: ... (checks Rule 3, Rule 4, etc.) ...
Computer: Rule 7 is [3, 4, 5] (middle row). Are squares 3, 4, and 5 all 'X'? Let me check... Square 3 is X, square 4 is X, and Player X just put their mark in square 5 and it's also X! Yes!
Computer: Player X wins!
```

This is the basic process. The `winPatterns` list provides the computer with the specific square combinations it needs to look at.

## What's Next?

We now understand the foundation of the board ([Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md)) and what constitutes a win (this chapter). But we're missing a crucial piece: How does the game know *whose turn* it is to place an 'X' or an 'O'?

In the next chapter, we'll explore [Chapter 3: Player Turn Management](03_player_turn_management_.md) – how we keep track of whose turn it is and switch between players.

[Chapter 3: Player Turn Management](03_player_turn_management_.md)

---

Generated by AI Codebase Knowledge Builder