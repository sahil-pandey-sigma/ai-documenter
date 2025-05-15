# Chapter 5: Winner Checker

Welcome back! In our journey so far, we've built the foundation of our Tic Tac Toe game. We have our game squares ([Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md)), we know the winning combinations ([Chapter 2: Winning Rules (Patterns)](02_winning_rules__patterns__.md)), we can manage whose turn it is ([Chapter 3: Player Turn Management](03_player_turn_management_.md)), and we know how to place the correct mark in a clicked square and disable it ([Chapter 4: Move Placement Handler](04_move_placement_handler_.md)).

But there's one huge missing piece: How does the game know when someone has won? After a player places their mark, we need to immediately check if that move finished a winning line. This is the job of the "Winner Checker".

## What is the Winner Checker?

Imagine a referee in a sports game. After a critical play, the referee might pause and review the action to see if a rule was broken or if a point was scored.

Our Winner Checker function acts like this referee for our Tic Tac Toe game. After *every single move* is successfully placed on the board, the game needs to quickly check the board to see if the player who just moved has created one of the winning patterns we defined in [Chapter 2: Winning Rules (Patterns)](02_winning_rules__patterns__.md).

Its main goal is simple: **Determine if the game is over because a player has won.**

## When Does the Check Happen?

The Winner Checker must run *immediately* after a player places their mark and before the next player's turn begins. Why? Because the move just made is the *only* move that could have possibly created a new winning line. If that move didn't create a win, then no win occurred on this turn.

Looking back at our [Chapter 4: Move Placement Handler](04_move_placement_handler_.md), you'll see the spot where we need to add this check. It's right after we place the mark and disable the box:

```javascript
boxes.forEach((box) => {
  box.addEventListener("click", (e) => {
    // ... code to place the mark and switch turn ...
    // ... disable the box ...

    // *** This is where we check for a winner ***
    checkWinner(); // <-- We need a function like this!

  });
});
```

Every time a square is clicked and a mark is placed, this `checkWinner()` function will be called to do its job.

## How Does it Work? (High Level)

The `checkWinner` function needs access to two main things:

1.  **The current state of the board:** What marks are currently in each of the 9 squares?
2.  **The list of winning patterns:** The `winPatterns` array we discussed in [Chapter 2: Winning Rules (Patterns)](02_winning_rules__patterns__.md).

Here's the basic process the `checkWinner` function follows:

