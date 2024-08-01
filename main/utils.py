
def group_time_slots(t):
    time_row = []
    time_group = []
    for i in t:
        time_row.append(str(i))
        if len(time_row) == 4:
            time_group.append(time_row)
            time_row = []
    if time_row:
        time_group.append(time_row)

    return time_group