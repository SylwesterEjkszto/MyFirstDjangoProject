from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import random
import requests

def home(request):
    return render(request, 'blog/home.html', )

def listofprograms(request):
    return render(request, 'blog/listofprograms.html',)

def dj_bs(request):
    if request.method == "POST":
        strona = 1
        citi = request.POST.get('citi', None)
        first_url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/' + citi + "/?page=" + str(strona)
        first_page = requests.get(first_url)
        first_soup = BeautifulSoup(first_page.content, 'html.parser')
        auction_link = []
        page_number = []
        auction = []
        auction_priceFin = []
        auction_title = []
        for a in first_soup.find_all('a', class_="block br3 brc8 large tdnone lheight24"):
            page_number.append(a)
        page_number.append(1)

        ##### skan właściwy linków #########

        for i in range(len(page_number)):
            strona += 1
            url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/' + citi + "/?page=" + str(strona)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            for a in soup.find_all('a', class_="marginright5 link linkWithHash detailsLinkPromoted", href=True):
                auction_link.append(a['href'])
            for a in soup.find_all('a', class_="marginright5 link linkWithHash detailsLink", href=True):
                auction_link.append(a['href'])

        print("ilość wszystkich aukcji:" + str(len(auction_link)))

        for i in range(len(auction_link)):
            auction.append([])

        ##### skan dokłany aukcji ###########

        for i in range(len(auction_link)):
            auction_url = auction_link[i]
            auction_page = requests.get(auction_url)
            auction_soup = BeautifulSoup(auction_page.content, 'html.parser')
            auction_name = auction_soup.find("h1")

            if "olx" in auction_url:
                auction_price = auction_soup.find("div", class_="price-label")

            else:
                auction_price = auction_soup.find("div", class_="css-1vr19r7")

            auction_price = str(auction_price)
            # auction_surface = auction_soup.find("td", class_="value")
            auction[i].append(str(i))
            auction[i].append(str(auction_name.text))



            if "not-arranged" in auction_price:
                auction_final_price = auction_price#[66:72]
                auction[i].append(auction_final_price)

            elif "css-1vr19r7" in auction_price:
                auction_final_price = auction_price#[25:31]
                auction[i].append(auction_final_price)

            else:
                auction_final_price = auction_price#[62:70]
                auction[i].append(auction_final_price)

            # auction[i].append("cena:" + str(auction_price))
            auction[i].append(str(auction_url))
            # auction[i].append("powierzchnia:" + str(auction_surface.text))
            print(i)

        for i in range(len(auction)):
            auction[i] = [s.strip("\n") for s in auction[i]]
        print(auction)



        h1_val = 1

        return render(request, 'blog/django-bs.html', {'h1_val':auction})

    return render(request, 'blog/django-bs.html')

