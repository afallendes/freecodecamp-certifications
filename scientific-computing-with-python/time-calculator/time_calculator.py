def add_time(start:str, duration:str, start_weekday:str = '') -> str:
    
    start_h, start_m = time_values(start)
    duration_h, duration_m = [ int(_) for _ in duration.split(':') ]

    total_m = start_m + duration_m
    end_m = total_m - 60 if total_m > 60 else total_m

    total_h = start_h + duration_h + total_m // 60
    days = total_h // 24
    end_h = total_h - 24 * days
    
    end_time = time_label(end_h, end_m)

    # Add time
    time_calculation = end_time

    # Add weekday (optional)
    if start_weekday:
        start_d = WEEKDAYS_VALUES.index(start_weekday.lower())
        end_d = WEEKDAYS_VALUES[ (start_d + days) % 7 ]
        time_calculation += ', ' + end_d.title()
    
    # Add days
    if days == 1:
        time_calculation += ' (next day)'
    elif days > 1:
        time_calculation += f' ({days} days later)'

    return time_calculation

# Helpers:

WEEKDAYS_VALUES = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
]


def time_values(time_str:str):
    time, meridiem = time_str.split()
    h, m = [ int(_) for _ in time.split(':') ]
    return (h, m) if meridiem == 'AM' else (h + 12, m)


def time_label(h:int, m:int):
    m = str(m).zfill(2)
    if h < 12:
        return f'{12 if h == 0 else h}:{m} AM'
    else:
        return f'{12 if h == 12 else h - 12}:{m} PM'
