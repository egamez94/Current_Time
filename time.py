def time():
    # import date from datetime
    from datetime import datetime
    #find time
    now = datetime.now()
    #Time in hour, minutes, and seconds
    current_time = now.strftime("%H:%M:%S")
    print("Time = ", current_time)


time()