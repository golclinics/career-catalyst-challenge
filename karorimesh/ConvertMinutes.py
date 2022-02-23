# This function converts given meets in patameter to minutesToSeconds


def minutesToSeconds( minutes){
    if isinstance(minutes, int):
        return minutes * 60
    else:
        return -1
}

# TestCase

print(minutesToSeconds(5))