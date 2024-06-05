def maxPresentations(scheduleStart, scheduleEnd):
    # Combine start and end times into tuples for easier sorting
    presentations = [(start, end) for start, end in zip(scheduleStart, scheduleEnd)]

    presentations.sort(key=lambda x: x[1])
    
    max_presentations = 0
    current_end_time = 0
    
    for start, end in presentations:
        # If the current presentation starts after the previous one ends, attend it
        if start >= current_end_time:
            max_presentations += 1
            current_end_time = end
    
    return max_presentations