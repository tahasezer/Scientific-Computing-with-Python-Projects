def add_time(start_time, duration, start_day=None):
  # Splitting the start time and period
  start_time, period = start_time.split()
  
  # Splitting the hours and minutes of the start time
  start_time = start_time.split(':')
  
  # Splitting the hours and minutes of the duration
  duration = duration.split(':')
  
  # Converting start hours to 24-hour format
  if period=="PM":
    start_hours=int(start_time[0])+12
  else:
    start_hours=int(start_time[0])

  # Converting start minutes, duration hours and minutes to integer
  start_min=int(start_time[1])
  duration_hours=int(duration[0])
  duration_min=int(duration[1])

  left_hours=0
  
  # Calculating total minutes
  total_min=start_min+duration_min
  
  # Adjusting total minutes if it exceeds 60
  if total_min>=60:
    left_hours=total_min//60
    total_min %= 60
    
  # Calculating total hours
  total_hours=start_hours+duration_hours+left_hours

  n_next_day = 0

  # Adjusting total hours if it exceeds 24
  if total_hours>24:
    n_next_day=total_hours//24
    total_hours%= 24 
  else:
    n_next_day = 0

  # Adjusting total hours to AM/PM format
  if total_hours > 0 and total_hours < 12 :
    period="AM"
  elif total_hours==12:
    period="PM"
  elif total_hours>12:
    period="PM"
    total_hours-=12
  elif total_hours==0:
    period="AM"
    total_hours+=12

  week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

  # Adding days if start day is provided
  if start_day :
    weeks=n_next_day//7
    k=week_days.index(start_day.lower().capitalize()) + (n_next_day - 7 * weeks)
    if k>=7:
      k-=7
    day=", "+week_days[k]
  else:
    day = ""

  # Adding information about next day(s)
  if n_next_day > 0 :
    if n_next_day == 1 :
      days_later = " (next day)"
    else :
      days_later = " (" + str(n_next_day) + " days later)"
  else :
    days_later = ""
    
  # Constructing the new time string
  new_time=str(total_hours)+":"+(str(total_min) if total_min > 9 else ("0" + str(total_min)))+" "+ period+ day + days_later
  return new_time
