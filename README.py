meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL":"bir şakaya karşılıklı cevap",
            "SHEESH":"onaylamak",
            "CREEPY":"korkunç",
            "AGGRO":"agresifleşmek/sinirlenmek",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    
    
    
else:
    print("bu kelime sözlükte yok")
