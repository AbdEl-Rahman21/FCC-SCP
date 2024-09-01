def add_time(start, duration, current_day=''):
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = int(start.split(':')[0])
    minutes = int(start.split(':')[1].split(' ')[0])
    am_pm = start.split(':')[1].split(' ')[1]

    if am_pm == 'PM': hours += 12

    hours += int(duration.split(':')[0])
    minutes += int(duration.split(':')[1])

    if minutes >= 60:
        minutes -= 60
        hours += 1

    days = hours // 24

    if days != 0: hours -= days * 24
    if minutes < 10: minutes = '0' + str(minutes)

    if hours > 12:
        new_time = f'{hours - 12}:{minutes} PM'
    elif hours == 12:
        new_time = f'{hours}:{minutes} PM'
    elif hours == 0:
        new_time = f'{hours + 12}:{minutes} AM'
    else:
        new_time = f'{hours}:{minutes} AM'

    if current_day:
        new_day_index = (week_days.index(current_day.title()) + days) % len(week_days)
        new_day = week_days[new_day_index]
        new_time += f', {new_day}'

    if days == 1:
        new_time += ' (next day)'
    elif days > 1:
        new_time += f' ({days} days later)'

    return new_time

print(add_time('8:16 PM', '466:02', 'tuesday'))
