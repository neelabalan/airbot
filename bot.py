import requests


class Bot:
    def __init__(self, chat_id, token):
        self.method = ""
        self.base_url = "https://api.telegram.org/bot{}".format(token)
        self.chat_id = chat_id

    def post_message(
        self,
        text,
    ):
        """posts a message to the bot"""
        response = requests.post(
            url=self.base_url + "/" + "sendMessage",
            data=dict(chat_id=self.chat_id, text=text, parse_mode="Markdown"),
        )
