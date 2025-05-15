# Chapter 3: Player Turn Management

Welcome back! In our last chapter, [Chapter 2: Winning Rules (Patterns)](02_winning_rules__patterns__.md), we learned how our game knows *what* combinations of squares make a player win. We have our game squares ([Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md)) and we know the winning patterns.

But there's a crucial part missing from our game: How does it know *whose turn* it is? In Tic Tac Toe, Player 'O' usually goes first, then Player 'X', then 'O' again, and so on. We need a system to manage this order.

## What is Player Turn Management?

Imagine you're playing a board game with a friend. You take your turn, and then you announce, "Okay, your turn!" and your friend takes their turn. You take turns back and forth until the game ends.

Player Turn Management in our code is the same idea. It's the system that ensures:

1.  Only one player can make a move at a time.
2.  The players take turns in the correct order ('O', 'X', 'O', 'X', ...).

## Keeping Track of the Current Turn

To manage whose turn it is, our game needs a way to remember this information. We use a special variable for this purpose. In our `app.js` code, you'll see this line:

```javascript
let turn0 = true;
```

*   `let turn0 = true;`: This line declares a variable named `turn0` and sets its starting value to `true`.
    *   We'll use `true` to mean it's Player 'O''s turn. ('O' often goes first in Tic Tac Toe, and `turn0` sounds a bit like "turn O").
    *   We'll use `false` to mean it's Player 'X''s turn.

So, right when the game starts, `turn0` is `true`, indicating that 'O' is the first player to move.

## How the Turn Switches

The turn needs to switch *after* a player successfully makes a move. This happens inside the code that runs when a box is clicked. Remember from [Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md) that we have code that listens for clicks on the boxes?

Inside that click listener code, after we figure out which mark to place, we also update the `turn0` variable to switch turns.

Look at this simplified snippet from the click handler in `app.js`:

```javascript
boxes.forEach((box) => {
  box.addEventListener("click", (e) => {
    if (turn0) {
      // If turn0 is true, it's O's turn
      box.innerText = "O"; // Place 'O'
      turn0 = false; // Switch turn to X (set turn0 to false)
    } else {
      // If turn0 is false, it's X's turn
      box.innerText = "X"; // Place 'X'
      turn0 = true; // Switch turn to O (set turn0 to true)
    }
    box.disabled = true; // Disable the box (from Chapter 1)
    // checkWinner(); // Check for winner (from later chapter)
  });
});
```

Let's break down the `if/else` part related to turn management:

1.  `if (turn0)`: The code checks the value of the `turn0` variable.
2.  `if (turn0)` is `true`: This block of code runs.
    *   `box.innerText = "O";`: The game places an 'O' in the clicked box.
    *   `turn0 = false;`: **This is the key!** The value of `turn0` is changed from `true` to `false`. For the *next* click, the `if (turn0)` check will be false, and the `else` block will run.
3.  `else` (if `turn0` is `false`): This block of code runs.
    *   `box.innerText = "X";`: The game places an 'X' in the clicked box.
    *   `turn0 = true;`: **This is the key!** The value of `turn0` is changed from `false` back to `true`. For the *next* click, the `if (turn0)` check will be true again, and the `if` block will run.

This simple `if/else` structure, combined with changing the `turn0` variable, makes sure that 'O' and 'X' marks are placed alternately every time a box is clicked.

## Step-by-Step Turn Switching

Let's trace what happens when the first two moves are made:

1.  **Game Starts:** `turn0` is `true`. It's O's turn.
2.  **Player Clicks Box:** The click event handler runs.
3.  **Check Turn:** The code sees `if (turn0)` is `true`.
4.  **Place Mark:** It sets the box's text to 'O'.
5.  **Switch Turn:** It sets `turn0` to `false`.
6.  **Disable Box:** The box is disabled.
7.  **First Turn Ends:** `turn0` is now `false`. It's X's turn.
8.  **Another Player Clicks Box:** The click event handler runs again for a *different* box.
9.  **Check Turn:** The code sees `if (turn0)` is `false`.
10. **Place Mark:** It goes into the `else` block and sets the box's text to 'X'.
11. **Switch Turn:** It sets `turn0` back to `true`.
12. **Disable Box:** The box is disabled.
13. **Second Turn Ends:** `turn0` is now `true`. It's O's turn again.

And so the game continues, switching between `turn0 = true` and `turn0 = false` after each valid move.

## Where in the Code?

As shown above, the turn management logic is primarily handled inside the `addEventListener` function attached to each `box`.

```javascript
// ... inside the event listener for each box ...

    // Check whose turn it is based on 'turn0'
    if (turn0) {
      box.innerText = "O"; // Place O's mark
      box.style.color = "green"; // (Specific styling, not core turn logic)
      turn0 = false; // *** Switch turn to X ***
    } else {
      box.innerText = "X"; // Place X's mark
      box.style.color = "red"; // (Specific styling)
      turn0 = true; // *** Switch turn to O ***
    }

    box.disabled = true; // Disable the box
    // checkWinner(); // Check for winner (covered later)

// ... rest of the code ...
```

The `let turn0 = true;` declaration is done once at the beginning of the script so the variable is available to the click handler.

## Conclusion

Player Turn Management in our Tic Tac Toe game is simply about keeping track of whose turn it is using a variable (`turn0`) and switching the value of that variable (`true` to `false`, or `false` to `true`) after each valid move is made. This ensures the game flows correctly with players taking turns.

Now that we know how we manage turns, we can look closer at the process of actually placing the mark in the clicked square, which depends directly on whose turn it is.

Next, we'll dive into [Chapter 4: Move Placement Handler](04_move_placement_handler_.md) to see how the game uses the turn information to place the correct 'X' or 'O' in the clicked square.

[Chapter 4: Move Placement Handler](04_move_placement_handler_.md)

---

Generated by AI Codebase Knowledge Builder