def NicknameGenerator(request):
    if request.method == "POST":
        malename = ['1. Liam',
                    '2. Noah',
                    '3. William',
                    '4. James',
                    '5. Oliver',
                    '6. Benjamin',
                    '7. Elijah',
                    '8. Lucas',
                    '9. Mason',
                    '10. Logan',
                    '11. Alexander',
                    '12. Ethan',
                    '13. Jacob',
                    '14. Michael',
                    '15. Daniel',
                    '16. Henry',
                    '17. Jackson',
                    '18. Sebastian',
                    '19. Aiden',
                    '20. Matthew',
                    '21. Samuel',
                    '22. David',
                    '23. Joseph',
                    '24. Carter',
                    '25. Owen',
                    '26. Wyatt',
                    '27. John',
                    '28. Jack',
                    '29. Luke',
                    '30. Jayden',
                    '31. Dylan',
                    '32. Grayson',
                    '33. Levi',
                    '34. Issac',
                    '35. Gabriel',
                    '36. Julian',
                    '37. Mateo',
                    '38. Anthony',
                    '39. Jaxon',
                    '40. Lincoln',
                    '41. Joshua',
                    '42. Christopher',
                    '43. Andrew',
                    '44. Theodore',
                    '45. Caleb',
                    '46. Ryan',
                    '47. Asher',
                    '48. Nathan',
                    '49. Thomas',
                    '50. Leo']
        femalename = ['Emma',
                    'Olivia',
                    'Ava',
                    'Isabella',
                    'Sophia',
                    'Charlotte',
                    'Mia',
                    'Amelia',
                    'Harper',
                    'Evelyn',
                    'Abigail',
                    'Emily',
                    'Elizabeth',
                    'Mila',
                    'Ella',
                    'Avery',
                    'Sofia',
                    'Camila',
                    'Aria',
                    'Scarlett',
                    'Victoria',
                    'Madison',
                    'Luna',
                    'Grace',
                    'Chloe',
                    'Penelope',
                    'Layla',
                    'Riley',
                    'Zoey',
                    'Nora',
                    'Lily',
                    'Eleanor',
                    'Hannah',
                    'Lillian',
                    'Addison',
                    'Aubrey',
                    'Ellie',
                    'Stella',
                    'Natalie',
                    'Zoe',
                    'Leah',
                    'Hazel',
                    'Violet',
                    'Aurora',
                    'Savannah',
                    'Audrey',
                    'Brooklyn',
                    'Bella',
                    'Claire',
                    'Skylar',]
        AppearenceAdjectives = ['attractive',
                                'bald',
                                'beautiful',
                                'chubby',
                                'clean',
                                'dazzling',
                                'drab',
                                'elegant',
                                'fancy',
                                'fit',
                                'flabby',
                                'glamorous',
                                'gorgeous',
                                'handsome',
                                'long',
                                'magnificent',
                                'muscular',
                                'plain',
                                'plump',
                                'quaint',
                                'scruffy',
                                'shapely',
                                'short',
                                'skinny',
                                'stocky',
                                'ugly',
                                'unkempt',
                                'unsightly']
        PositivePersonalityAdjectives = ['aggressive',
                                        'agreeable',
                                        'ambitious',
                                        'brave',
                                        'calm',
                                        'delightful',
                                        'eager',
                                        'faithful',
                                        'gentle',
                                        'happy',
                                        'jolly',
                                        'kind',
                                        'lively',
                                        'nice',
                                        'obedient',
                                        'polite',
                                        'proud',
                                        'silly',
                                        'thankful',
                                        'victorious',
                                        'witty',
                                        'wonderful',
                                        'zealous']
        NegativePersonalityAdjectives = ['angry',
                                        'bewildered',
                                        'clumsy',
                                        'defeated',
                                        'embarrassed',
                                        'fierce',
                                        'grumpy',
                                        'helpless',
                                        'itchy',
                                        'jealous',
                                        'lazy',
                                        'mysterious',
                                        'nervous',
                                        'obnoxious',
                                        'panicky',
                                        'pitiful',
                                        'repulsive',
                                        'scary',
                                        'thoughtless',
                                        'uptight',
                                        'worried']
        SizeAdjectives = ['big',
                        'colossal',
                        'fat',
                        'gigantic',
                        'great',
                        'huge',
                        'immense',
                        'large',
                        'little',
                        'mammoth',
                        'massive',
                        'microscopic',
                        'miniature',
                        'petite',
                        'puny',
                        'scrawny',
                        'short',
                        'small',
                        'tall',
                        'teeny',
                        'tiny']
        for e in range(len(malename)):
            malename[e] = malename[e][3:]
        gender = request.POST.get("gender", None)
        gender = gender.lower()
        gendervalue = {}
        if gender== "male":
            randomname = random.choice(malename)
        elif gender=="female":
            randomname = random.choice(femalename)
        else:
            randomname = "choice your gender"
        Adjectives = []
        Adjectives.append(random.choice(AppearenceAdjectives))
        Adjectives.append(random.choice(PositivePersonalityAdjectives))
        Adjectives.append(random.choice(NegativePersonalityAdjectives))
        Adjectives.append(random.choice(SizeAdjectives))
        RandomAdjectives = random.choice(Adjectives)
        randomname = randomname + " " + RandomAdjectives
        gendervalue['outputofnickgenerator'] = randomname
        return render(request, 'blog/NicknameGenerator.html', gendervalue)
    return render(request, 'blog/NicknameGenerator.html',)

