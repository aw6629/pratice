def get_stroke(s):
    import requests
    from bs4 import BeautifulSoup
    lendic={}
    for x in l:
        all_page=requests.get(f'https://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint={x}')
        bs=BeautifulSoup(all_page.text,'html.parser')
        # print(all_page.text)
        tag=bs.find('a',string='kTotalStrokes')
        tag_parent1=tag.find_parent()
        tag_parent2=tag_parent1.find_parent()
        y=tag_parent2.find('code')
        len_str=int(y.text)
        lendic.setdefault(x,len_str)
    return (lendic)


l=['陳','王','林']
l.sort(key=get_stroke)

print(l)