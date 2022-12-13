from datetime import date
from bot import Bot  # just has post message

import configparser
import logging
import feedparser
import requests
import logging
import os

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# creating file handler
logpath = "airbot.log"
handler = logging.FileHandler(logpath)
handler.setLevel(logging.INFO)

# creating logging format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", "%d-%m-%Y--%H:%M:%S"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

# ---

TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")

urls = {
    "local": "http://newsonair.nic.in/Regional_Audio_rss.aspx",
    "national": "http://newsonair.nic.in/NSD_Audio_rss.aspx",
}

# utils
def get_config(config_name="config.ini"):
    """returns config preferences from config.toml"""
    config = configparser.ConfigParser()
    config.read(config_name)
    stations = ["national", "local"]
    return {
        station: list(map(lambda x: x.strip(), config["station"][station].split(",")))
        for station in stations
    }


def get_feed_data(url):
    """returns feed parser dictionary"""
    return feedparser.parse(url.strip())


def _format_time(time):
    """input - 1010, output - 10:10"""
    tformat = lambda x: x[:2] + ":" + x[2:]
    if "-" in time:
        split = time.split("-")
        return tformat(split[0]) + "-" + tformat(split[1])
    else:
        return tformat(time)


def construct_message(entry, published, title):
    time = entry.get("bulletintime")
    date_time = published + " " + _format_time(time)
    return """[{}]({})\n\n_{}_""".format(
        title.upper(),
        entry.get("link"),
        date_time,
    )


# ---


def local_news_filter(entry):
    """function to return keys for filtering by preference"""
    title = entry.get("title")
    filter_title = "-".join(title.split("-")[:2]).lower()
    return filter_title


def national_news_filter(entry):
    """function to return keys for filtering by preference"""
    return entry.get("author").lower()


def get_messages_for_posting(feed_data, preference, filter_function):
    """returns messages"""
    entries = feed_data.get("entries")
    messages = list()
    for entry in entries:
        filtrate = filter_function(entry)
        published = entry.get("published")
        if filtrate in preference and published.split(",")[0] == date.today().strftime(
            "%b %d"
        ):
            messages.append(
                construct_message(
                    entry=entry,
                    published=published,
                    title=filtrate,
                )
            )
    return messages


def run(config_name="config.toml"):
    """runs the radio to fetch audio files"""
    config_dict = get_config(config_name)
    local_preference = config_dict.get("local")
    national_preference = config_dict.get("national")
    logger.info(
        "local_preference - {}, national_preference".format(
            local_preference, national_preference
        )
    )

    local_feed_data = get_feed_data(urls["local"]) if local_preference else list()
    national_feed_data = (
        get_feed_data(urls["national"]) if national_preference else list()
    )

    messages = get_messages_for_posting(
        feed_data=local_feed_data,
        preference=local_preference,
        filter_function=local_news_filter,
    )

    messages += get_messages_for_posting(
        feed_data=national_feed_data,
        preference=national_preference,
        filter_function=national_news_filter,
    )

    logger.info("messages - {}".format(messages))
    bot = Bot(token=TOKEN, chat_id=CHANNEL)  # example - @airbotchannel
    for message in messages:
        bot.post_message(message)


if __name__ == "__main__":
    run()
