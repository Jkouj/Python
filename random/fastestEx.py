#Print the number of the fastest walker

# Given:  Distances and times for n walkers
# Find:  Speed of the fastest walker

# Get the number of walkers in the group
num_walkers = float(input("How many walkers in your group? "))

# Get the first distance and time
dist = float(input("Enter the distance: "))
time = float(input("Enter the time: "))

# Compute the speed
speed = dist/time

# Intialize counter for loop
i = 1

# Initialize the value for the highest speed
high_speed = speed
fastest = 0

# Loop through to compute speeds and find the highest
while i < num_walkers:
    # Get the distance and time for the next walker
    dist = float(input("Enter the distance: "))
    time = float(input("Enter the time: "))

    # Compute the speed for the next walker
    speed = dist/time

    # Test to see if this speed is higher than the max speed so far
    if speed > high_speed:
        high_speed = speed
        fastest = i+1
    # Increment counter
    i = i + 1

# Print the highest speed
print("The fastest speed in the walking group is: ",high_speed, " miles/minute")
print("The fastest person walking is person #", fastest)
