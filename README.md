# W_chess

This project provides Python utilities for detecting chess pieces from a
screen capture and analysing the position with [Stockfish](https://stockfishchess.org/).
It began as an experiment and was never meant for competitive play. Use it only
for educational purposes.

## Requirements

Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

The `pywin32` dependency means the code is primarily intended for Windows
systems.

## Running

Execute the main script after installing requirements:

```bash
python main.py
```

The program will ask for your colour and then start capturing the board,
printing Stockfish's best moves for each detected position.
