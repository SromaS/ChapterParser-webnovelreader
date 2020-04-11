from bs4 import BeautifulSoup
import requests

url = "https://webnovelreader.org/solo-leveling/chapter-270"

headers_Get = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


def get_html():
    print("Upload HTML manually via a file[1], or via a site request(doesn't always work)?[2]")
    print("Input 1 or 2")
    choice = int(input())
    if choice == 1:
        handle = open("html.txt", "r")
        data = handle.read()
        handle.close()
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
        data = requests.post(url, headers=headers)
    return data


def novell_parser(html_page):
    handle = open("result.txt", 'w')
    try:
        soup = BeautifulSoup(html_page)
    except TypeError:
        print("503 Server Error: Service Temporarily Unavailable")
        print("You can get the content by copying the site's view-source in html.txt")
        return "Error"
    main_class = soup.find('div', {'class': 'chapter-content3'})
    rows = main_class.find_all('p')
    for row in rows:
        text = str(row)
        handle.write(text[3:-4])
        handle.write('\n\n')
    handle.close()


novell_parser(get_html())
