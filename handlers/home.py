import os

from tornado.gen import coroutine
from tornado.web import RequestHandler
from tornado_sqlalchemy import as_future, make_session_factory, SessionMixin
from tornado.escape import json_encode

from models.word import Word
from utils.crawler import build_word_dict
from utils.crypto import decrypt_data,encrypt_data,get_keys
from utils.hashing import get_salted_hash

class HomeHandler(SessionMixin, RequestHandler):
    def get(self):
        with self.make_session() as session:
            count = session.query(Word).count()
        self.render("base.html", word_array=None)

    @coroutine
    def post(self):
        url = self.get_argument('url')
        # Fetch word dictionary with frequency
        word_dict = build_word_dict(url)
        # Get public key
        public_key = get_keys("public_key")
        new_dict_array = []
        with self.make_session() as session:
            # Iterate through all the word in the word_dict , create the word hash and
            # check if a word hash exists in the database
            for word, quantity in word_dict:
                new_dict = { 'text' : word, 'size' : quantity }
                new_dict_array.append(new_dict)
                salted_hash = get_salted_hash(word)
                word_element = yield as_future(session.query(Word).filter(Word.word_hash == salted_hash).first)
                if not word_element:
                    # Create a word object and add to session
                    encrypted_word = encrypt_data(word, public_key)
                    session.add(Word(word_hash=salted_hash, word=encrypted_word, count=quantity))
                else:
                    # update the word object with the frequency
                   word_element.count += quantity
                session.commit()
        self.render("base.html", word_array=json_encode(new_dict_array))


