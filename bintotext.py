osef = False
lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","a","]","^","_","a","a","b","c","b","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

while not osef:
    text = input("Enter binary text: ")
    if len(text) / 8 != round(len(text) / 8,  0):
        print("Wrong")
    else:
        osef = True
        text.replace(" ","")

texte = ""
a = len(text) / 8
while a != 0:
    b = 128
    nb = 0
    c = 65

    for i in range(0, 8):
        if text[i] == "1":
            nb += b
        b = b / 2

    for i in range(0, 57):
        if nb == 32:
            texte += " "
            break
        elif nb == 39:
            texte += "\'"
            break
        elif nb == c:
            texte += lettres[i]
            break
        else:
            c+=1

    text = text[8:len(text)]

    a -= 1
print(texte)
