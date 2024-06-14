def to_latin(word):
    alph = {
        'й': 'i', 'ц': 'ts', 'у': 'u', 
        'к': 'k', 'е': 'ye', 'н': 'n', 
        'г': 'g', 'ш': 'sh', 'щ': 'shch', 
        'з': 'z', 'х': 'kh', 'ъ': '', 
        'ф': 'f', 'ы': 'i', 'в': 'v', 
        'а': 'a', 'п': 'p', 'р': 'r', 
        'о': 'o', 'л': 'l', 'д': 'd', 
        'ж': 'zh', 'э': 'ae', 'я': 'ya', 
        'ч': 'ch', 'с': 's', 'м': 'm', 
        'и': 'i', 'т': 't', 'ь': '', 
        'б': 'b', 'ю': 'yu'
    }

    lat_word = ''.join([alph[i] if i in alph.keys() else i for i in word])
    
    return lat_word
