letras = '()[]{}'

map_charcter = {'(':')',
                '[':']',
                '{':'}'}

if len(letras) % 2 == 0 :
    last_value = None
    for index, value in enumerate(letras):
        if index % 2 != 0:
            try:
                val_check = map_charcter[last_value]
                if val_check == value:
                    pass
            except:
                return None
        else: 
            last_value = value
    return 'OK'
else:
    return None
            