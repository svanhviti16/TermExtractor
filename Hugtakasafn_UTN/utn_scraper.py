import requests
website_url = requests.get('http://www.hugtakasafn.utn.stjr.is/leit-nidurstodur.adp?leitarord=_&tungumal=oll&ordrett=o').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url, "html.parser")

icelandic_terms = []
# finds all icelandic terms
content = soup.find_all('div',{'class':'term'})
for content_item in content:
    icelandic_terms.append(content_item.find_next('dt').findAll('a'))

terms = []

for i in content:
    terms.append(i.text)

# a list of lists
term_lists = []

for term in terms:
    term_lists.append(term.split("\n"))

for t in term_lists:
    print(t[1])