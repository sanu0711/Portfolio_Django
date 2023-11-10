from django.shortcuts import render
from django.http import HttpResponse
import random

def Create_password(request,l,s,n):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    for char in range(1, l + 1):
        password_list.append(random.choice(letters))

    for char in range(1, s + 1):
        password_list += random.choice(symbols)

    for char in range(1, n + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    return password


game_name="""𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕥𝕙𝕖 ℝ𝕒𝕟𝕕𝕠𝕞 ℙ𝕒𝕤𝕤𝕨𝕠𝕣𝕕 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣!"""

def randompassword(request):
    try:
        data={'game_name':game_name,"l":0,"s":0,"n":0}
        if request.method == 'POST':
            letter = int(request.POST.get('letters'))
            special = int(request.POST.get('symbol'))
            numbers = int(request.POST.get('numbers'))
            password = Create_password(request,letter,special,numbers)
            data={'password':password
                ,'game_name':game_name,"l":letter,"s":special,"n":numbers}
            return render(request,'Random-Password-Generator.html',data)
        else:
            return render(request,'Random-Password-Generator.html',data)
    except:
        pass
# Create your views here.













