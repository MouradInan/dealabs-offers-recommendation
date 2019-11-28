from flask import Flask, jsonify
from dealabs import Dealabs


class Deals:

    d = None

    def __init__(self):
        self.d = Dealabs()

    def get_deals(self):
        hot_deals = self.d.get_hot_deals()['data']
        deals_to_show = []
        for deal in hot_deals:
            deals_to_show.append({
                "title": deal["title"],
                "price": deal["price"] if "price" in deal else "NaN",
                "expired": deal["expired"],
                "cat": deal["group_display_summary"]
            })
        return deals_to_show


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/train')
def train():
    d = Deals()
    return jsonify(d.get_deals())


if __name__ == '__main__':
    app.run()
