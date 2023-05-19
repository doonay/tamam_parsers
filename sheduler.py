import schedule
import parser_playstation
import parser_xbox

def run_parsers():
    parser_xbox.xbox_parser()

def main():
    schedule.every().day.at('14:11').do(run_parsers)

    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()