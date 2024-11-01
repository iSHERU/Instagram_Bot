import requests
from bs4 import BeautifulSoup


def hash_list():
    keyword = 'furniture' # Please enter the niche for which hashtags are needed without any spaces or special characters

    hashtag_list = []

    # Send a GET request to the page
    response = requests.get(f'https://best-hashtags.com/hashtag/{keyword}/')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        hashtags_list = soup.find('ul', class_='list-unstyled save-job')

        if hashtags_list:
            hashtags = hashtags_list.find_all('a')
            for tag in hashtags:
                hashtag_list.append(tag.text[1:])

            return hashtag_list

        else:
            print('Hashtags list not found.')
    else:
        print(f'Error: {response.status_code}')
