import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--module")
    parser.add_argument("-pk", "--private_key")
    parser.add_argument("-tn", "--token_name")
    parser.add_argument("-tv", "--token_value")
    parser.add_argument("-ftv", "--from_token_value")
    parser.add_argument("-r", "--rate")
    parser.add_argument("-ta", "--asset_A_name")
    parser.add_argument("-tb", "--asset_B_name")

    return parser