*   Go through *each* winning pattern defined in `winPatterns`.
*   For the current pattern being checked (e.g., `[0, 1, 2]` for the top row):
    *   Look at the marks in the squares corresponding to the numbers in the pattern (Square 0, Square 1, Square 2).
    *   Check if all three of these squares are **not empty**. (An empty square can't be part of a win).
    *   Check if the marks in these three squares are **exactly the same** ('X', 'X', 'X' or 'O', 'O', 'O').
*   If it finds *any* pattern that meets these two conditions (not empty AND same mark), it means a winner is found!
*   If it checks *all* 8 patterns and doesn't find a match, nobody has won with this move, and the game continues.

## The `checkWinner` Function in Code

Let's look at the actual `checkWinner` function in our `app.js` file.

```javascript
const checkWinner = () => {
  // This function loops through all winning patterns
  // and checks the board to see if any pattern is filled
  // with the same non-empty mark.
};
```

This is where our winning rules (`winPatterns`) come into play. We need to loop through that list:

```javascript
const checkWinner = () => {
  // winPatterns is the list of all winning combinations (like [0, 1, 2])
  for (let pattern of winPatterns) {
    // 'pattern' will be one winning combination at a time, e.g., [0, 1, 2]

    // We need to get the marks from the squares listed in this pattern
    // Remember 'boxes' is our list of all 9 squares from Chapter 1
    let pos1Val = boxes[pattern[0]].innerText; // Mark in the 1st square of pattern
    let pos2Val = boxes[pattern[1]].innerText; // Mark in the 2nd square of pattern
    let pos3Val = boxes[pattern[2]].innerText; // Mark in the 3rd square of pattern

    // Now, check if these three squares form a winning line...
    // (Checks explained next)
  }
};
```

*   `for (let pattern of winPatterns)`: This loop goes through each item in the `winPatterns` array. In the first loop, `pattern` will be `[0, 1, 2]`. In the second, `[0, 4, 8]`, and so on.
*   `boxes[pattern[0]]`: `pattern[0]` gets the *first* number from the current pattern (e.g., `0`). `boxes[0]` gets the actual first game square element (from our `boxes` list, see [Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md)).
*   `.innerText`: This gets the mark ('O', 'X', or empty `""`) currently displayed inside that game square. We store these marks in `pos1Val`, `pos2Val`, and `pos3Val`.

Next, we add the conditions to check if these three squares form a win:

```javascript
const checkWinner = () => {
  for (let pattern of winPatterns) {
    let pos1Val = boxes[pattern[0]].innerText;
    let pos2Val = boxes[pattern[1]].innerText;
    let pos3Val = boxes[pattern[2]].innerText;

    // Condition 1: Are all three squares in this pattern NOT empty?
    if (pos1Val != "" && pos2Val != "" && pos3Val != "") {

      // Condition 2: Do all three non-empty squares have the SAME mark?
      if (pos1Val === pos2Val && pos2Val === pos3Val) {

        // *** Winner Found! ***
        console.log("Winner!", pattern); // Just for checking behind the scenes

        // Do something to show the winner and end the game
        // (Covered in detail next)

      }
    }
  }
};
```

Let's break down the `if` conditions:

*   `if (pos1Val != "" && pos2Val != "" && pos3Val != "")`: This checks if none of the three squares in the current pattern are empty. `!= ""` means "is not an empty string". The `&&` means "and", so all three parts must be true. If any square is empty, this pattern can't be a winning one *yet*, so the code inside this `if` block is skipped, and the loop moves to the next pattern.
*   `if (pos1Val === pos2Val && pos2Val === pos3Val)`: This checks if the mark in the first square (`pos1Val`) is the same as the mark in the second (`pos2Val`), AND if the mark in the second square is the same as the mark in the third (`pos3Val`). If both are true, it means all three squares have the same mark (either 'X' or 'O' because of the first check).

If both conditions are met for a specific pattern, it means we have found a winner!

## What Happens When a Winner is Found?

Once the `checkWinner` function detects a winning pattern, the game needs to react. In our simple code, it does two things:

1.  It shows a message saying who won.
2.  It resets the game (by reloading the page).

This happens inside the innermost `if` block where we found the winner:

```javascript
// ... inside the checkWinner function, inside the winning if blocks ...

      if (pos1Val === pos2Val && pos2Val === pos3Val) {
        // Winner Found!

        // 1. Show Winner Message
        // pos1Val will be the winning mark ('X' or 'O')
        setTimeout(() => {
          alert("Winner : " + pos1Val); // Show a pop-up message
        }, 100); // Add a small delay (optional, but sometimes nice)


        // 2. Reset the Game
        // For simplicity, we'll just reload the page
        location.reload();

      }
// ... rest of the checkWinner function ...
```

*   `alert("Winner : " + pos1Val)`: The `alert()` function pops up a simple message box in the browser. We combine the text "Winner : " with the winning mark (`pos1Val`, which is either 'X' or 'O'). The `setTimeout` is used here to give a brief moment before the alert appears, though 100ms is very fast. The 5000 value in the original code looks like it might have been intended as a delay in milliseconds, but it's placed incorrectly in the `setTimeout` arguments in the snippet provided in the context. The simpler form `alert("Winner : " + pos1Val);` works fine without `setTimeout` for basic functionality.
*   `location.reload()`: This is a browser command that simply reloads the current web page. It's a quick way to reset the game back to its starting state for a new round. We'll discuss game resetting more in the next chapter ([Chapter 6: Game Reset Functionality](06_game_reset_functionality_.md)).

## The Winner Checking Process in Flow

Let's trace the flow when a move is made and `checkWinner` is called:

```mermaid
sequenceDiagram
    participant Player
    participant Box as Clicked Box
    participant Handler as Move Handler (Click Listener)
    participant Checker as Winner Checker (checkWinner fn)
    participant Board as Game Board (boxes)
    participant Patterns as Winning Patterns (winPatterns)

    Player->Box: Clicks empty square
    Box->Handler: Triggers 'click' event
    Handler->Board: Places 'X' or 'O', disables Box
    Handler->Checker: Calls checkWinner()
    Checker->Patterns: Gets the list of win patterns
    loop For each pattern in winPatterns
        Checker->Board: Checks innerText of 3 squares for this pattern
        alt If all 3 squares are NOT empty AND have the same mark
            Checker->Checker: Winner found!
            Checker-->>Player: Shows "Winner: X" or "Winner: O" message
            Checker->Game: Resets the game (e.g., reloads page)
            break Loop ends (game over)
        end
    end
    opt If no winner found after checking all patterns
        Checker-->Handler: Returns (or finishes)
        Handler->>Player: Game continues (next turn)
    end
```

This diagram shows that the `checkWinner` function is triggered by the `Move Handler` (the click listener). It then loops through the `winPatterns` and checks the `Board` state for each pattern. If a winner is found during this loop, it stops and signals the end of the game. Otherwise, the function finishes, and the game continues.

## Where in the Code?

The `checkWinner` function is defined once in your `app.js` file:

```javascript
// ... other code ...

const checkWinner = () => {
  for (let pattern of winPatterns) {
    let pos1Val = boxes[pattern[0]].innerText;
    let pos2Val = boxes[pattern[1]].innerText;
    let pos3Val = boxes[pattern[2]].innerText;

    if (pos1Val != "" && pos2Val != "" && pos3Val != "") {
      if (pos1Val === pos2Val && pos2Val === pos3Val) {
        // Found a winner!
        setTimeout(() => {
          alert("Winner : " + pos1Val); // Show who won
        }, 100); // Small delay

        location.reload(); // Reset the game

      }
    }
  }
};

// ... rest of the code ...
```

And it is called inside the click event listener for each box, as shown earlier and in [Chapter 4: Move Placement Handler](04_move_placement_handler_.md):

```javascript
boxes.forEach((box) => {
  box.addEventListener("click", (e) => {
    // ... code to place mark and switch turn ...

    box.disabled = true; // Disable the box

    checkWinner(); // <<< Called here after each move!

    // ... rest of the handler ...
  });
});
```

This setup ensures that after every player makes a move by clicking a box, the game instantly checks if that move resulted in a win by comparing the board state against all possible winning patterns.

## What about a Draw?

Our current `checkWinner` only handles the case where a player wins. What if all 9 squares are filled, but nobody has won? That's a draw (or a tie)! Our current `checkWinner` function doesn't explicitly check for this, but a full Tic Tac Toe game needs to.

A simple way to check for a draw is to count how many boxes have been filled. If all 9 boxes are filled (`box.innerText` is not empty for all of them), and `checkWinner` did *not* find a winner, then it's a draw. This check would also happen after each move. We could add this logic into or after the `checkWinner` function. For this tutorial, we'll stick to the win condition check as the core concept of this chapter.

## Conclusion

The Winner Checker (`checkWinner`) is a vital part of our Tic Tac Toe game. It's the routine that runs after every move, acting as the game's referee to see if the player who just moved has completed any of the predefined winning patterns ([Chapter 2: Winning Rules (Patterns)](02_winning_rules__patterns__.md)). It does this by examining the marks on the game squares ([Chapter 1: Game Squares (Boxes)](01_game_squares__boxes__.md)) at the specific positions listed in each winning pattern. If a win is found, the game announces the winner and prepares for a new game.

Speaking of new games, what happens after a winner is found, or if the game ends in a draw, or if the player just wants to start over? We need a way to reset the game board and its state.

In our final chapter, we'll explore [Chapter 6: Game Reset Functionality](06_game_reset_functionality_.md) – how we can bring the game back to its initial state for a new round.

[Chapter 6: Game Reset Functionality](06_game_reset_functionality_.md)

---

Generated by AI Codebase Knowledge Builder