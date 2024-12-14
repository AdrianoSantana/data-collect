# %%
import requests
from bs4 import BeautifulSoup

def get_content(url):
    cookies = {
        '_ga_DJLCSW50SC': 'GS1.1.1734112190.2.1.1734112278.57.0.0',
        '_ga': 'GA1.2.1487440321.1734107347',
        '_ga_D6NF5QC4QT': 'GS1.1.1734112190.2.1.1734112278.57.0.0',
        '_gid': 'GA1.2.609251158.1734107348',
        '__gads': 'ID=95048d5ff749840b:T=1734107399:RT=1734112191:S=ALNI_MZPLZsVCA98cWGkUMhux-ineon9LA',
        '__gpi': 'UID=00000f7ef9232d5f:T=1734107399:RT=1734112191:S=ALNI_MZ8C8oiDR7cyij0at0sI19qhD5wMA',
        '__eoi': 'ID=f2501897c30a03e1:T=1734107399:RT=1734112191:S=AA-AfjalBlIsYdcg7f3TnAijzW_S',
        '_gat_gtag_UA_29446588_1': '1',
        'FCNEC': '%5B%5B%22AKsRol99MZewI3v0FkdWWoRpk-uK-RUBZFOpvpAbfL7ta0GKbOUzricCIhpcu0kUKjc5QvYly8ApD2RULbrit4PDhWrWUQtSU0oTg5SreQREItGy3d-EjLop_twsqkPYOGL-8S2FmNYf-svdC3Ml64eiOmUaSbFGsQ%3D%3D%22%5D%5D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://www.residentevildatabase.com/personagens/',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga_DJLCSW50SC=GS1.1.1734112190.2.1.1734112278.57.0.0; _ga=GA1.2.1487440321.1734107347; _ga_D6NF5QC4QT=GS1.1.1734112190.2.1.1734112278.57.0.0; _gid=GA1.2.609251158.1734107348; __gads=ID=95048d5ff749840b:T=1734107399:RT=1734112191:S=ALNI_MZPLZsVCA98cWGkUMhux-ineon9LA; __gpi=UID=00000f7ef9232d5f:T=1734107399:RT=1734112191:S=ALNI_MZ8C8oiDR7cyij0at0sI19qhD5wMA; __eoi=ID=f2501897c30a03e1:T=1734107399:RT=1734112191:S=AA-AfjalBlIsYdcg7f3TnAijzW_S; _gat_gtag_UA_29446588_1=1; FCNEC=%5B%5B%22AKsRol99MZewI3v0FkdWWoRpk-uK-RUBZFOpvpAbfL7ta0GKbOUzricCIhpcu0kUKjc5QvYly8ApD2RULbrit4PDhWrWUQtSU0oTg5SreQREItGy3d-EjLop_twsqkPYOGL-8S2FmNYf-svdC3Ml64eiOmUaSbFGsQ%3D%3D%22%5D%5D',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get(url, cookies=cookies, headers=headers)
    print(f'Response status code ${response.status_code} to request ${url}')

    return response

def get_basic_info(soup):
    content_div = soup.find('div', class_="td-page-content")
    character_data_raw = content_div.find_all('p')[1]
    character_data_raw = character_data_raw.find_all('em')
    character_data = {}
    for i in character_data_raw:
        key, value = i.text.split(':')
        character_data[key.strip()] = value.strip()

    return character_data

def get_series_participations(soup):
    content_div = soup.find('div', class_="td-page-content")
    title_block = content_div.find_all('ul')
    title_list = title_block[0]
    print(title_list)
    for title in title_list:
        print(title)
        title_text = 'a'
        print(title_text)
# %%
url = 'https://www.residentevildatabase.com/personagens/ada-wong/'
response = get_content(url)
if response.status_code != 200:
    error_message = f'Error to get data from {url} - status code: {response.status_code}'
    raise Exception(error_message)

soup = BeautifulSoup(response.text)
info = get_basic_info(soup)

get_series_participations(soup)
# %%