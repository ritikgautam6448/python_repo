# this function checks if a person is sleeping based on the day of the week and vacation status
# weekday is True if it is a weekday, False if it is a weekend
# vacation is True if the person is on vacation, False otherwise
def sleeping (weekday,vacation):
    if not weekday or vacation:
        return True
    else:
        return False