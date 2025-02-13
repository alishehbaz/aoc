import hashlib


def getLowestNumber(puzzleInput, start, end, numOfZeroesToBeMatched):

    zeroesToBeMatched = "0" * numOfZeroesToBeMatched

    for i in range(start, end):
        toBeHashed = puzzleInput + str(i)

        md5Hash = hashlib.md5(toBeHashed.encode("utf-8")).hexdigest()

        if md5Hash[:numOfZeroesToBeMatched] == zeroesToBeMatched:
            return i
