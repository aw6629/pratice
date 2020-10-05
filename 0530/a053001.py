def get_stroke(s):
    import requests
    from bs4 import BeautifulSoup
    r=requests.get('https://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint='+s)
    soup=BeautifulSoup(r.content,'html.parser')
    naviStr=soup.find(text='kTotalStrokes')
    next_td=naviStr.find_next('td')
    return int(next_td.find('code').text)

l=['王','林','陳']
l.sort(key=get_stroke)
print(l)