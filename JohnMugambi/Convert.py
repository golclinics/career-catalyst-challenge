no_of_minuntes = 2

def minutes_to_seconds(minutes):
    seconds = 60
    if(isinstance(minutes, int)):
        return minutes*seconds
    else: 
        return print('Number of minutes must be an integer.')

minutes_to_seconds(no_of_minuntes)
