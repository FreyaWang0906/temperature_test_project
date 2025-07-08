def diagnose_temperature(temp, prev_temp=None):

    if temp < 18:
        return "Too Cold"
    elif temp > 32:
        return "Too Hot"
    elif prev_temp is not None and abs(temp - prev_temp) > 5:
        return "Unstable"
    else:
        return "Normal"


def batch_diagnose(temp_list):

    results = []
    prev = None
    for t in temp_list:
        diagnosis = diagnose_temperature(t,prev_temp=prev)
        results.append(diagnosis)
        prev = t

    return results
