from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reversed(request):
    usertext = request.GET['usertext']
    wordscount = len(usertext.split())
    reversetext = usertext[::-1]
    return render(request, 'reversed.html', {'usertext': usertext, 'reversetext': reversetext,'wordscount': wordscount})