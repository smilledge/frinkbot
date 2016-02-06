Frinkbot
========

Frinkbot is a slash command that posts memes to your Slack channels from https://frinkiac.com/.

## Usage

### Post a frame

This will post a random frame from the search results, and the default caption (if there is one).

```
/frink nothing at all
```

### Custom captions

You can override the caption by adding your own text in quotation marks at the end of the command.

```
/frink nothing at all "Feels like I'm wearing nothing at all!"
```

### Force line breaks

By default captions will be automatically wrapped to ensure they fit within the image. If you would like to manually control line breaks you can use the pipe character ("|") within your caption to set where line breaks should occur.

```
/frink nothing at all "Nothing at all... | Nothing at all... | Nothing at all..."
```

## Install

### Setup Frinkbot server

```
git clone https://github.com/smilledge/frinkbot.git
pip install -r requirements.txt
cp .env.example .env
python frinkbot.py
```
Obviously you should be using virtualenv here. There are also some useful config files in the `contrib` folder for setting up a production instance with Nginx / Supervisord / Gunicorn.

#### Configuration

You can set the following option in your `.env` file:

 - `HOST`, `PORT`, `DEBUG`: Self explanatory; all are optional.
 - `SLACK_COMMAND`: The Slack command you will be using (without the preceding "/") (defaults to "frink")
 - `SLACK_TEAM_ID`: Your Slack team ID (not team name). You can find it here here https://api.slack.com/methods/auth.test/test.
 - `SLACK_COMMAND_TOKEN`: Token for your Slack slash command, you will get this when you create the command (see below).

### Setup Slack slash command

1. Go to https://my.slack.com/services/new/slash-commands and add a new slash command. (If you choose something other than "/frink" you will need to update `SLACK_COMMAND` in your `.env` file)
2. URL should be set to `http://{your hostname}/slack`
3. Copy the value of the "Token" field and update `SLACK_COMMAND_TOKEN` in your `.env` file.
4. Set the username and image fields to whatever you like.
5. Restart the Frinkbot server and you're good to go!