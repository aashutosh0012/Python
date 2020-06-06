import bs4,requests,os
os.chdir('path\Downloading All XKCD Comics')

prev=''
while url!='https://xkcd.com/#':
    url='https://xkcd.com'
    url= url + prev
    print(f'Downloading {url}')
    res=requests.get(url)
    res.raise_for_status()
    res=res.text
    soup=bs4.BeautifulSoup(res,'html.parser')
    prev=soup.find('a',rel='prev')['href']
    prev_url='https://xkcd.com' + soup.find('a',rel='prev')['href']
    img_url=soup.find('div',id='comic').find('img')['src']
    img_file=img_url.split('/')[-1]
    img_url = 'https:' + img_url
    print(f'Downloading {img_url}')
    image=requests.get(img_url)
    image.raise_for_status()
    with open(img_file,'wb') as file:
       file.write(image.content)
