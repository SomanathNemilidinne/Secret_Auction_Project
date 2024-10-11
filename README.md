# Secret Auction README

Welcome to the **Secret Auction** project! This fun and interactive auction program allows users to place bids anonymously, and at the end, it reveals the highest bidder. Built entirely with Python, it’s a great way to understand basic programming concepts while engaging with the community!

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)

## Project Overview

The **Secret Auction** program simulates a blind auction environment. Users can enter their names and bids, and the program will determine the highest bidder once all bids are submitted. 

## Features
- Anonymous bidding: Users can submit bids without revealing their identities.
- Clear winner announcement: The program clearly displays the highest bidder and their bid amount.
- User-friendly prompts: Easy-to-follow input prompts make the experience seamless.

## Installation

To run the Secret Auction project, ensure you have Python installed on your machine. If you haven’t done this yet, you can download it from [python.org](https://www.python.org/downloads/).

1. Clone this repository or download the files.
2. Navigate to the project directory in your terminal.

```bash
git clone <repository-url>
cd secret-auction
```

3. Run the main program using Python:

```bash
python secretauction.py
```

## Usage

1. Launch the program in your terminal.
2. Follow the prompts to enter your name and bid.
3. After everyone has submitted their bids, the program will display the highest bidder.

## Code Structure

The project consists of two main files:

### `secretauction.py`

This is the main file that contains the auction logic. Here’s a brief overview of its structure:

- **Input Handling**: Prompts users for their names and bids.
- **Data Storage**: Bids are stored in a dictionary.
- **Bid Comparison**: Determines the highest bid using a comparison function.

### `art.py`

This file contains the ASCII art logo that is displayed when the auction starts. Here’s a sneak peek of the logo:

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
```

## Contributing

We welcome contributions! If you have ideas for new features, improvements, or bug fixes, please feel free to submit a pull request. 

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch and create a pull request.

---

Thank you for checking out the Secret Auction project! Happy bidding! 🏆💰

*Created with ❤️ by Somanath Nemilidinne*
