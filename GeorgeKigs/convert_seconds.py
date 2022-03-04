def my_function(minutes:int):
    '''
    A function to convert minutes to seconds.
    '''
    try:
        seconds = int(minutes) * 60
        if minutes < 0:
            raise ValueError("Value has to be postive")
        return seconds
    except ValueError:
        return "Value should be a positive int"
