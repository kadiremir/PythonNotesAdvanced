import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser(description="A simple argument parser example.")

# Add arguments
parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

# Parse the arguments
args = parser.parse_args()

# Access the arguments
if args.verbose:
    print(f"Verbose Mode Enabled")
print(f"Name: {args.name}")
print(f"Age: {args.age}")

# Run this script with the following command:
# python argparser.py --name "kadir" --age 38
# For help:
# python argparser.py --help
