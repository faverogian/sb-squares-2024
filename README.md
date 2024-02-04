# Favero Super Bowl Squares Pool

Gian Favero | 2024

## Overview

This project offers a complete solution for managing a Super Bowl squares pool, integrating features for creating pools, live score updates, payout management, and real-time tweet interactions during the game.
## Features

- **Squares Pool Creation**: Set up your pool, assigning participants random squares.
- **Live Score Updates**: Set and display live scores directly in your pool.
- **Payout Calculation**: Automatically calculate and distribute winnings.
- **Tweet Procurement**: Create relevant tweets upon score updates to keep everyone informed and engaged.

## Getting Started

### Creating a Pool
1. Use the Jupyter Notebook to add the pool partipants (first, lastname)
2. Run all codeblocks
3. A .csv file corresponding to the pool square board will be outputted

### Displaying the Square Board
1. Utilize the .xlsx template to create a prettier square board for the pool
2. Populate the squares with the output of the .csv file obtained from the Jupyter Notebook
3. Style and design as you wish

### Managing In-Game Updates
1. Update the parameters to suit your own pool (payout, pot value, participants)
2. Run the ```running-shell.py``` script to launch the SquareBot
3. Use the commands ```score-type team``` to update the bot with the current score, score payout, and pot deduction
4. In the case of a screw-up, use commands ```restart``` or ```set_score``` to manuever the issue
5. At the conclusion of the game, run ```game-over``` to calculate the final payouts
