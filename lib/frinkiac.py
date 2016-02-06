import urllib
import random
import requests


FRINKIAC_URL = 'https://frinkiac.com'
USER_AGENT = 'FRINKBOT 5000'


def make_meme(query, caption):
    episode, timestamp = get_frame(query)
    if not caption:
        caption = get_caption(episode, timestamp)
    return get_meme_url(episode, timestamp, caption)


def get_frame(query):
    """
    Search Frinkiac and return a random frame

    :param query: Search query string
    :return: episode, timestamp
    """
    print get_search_url(query)
    r = requests.get(get_search_url(query), headers={
        'User-Agent': USER_AGENT
    })
    if not r.ok:
        raise ValueError('Invalid search query')
    results = r.json()
    frame = random.choice(results)
    return (frame['Episode'], frame['Timestamp'])


def get_caption(episode, timestamp):
    """
    Get the caption for a frame

    (May need to handle wrapping text here, but not sure yet)

    :param episode:
    :param timestamp:
    :return:
    """
    r = requests.get(get_caption_url(episode, timestamp), headers={
        'User-Agent': USER_AGENT
    })
    if not r.ok:
        return None
    try:
        result = r.json()
        return '\n'.join([subtitle['Content'] for subtitle in result['Subtitles']])
    except:
        return None


def get_search_url(query):
    """
    Get the Frinkiac API search URL

    :param query:
    :return:
    """
    return '%s/api/search?q=%s' % (FRINKIAC_URL, urllib.quote(query))


def get_caption_url(episode, timestamp):
    """
    Get the caption URL for a Frinkiac meme

    :param episode:
    :param timestamp:
    :param caption:
    :return:
    """
    return '%s/caption?e=%s&t=%s' % (FRINKIAC_URL, episode, timestamp)


def get_meme_url(episode, timestamp, caption):
    """
    Get the image URL for a Frinkiac meme

    :param episode:
    :param timestamp:
    :param caption:
    :return:
    """
    if caption:
        caption = urllib.quote(caption)
        return '%s/meme/%s/%s.jpg?lines=%s' % (FRINKIAC_URL, episode, timestamp, caption)
    else:
        return '%s/meme/%s/%s.jpg' % (FRINKIAC_URL, episode, timestamp)
