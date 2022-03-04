def my_function(minutes:int):
    '''
    A function to convert minutes to seconds.
    '''
    try:
        seconds = int(minutes) * 60
        return seconds
    except ValueError:
        return "Value should be an int"
