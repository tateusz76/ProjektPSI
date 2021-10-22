def info(dataText):
    slownik = {
        'length': len(dataText),
        'letters':  list(dataText),
        'big_letters': dataText.upper(),
        'small_letters': dataText.lower()
    }
    for val in slownik.values():
        print(val)

info("Dog")