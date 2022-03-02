# Convert minutes to seconds
def minutes_to_seconds(minutes):

	# Check whether argument is numeric
	if str(minutes).isdigit():
		seconds = int(minutes) * 60
		return seconds

	else:
		raise ValueError("The value for minutes needs to be numeric")

# Test values
print(minutes_to_seconds(5))
print(minutes_to_seconds(3))
print(minutes_to_seconds(20))