
def check_settings(settings):
    try:
        settings = dict(settings)
    except:
        return False, "not a valid dictionary"
    else:
        return True, ''