def funkcja2(text):
    dict = {
        'length':len(text),
        'letters':list(text),
        'big_letters':text.upper(),
        'small_letters':text.lower()
    }
    for k, v in dict.items():
        print(k+' '+str(v))

funkcja2('ubagubaTeXT123SDADA')