import requests
from lxml import html
headers = {'User-Agent': 'Mozilla/5.0'}

def getNews(countryCode):
    url = optionsNameLink[int(countryCode)-1][2]
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        news = []
        xpathAll = '/html/body/div[3]/div[6]/div[1]/div[2]/div[2]/div'
        newsSize = tree.xpath(xpathAll)
        for i in range(1,len(newsSize)+1):
            time = tree.xpath(xpathAll+'['+str(i)+']/div[1]/span')
            title = tree.xpath(xpathAll+'['+str(i)+']/div[2]')
            link = tree.xpath(xpathAll+'['+str(i)+']/div[1]/div/a/@href')
            news.append('[\033[32m' + time[0].text_content() + '\033[0m]\n\n' + title[0].text_content() + '\n\n\033[34m' + link[0] + '\033[0m')
        for i in range(0,len(newsSize)):    
            print('\n#################\n\n'+news[i])
    else:
        print(f'Error: {response.status_code}')
        
def showOptions():
    global optionsNameLink
    urlOptions = 'https://liveuamap.com'
    responseOptions = requests.get(urlOptions, headers=headers)
    if responseOptions.status_code == 200:
        tree = html.fromstring(responseOptions.content)
        options = []
        xpathAll = '/html/body/div[3]/div[3]/div/div'
        optionsSize = tree.xpath(xpathAll)
        for i in range(2,len(optionsSize)+1):
            countryRow = tree.xpath(xpathAll+'['+str(i)+']/div')
            for j in range(1,len(countryRow)+1):
                name = tree.xpath(xpathAll+'['+str(i)+']/div['+str(j)+']/a[2]/span')
                link = tree.xpath(xpathAll+'['+str(i)+']/div['+str(j)+']/a[2]/@href')
                if '#' not in link:
                    optionsNameLink.append((len(optionsNameLink)+1,name[0].text_content(),link[0]))
    else:
        print(f'Error: {responseOptions.status_code}')

    for name in optionsNameLink:
        print(str(name[0])+') '+name[1])
        
optionsNameLink = []
showOptions()
countryCode = input("\nPlease choose a country: ")
getNews(countryCode)

