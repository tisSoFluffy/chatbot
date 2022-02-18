import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from chat_functions import *

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN")#,
    #signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))
    )

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    #say(f"Hey there <@{message['user']}>!")
    #res = chatbot_response(msg)
    say('Hi there, how may I be of assistance?')

@app.command('/hello-socket-mode')
def hello_command(ack, body):
    user_id = body['user_id']
    ack(f'Hi, <@{user_id}>!')

@app.event('app_mention')
def event_test(body,logger):
    say(logger.info(body))
    res = chatbot_response(message)
    say(res)

# Start your app
if __name__ == "__main__":
    #app.start(port=int(os.environ.get("PORT", 3000)))
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()