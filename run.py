import argparse
from game import main

def parse_arguments():
    parser = argparse.ArgumentParser(description='Run the game with different environment settings.')
    parser.add_argument('--dev', action='store_true', help='Run the game in development mode.')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    game = main.Game(dev_mode=args.dev)
    game.run()
