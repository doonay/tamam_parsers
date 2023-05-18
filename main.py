import schedule

def run_parsers():
    print('Steam parser 1 is done')
    print('Steam parser 2 is done')
    print('Ps parser is done')
    print('Epic parser 1 is done')

def main():
    schedule.every().day.at('03:00').do(run_parsers)

    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()