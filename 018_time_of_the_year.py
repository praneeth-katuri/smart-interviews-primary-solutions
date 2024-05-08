def solution(seconds):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30,31, 30, 31]
    month_names = ['JAN','FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    year = 1970
    month = 0
    date = 1
    day = 3

    seconds_in_day = 24 * 60 * 60
    days = seconds // seconds_in_day

    while days >= 365:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if days >= 366:
                days -= 366
                year += 1
            else:
                break
        else:
            days -= 365
            year += 1
    
    if (year%4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    for i in range(12):
        if days < days_in_month[i]:
            month = i
            date = days + 1
            break
        else:
            days -= days_in_month[i]
    
    day = (3 + seconds // seconds_in_day) % 7
    print(f"{date:02d}-{month_names[month]}-{year} {day_names[day]}")


t = int(input())
for _ in range(t):
    epoch_seconds = int(input())
    solution(epoch_seconds)