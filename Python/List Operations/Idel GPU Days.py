def gpu_idle_days(days, training_sessions):
    # Create a boolean array of size 'days' initialized to False
    # False means the GPU is idle on that day
    occupied = [False] * days  

    # Iterate through each training session's start and end days
    for start, end in training_sessions:
        # Mark the GPU as occupied for all days in the given range
        for day in range(start, end + 1):
            # Convert 1-based day to 0-based index for correct list indexing
            occupied[day - 1] = True  

    # Count the number of idle days by summing occurrences of False in the occupied list
    return sum(1 for day in range(1, days + 1) if not occupied[day - 1])
