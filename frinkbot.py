from flask import Flask
from flask_slack import Slack
import settings
from lib.utils import parse_command_text
from lib.frinkiac import make_meme

app = Flask(__name__)
slack = Slack(app)

app.add_url_rule('/slack', view_func=slack.dispatch)


@app.route('/')
def index():
    return 'HOYVIN-GLAVIN!'


@slack.command(command=settings.SLACK_COMMAND, token=settings.SLACK_COMMAND_TOKEN,
               team_id=settings.SLACK_TEAM_ID, methods=['POST'])
def slash_frink(**kwargs):
    try:
        meme_url = make_meme(*parse_command_text(kwargs.get('text')))
        if meme_url:
            return slack.response('', attachments=[{
                'fallback': 'HOYVIN-GLAVIN!',
                'image_url': meme_url
            }], response_type='in_channel')
        else:
            return slack.response('Nothing found! Oh, for flavin out loud.', response_type='ephemeral')
    except:
        return slack.response('Something exploded! Oh, for flavin out loud.', response_type='ephemeral')


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
