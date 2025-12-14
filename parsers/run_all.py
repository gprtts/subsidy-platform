from parsers.moscow import MoscowParser

def main():
    parsers = [
        MoscowParser(),
    ]

    for parser in parsers:
        parser.run()

if __name__ == "__main__":
    main()
