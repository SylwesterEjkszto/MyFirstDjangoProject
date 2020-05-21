def dj_bs(request):
    if request.method == "POST":
        website_link = request.POST.get('web_link', None)
        #requests
        url = website_link #url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}#headers
        source=requests.get(url, headers=headers).text # url source
        #bs
        soup = BeautifulSoup(source, 'html.parser')
        h1_val = soup.h1.string #h1 value

        return render(request, 'blog/django-bs.html', {'h1_val':[h1_val,'kupa']})

    return render(request, 'blog/django-bs.html')
# Create your views here.