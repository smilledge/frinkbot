import re


def parse_command_text(text):
    """
    Parse the message text from Slack.

    This extracts the search query and the caption.

    Example commands (the "/frink" won't be included):
     - /frink do'h
     - /frink don't you hate pants?
     - /frink nothing at all "Feels like I'm wearing nothing at all"
     - /frink nothing at all "Nothing at all. | Nothing at all. | Nothing at all."

    :param text:
    :return:
    """
    try:
        caption = re.findall(r'"([^"]*)"', text)[0]
    except Exception, e:
        caption = None

    try:
        # Index will raise an exception in the string does not exist
        if caption and caption.index('|'):
            caption = '\n'.join([s.strip() for s in caption.split('|')])
    except Exception, e:
        # If the user has not set the line breaks, make sure lines at 25 chars max
        # Frinkiac seems to use two different text sizes. I don't know why?
        caption = wrap_text(caption, 25)

    try:
        query = text[:text.index('"')].strip()
    except ValueError, e:
        query = text.strip()

    return (query, caption)


def wrap_text(text, max_length):
    """
    Wrap text at the max line length

    Source: http://stackoverflow.com/a/32122312/499631

    :param text: String of text
    :param max_length: Maximum characters on a line
    :return:
    """
    words = iter(text.split())
    lines, current = [], next(words)
    for word in words:
        if len(current) + 1 + len(word) > max_length:
            lines.append(current)
            current = word
        else:
            current += ' ' + word
    lines.append(current)
    return '\n'.join(lines)
