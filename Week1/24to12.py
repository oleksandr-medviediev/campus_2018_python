from validate_24h import is_valid_24h

def main():
    time_24h = input('enter time in 24h format:\n')

    if not is_valid_24h(time_24h):
        print('not valid')
        return
    
    hours = int(time_24h[:2])
    minutes = int(time_24h[3:])
    is_am = hours <= 11

    if not is_am: hours -= 12

    am_pm_str = "am" if is_am else "pm"
    res = "{:02d}:{:02d} {:s}".format(hours, minutes, am_pm_str)
    print(res)

if __name__ == "__main__":
    main()