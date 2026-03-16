def get_respiration_score(rate):
    if rate <= 8 or rate >= 25:
        return 3
    elif rate >= 9 and rate <= 11:
        return 1
    elif rate >= 21 and rate <= 24:
        return 2
    else:
        return 0
    
def get_spo2_score(value, air_or_oxygen):
    # 1. scores that are the same for everyone
    if value <= 83:
        return 3
    elif value == 84 or value == 85:
        return 2
    elif value == 86 or value == 87:
        return 1

    # 2. universal normal range
    if 88 <= value <= 92:
        return 0
    
    # 3. conditional logic (patient on air or oxygen)

    # patient is on air
    if air_or_oxygen == 0:
        return 0 # 93+ on air is always 0
    
    # patient on oxygen (air_or_oxygen == 2)
    elif air_or_oxygen == 2:
        if value == 93 or value == 94:
            return 1
        elif value == 95 or value == 96:
            return 2
        elif value >= 97:
            return 3
    return 0

def get_temperature_score(temp):
    # rounding to single decimal digit
    t = round(float(temp), 1)

    if t <= 35.0:
        return 3
    elif 35.1 <= t <= 36.0:
        return 1
    elif 38.1 <= t <= 39.0:
        return 1
    elif t >= 39.1:
        return 2
    else:
        # covering the 36.1 - 38.0 range
        return 0
    
def get_consciousness_score(status):
    # status = 0 = alert (0 point)
    # status = non 0 = CVPU (3 points)
    if status == 0:
        return 0
    else:
        return 3
    
# bonus task
def get_cbg_score(value, is_fasting):
    v = float(value)
    if is_fasting:
        if v <= 3.4 or v >= 6.0:
            return 3
        elif 3.5 <= v <= 3.9 or 5.5 <= v <= 5.9:
            return 2
        else:
            return 0
    else:
        if v <= 4.5 or v >= 9.0:
            return 3
        elif 4.6 <= v <= 5.8 or 7.9 <= v <= 8.9:
            return 2
        else:
            return 0
    
def calculate_medi_score(obs, previous_total=None):
    components = [
        obs['air_or_oxygen'],
        get_consciousness_score(obs['consciousness']),
        get_respiration_score(obs['respiration_rate']),
        get_spo2_score(obs['spo2'], obs['air_or_oxygen']),
        get_temperature_score(obs['temperature']),
        # bonus task metric
        get_cbg_score(obs.get('cbg', 5.0), obs.get('is_fasting', True))
    ]

    current_total = sum(components)
    
    # for trend alerting bonus
    is_rising_risk = False
    if previous_total is not None:
        if (current_total - previous_total) > 2:
            is_rising_risk = True

    return current_total, is_rising_risk

