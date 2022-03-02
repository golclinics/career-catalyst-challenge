def minutes_into_sec(x):
  sec = x * 60
  return sec

min = input("Enter minutes to be convert to seconds ")

print( min, " is ", minutes_into_sec(int(min)), " seconds")
