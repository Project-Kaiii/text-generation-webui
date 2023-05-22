from threading import Thread
from extensions.telegram_bot.TelegramBotWrapper import TelegramBotWrapper



def run_server():
    # create TelegramBotWrapper instance
    # by default, read parameters in telegram_config.cfg
    tg_server = TelegramBotWrapper(
        config_file_path="extensions/telegram_bot/telegram_config.cfg")
    # by default - read token from extensions/telegram_bot/telegram_token.txt
    tg_server.html_tag = ['<pre language="c++">', "</pre>"]
    tg_server.html_tag = ["", ""]
    tg_server.run_telegram_bot()


def setup():
    Thread(target=run_server, daemon=True).start()
