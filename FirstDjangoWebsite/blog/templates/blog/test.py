### sprawdzanie ilości podstron #######
if request.method == "POST":
    strona = 1
    citi = request.POST.get('citi', None)
    first_url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/' + citi + "/?page=" + str(strona)
    first_page = requests.get(first_url)
    first_soup = BeautifulSoup(first_page.content, 'html.parser')
    auction_link = []
    page_number = []
    auction = []
    for a in first_soup.find_all('a', class_="block br3 brc8 large tdnone lheight24"):
        page_number.append(a)
    page_number.append(1)

##### skan właściwy linków #########

    for i in range(len(page_number)):
        strona += 1
        url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/' + city + "/?page=" + str(strona)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for a in soup.find_all('a',class_="marginright5 link linkWithHash detailsLinkPromoted", href=True):
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
        #auction_surface = auction_soup.find("td", class_="value")
        auction[i].append(str(i))
        auction[i].append(str(auction_name.text))

        if "not-arranged" in auction_price:
            auction_final_price = auction_price[66:72]
            auction[i].append(auction_final_price)

        elif "css-1vr19r7" in auction_price:
            auction_final_price = auction_price[25:31]
            auction[i].append(auction_final_price)

        else:
            auction_final_price = auction_price[62:70]
            auction[i].append(auction_final_price)

        #auction[i].append("cena:" + str(auction_price))
        auction[i].append(str(auction_url))
        #auction[i].append("powierzchnia:" + str(auction_surface.text))
        print(i)

    for i in range(len(auction)):
        auction[i] = [s.strip("\n") for s in auction[i]]

    h1_val = auction[]