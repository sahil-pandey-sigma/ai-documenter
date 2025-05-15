# Chapter 1: Game Squares (Boxes)

Welcome to the first chapter of our Tic Tac Toe tutorial! We're going to build a simple game step-by-step, and we'll start with the very foundation: the game board itself.

Imagine you're playing Tic Tac Toe on paper. You draw a grid, right? That grid has 9 separate spots where you can place your 'X' or 'O'. In our web-based game, we need to do the same thing – we need to represent these 9 spots and make them interactive so a player can click on them.

These interactive spots are what we'll call "Game Squares" or simply "Boxes". They are the clickable areas on our game board.

## What are Game Squares?

Think of the game board as having 9 individual sections. Each section is a "box".

*   **They are clickable:** A player interacts with the game by clicking on one of these boxes.
*   **They hold a mark:** Once clicked, a box will display either an 'X' or an 'O'.
*   **They are unique:** Even though they look similar, each box is a distinct part of the board, and the game needs to know *which specific* box was clicked.

So, how do we work with these boxes in our code?

## Finding and Reacting to Our Boxes

Our web page has the visual representation of the board, including these 9 boxes. In our `app.js` file, the first thing we need to do is find these boxes so our code can interact with them.

We use some special JavaScript code to do this. Look at this line from `app.js`:

```javascript
let boxes = document.querySelectorAll(".box");
```

What this line does is go through the entire web page (`document`) and find all the elements that have a special label (a "class") called `.box`. It then collects all of these found elements into a list called `boxes`. Now, the `boxes` variable holds references to all 9 of our game squares!

Next, we want something to happen *when* a player clicks on any of these boxes. We need to tell each box, "Hey, listen for a click!" We do this by looping through the `boxes` list and adding an "event listener" to each one.

Here's the part of the code that does that:

```javascript
boxes.forEach((box) => {
  box.addEventListener("click", (e) => {
    // ... code to handle the click ...
  });
});
```

*   `boxes.forEach((box) => { ... });`: This is like saying, "For *each* individual `box` in our list of `boxes`, do the following..."
*   `box.addEventListener("click", (e) => { ... });`: For the current `box` we're looking at, this line says, "When this `box` is clicked, run the code inside the curly braces `{}`." The `e` is short for "event" and gives us information about the click, like *which* box was clicked.

So, this setup makes sure that when *any* of the 9 boxes is clicked, our special click-handling code runs.

## Placing a Mark and Disabling the Box

When a box is clicked, two important things need to happen regarding that specific box:

1.  We need to place the current player's mark ('X' or 'O') inside it.
2.  We need to make sure it can't be clicked again (you can't change a move!).

Inside the click-handling code we just saw (`box.addEventListener(...)`), after we know which box was clicked, we do this:

```javascript
// ... inside the click event handler ...
    box.innerText = "O"; // Or "X", depending on whose turn it is
    box.disabled = true; // Make the box unclickable
// ... rest of the code ...
```

*   `box.innerText = "O";`: This changes the text *inside* the clicked `box` to 'O' (or 'X'). This is how the mark appears on the board!
*   `box.disabled = true;`: This tells the browser to disable this specific `box`. Disabled elements can't be clicked, so the player can't mess with a square that already has a mark.

## Putting it Together (Simplified)

Let's trace what happens when a player clicks on one of the empty squares on the board, keeping it simple for now:

1.  The player clicks on a square.
2.  Because we added an event listener to that square, the code inside the `addEventListener` function runs.
3.  The code identifies *which* square was clicked (`e.target` or `box` in our loop).
4.  It places the current player's mark ('X' or 'O') inside that square by changing its `innerText`.
5.  It disables that square so it cannot be clicked again.
6.  *(As we'll see in later chapters, other things happen too, like checking for a winner!)*

Here's a very simplified look at the core interaction with a single box:

```javascript
// Imagine 'clickedBox' is the specific box that was clicked
clickedBox.innerText = "O"; // Put 'O' inside it
clickedBox.disabled = true; // Stop it from being clicked again

// Other checks like win-checking happen after this
// checkWinner();
```

This simple process is repeated every time a player clicks on an empty square, managing the placement of marks on our game squares.

## What's Next?

Now that we understand how we represent the game squares, how we find them, react when they are clicked, and place marks in them, we can move on to the next piece of the puzzle. Clicking on boxes and placing marks is great, but how do we know if someone has won the game?

In the next chapter, we'll explore the concept of [Winning Rules (Patterns)](02_winning_rules__patterns__.md) – the different combinations of three squares that result in a win.

---

Generated by AI Codebase Knowledge Builder