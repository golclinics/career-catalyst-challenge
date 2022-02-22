# Entry Challenge V3
def min_to_sec(minutes:int):
    return minutes*60

if __name__ == '__main__':
    mins = int(input("Enter Minutes to covert to Seconds: "))
    print("{} Minutes is equivalent to {} Seconds.".format(mins, min_to_sec(mins)))
