import argparse

from bot.validators import validate_order
from bot.orders import place_order


parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

validate_order(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)

place_order(
    args.symbol,
    args.side,
    args.type,
    args.quantity,
    args.price
)