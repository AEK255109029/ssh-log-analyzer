def get_risk(count):
    

    if count >= 5:
        return "HIGH"

    elif count >= 3:
        return "MEDIUM"

    return "LOW"
