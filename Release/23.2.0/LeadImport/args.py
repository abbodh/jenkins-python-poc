import argparse

def argstoparse():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--environment', action='store', type=str, required=True)
    args = parser.parse_args()
    return args
