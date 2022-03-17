def convert(minutes):
    if minutes < 0:
        return 0
    else:
        return minutes * 60

def main():
    minutes = int(input())
    print(convert(minutes))

if __name__ == "__main__":
    main()