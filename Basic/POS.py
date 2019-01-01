from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

db = pymysql.connect("localhost", "root", "std123", "pos_rest")

app = Flask(__name__)
CORS(app)


class Pos:
    def __init__(self, word, pos):
        self.word = word
        self.pos = pos

    def __repr__(self):
        return str(self.__dict__)


@app.route('/', methods=['GET'])
def get_ui():
    return 'Pos application'


@app.route('/', methods=['POST'])
def get_split_words():
    values = request.get_json()
    sentence = values['sentence']
    list_word = [Pos(i, '') for i in sentence.split(' ')]
    dict_list_word = [tx.__dict__ for tx in list_word]
    return jsonify(dict_list_word), 200


@app.route('/save', methods=['POST'])
def save_words():
    values = request.get_json()
    #insert data here

    return jsonify(values)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
