def calculateWatts(devices):
    watts = 0
    for device in devices:
        watts += device['watts']
    return watts/len(devices)