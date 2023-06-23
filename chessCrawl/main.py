import argparse
from chessCrawl import crawl as c
from chessCrawl import check


def crawl(args):
    print(">>>>>>>>>>>>>>>>>>this should be run")
    c.crawl()
    pass


parser = argparse.ArgumentParser()
subParsers = parser.add_subparsers()

crawlParser = subParsers.add_parser("crawl", help="")
crawlParser.set_defaults(function=crawl)


def main():
    args = parser.parse_args()
    print(args)
    args.function(args)


if __name__ == "__main__":
    main()