def sudoku(request):
    ListOfNumbers = [1,
                     2,
                     3,
                     4,
                     5,
                     6,
                     7,
                     8,
                     9]
    horizontal1 = {'Cell1h1':"",
                   'Cell2h1':"",
                   'Cell3h1':'',
                   'Cell4h1':'',
                   'Cell5h1':"",
                   'Cell6h1':'',
                   'Cell7h1':'',
                   'Cell8h1':'',
                   'Cell9h1':'' }
    horizontal2 = {'Cell1h2':"",
                   'Cell2h2':"",
                   'Cell3h2':'',
                   'Cell4h2':'',
                   'Cell5h2':'',
                   'Cell6h2':'',
                   'Cell7h2':'',
                   'Cell8h2':'',
                   'Cell9h2':'' }
    horizontal3 = {'Cell1h3':"",
                   'Cell2h3':"",
                   'Cell3h3':'',
                   'Cell4h3':'',
                   'Cell5h3':"",
                   'Cell6h3':'',
                   'Cell7h3':'',
                   'Cell8h3':'',
                   'Cell9h3':'' }
    horizontal4 = {'Cell1h4':"",
                   'Cell2h4':"",
                   'Cell3h4':'',
                   'Cell4h4':'',
                   'Cell5h4':"",
                   'Cell6h4':'',
                   'Cell7h4':'',
                   'Cell8h4':'',
                   'Cell9h4':'' }
    horizontal5 = {'Cell1h5':"",
                   'Cell2h5':"",
                   'Cell3h5':'',
                   'Cell4h5':'',
                   'Cell5h5':"",
                   'Cell6h5':'',
                   'Cell7h5':'',
                   'Cell8h5':'',
                   'Cell9h5':'' }
    horizontal6 = {'Cell1h6':"",
                   'Cell2h6':"",
                   'Cell3h6':'',
                   'Cell4h6':'',
                   'Cell5h6':"",
                   'Cell6h6':'',
                   'Cell7h6':'',
                   'Cell8h6':'',
                   'Cell9h6':'' }
    horizontal7 = {'Cell1h7':"",
                   'Cell2h7':"",
                   'Cell3h7':'',
                   'Cell4h7':'',
                   'Cell5h7':"",
                   'Cell6h7':'',
                   'Cell7h7':'',
                   'Cell8h7':'',
                   'Cell9h7':'' }
    horizontal8 = {'Cell1h8':"",
                   'Cell2h8':"",
                   'Cell3h8':'',
                   'Cell4h8':'',
                   'Cell5h8':"",
                   'Cell6h8':'',
                   'Cell7h8':'',
                   'Cell8h8':'',
                   'Cell9h8':'' }
    horizontal9 = {'Cell1h9':"",
                   'Cell2h9':"",
                   'Cell3h9':'',
                   'Cell4h9':'',
                   'Cell5h9':"",
                   'Cell6h9':'',
                   'Cell7h9':'',
                   'Cell8h9':'',
                   'Cell9h9':'' }

    #FirstSquare
    FirstSquareForLoop = ['Cell1h1',
                          'Cell2h1',
                          'Cell3h1',
                          'Cell1h2',
                          'Cell2h2',
                          'Cell3h2',
                          'Cell1h3',
                          'Cell2h3',
                          'Cell3h3' ]
    FirstSquareForLoopDic = [horizontal1,
                             horizontal1,
                             horizontal1,
                             horizontal2,
                             horizontal2,
                             horizontal2,
                             horizontal3,
                             horizontal3,
                             horizontal3]

    for i in range(len(FirstSquareForLoop)):
        FirstSquareForLoopDic[i][FirstSquareForLoop[i]] = random.choice(ListOfNumbers)
        ListOfNumbers.remove(FirstSquareForLoopDic[i][FirstSquareForLoop[i]])

    #Full first Row
    FirstRemove = ['Cell1h1',
                   'Cell2h1',
                   'Cell3h1']
    FirstRow= ['Cell4h1',
               'Cell5h1',
               'Cell6h1',
               'Cell7h1',
               'Cell8h1',
               'Cell9h1']
    ListOfNumbers = [1,2,3,4,5,6,7,8,9]
    for i in range(len(FirstRemove)):
        ListOfNumbers.remove(horizontal1[FirstRemove[i]])
    for i in range(len(FirstRow)):
        horizontal1[FirstRow[i]] = random.choice(ListOfNumbers)
        ListOfNumbers.remove(horizontal1[FirstRow[i]])

    #Second Full row

    SecondRemove = ['Cell1h2',
                    'Cell2h2',
                    'Cell3h2',]
    SecondRemovedisc = [horizontal2,
                        horizontal2,
                        horizontal2,]
    SecondRow = ['Cell4h2',
                 'Cell5h2',
                 'Cell6h2',
                 'Cell7h2',
                 'Cell8h2',
                 'Cell9h2']
    SecondSquareFirstRow = ['Cell4h1','Cell5h1','Cell6h1']
    ThirdSquareFirstRow = ['Cell7h1','Cell8h1', 'Cell9h1']
    SecondSquareFirstRowDisc = [horizontal1, horizontal1, horizontal1]
    for i in range(len(SecondRow)):
        ListOfNumbers = [1,2,3,4,5,6,7,8,9]
        if i <= 3:
            for x in range(len(SecondSquareFirstRow)):
                value = SecondSquareFirstRowDisc[x][SecondSquareFirstRow[x]]
                if value in ListOfNumbers:
                    ListOfNumbers.remove(value)
        if i > 3:
            for x in range(len(ThirdSquareFirstRow)):
                value = SecondSquareFirstRowDisc[x][ThirdSquareFirstRow[x]]
                if value in ListOfNumbers:
                    ListOfNumbers.remove(value)
        for x in range(len(SecondRemove)):
            value = SecondRemovedisc[x][SecondRemove[x]]
            if value in ListOfNumbers:
                ListOfNumbers.remove(value)
        horizontal2[SecondRow[i]] = random.choice(ListOfNumbers)
        SecondRemovedisc.append(horizontal2)
        SecondRemove.append(SecondRow[i])

        # Third FUll row
        SecondRemove = ['Cell1h3',
                        'Cell2h3',
                        'Cell3h3', ]
        SecondRemovedisc = [horizontal3,
                            horizontal3,
                            horizontal3, ]
        ThirdRow = ['Cell4h2',
                     'Cell5h2',
                     'Cell6h2',
                     'Cell7h2',
                     'Cell8h2',
                     'Cell9h2']
        SecondSquare = ['Cell4h1', 'Cell5h1', 'Cell6h1','Cell4h2',"Cell5h2","Cell6h2"]
        ThirdSquare = ['Cell7h1', 'Cell8h1', 'Cell9h1','Cell7h2', 'Cell8h2', 'Cell9h2']
        SecondSquareDisc = [horizontal1, horizontal1, horizontal1, horizontal2, horizontal2, horizontal2]
        for i in range(len(SecondRow)):
            ListOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if i <= 3:
                for x in range(len(SecondSquareFirstRow)):
                    value = SecondSquareDisc[x][SecondSquare[x]]
                    if value in ListOfNumbers:
                        ListOfNumbers.remove(value)
            if i > 3:
                for x in range(len(ThirdSquareFirstRow)):
                    value = SecondSquareDisc[x][ThirdSquare[x]]
                    if value in ListOfNumbers:
                        ListOfNumbers.remove(value)
            for x in range(len(SecondRemove)):
                value = SecondRemovedisc[x][SecondRemove[x]]
                if value in ListOfNumbers:
                    ListOfNumbers.remove(value)
            horizontal3[ThirdRow[i]] = random.choice(ListOfNumbers)
            SecondRemovedisc.append(horizontal3)
            SecondRemove.append(ThirdRow[i])

    #test prints check
    print(ListOfNumbers)
    print(horizontal1)
    print(horizontal2)
    print(horizontal3)
    return render(request, 'blog/sudoku.html')
