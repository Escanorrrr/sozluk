meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "COOL": "Havalı olmak ya da benzeri bir şey "
            
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
   print(meme_dict[word])
else:
    print("Böyle bir kelime yok")
