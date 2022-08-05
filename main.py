from flask import Flask
import random

random_num = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1 style='text-align: center;'>Welcome to the Higher or Lower Game!</h1>" \
           "<br>" \
           "<h2 style='text-align: center;'>Please guess a number between 0 and 9</h2>" \
           "<br>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif' width=300>"


@app.route("/<int:user_num>")
def guess(user_num):
    if user_num == random_num:
        return "<h1 style='color: Green; text-align: center;'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/cXaeWuJ1oKO4g/giphy.gif' width=300>"

    if user_num < random_num:
        return "<h1 style='color: Green; text-align: center;'>Oh No! Too Low!</h1>" \
               "<img src='https://media.giphy.com/media/iooQZVpXDz88U/giphy.gif' width=300>"

    if user_num > random_num:
        return "<h1 style='color: Red; text-align: center;'>Uh Oh! Too High!</h1>" \
               "<img src='https://media.giphy.com/media/3OhXBaoR1tVPW/giphy.gif' width=300>"


if __name__ == "__main__":
    app.run()
