import urllib2
import pprint
from bs4 import BeautifulSoup


def do_search(query_str):
    proxy_support = urllib2.ProxyHandler({"http": "http://10.15.135.20:8080"})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

    # search_url = "https://www.google.com/search?q=%s" % urllib2.quote(query_str)
    search_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    pprint.pprint(search_url)
    html = urllib2.urlopen(search_url)
    # pprint.pprint(html.read())
    soup = BeautifulSoup(html, 'html5lib')
    info = soup.find('table', attrs={'class': 'infobox vevent'}).find('tbody')

    for child in info.contents:
        for item in child.contents:
            for element in item.contents:
                for e in element.descendants:
                    print(e)
                # if element.name == 'a':
                #     print(element.next_element)
                # if not element.contents:
                #     print(element.text)
        print(" ")
    # pprint.pprint(soup.get_text())
    # pprint.pprint(info)
    # software_info = soup.find('<table>', attrs={'class': 'infobox vevent'})
    # if software_info:
    #     pprint.pprint(software_info.text.strip())
    # else:
    #     pprint.pprint("Not Found!")


if __name__ == '__main__':
    do_search("python")
