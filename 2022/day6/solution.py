def getStartingMarker(signal, uniqueCharMarker):
    unique = set()
    for i in range(len(signal)-uniqueCharMarker-1):
        for j in range(uniqueCharMarker):
            unique.add(signal[i+j])
        if len(unique) == uniqueCharMarker:
            return i+uniqueCharMarker

        unique = set()
