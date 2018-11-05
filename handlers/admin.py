from tornado.gen import coroutine
from tornado.web import RequestHandler
from tornado_sqlalchemy import as_future, make_session_factory, SessionMixin
from sqlalchemy import desc

from models.word import Word
from utils.crypto import decrypt_data, encrypt_data, get_keys

class AdminHandler(SessionMixin, RequestHandler):
    @coroutine
    def get(self):
        private_key = get_keys("private_key")
        words = []
        with self.make_session() as session:
            # Fetch all the words from the table in order of their frequency and return 
            # to the front end 
            word_array = yield as_future(session.query(Word).order_by(desc(Word.count)).all)
            for word_obj in word_array:
                word = {}
                word["count"] = word_obj.count
                # Decrypt the key before sending back to front end
                word["word"] = decrypt_data(word_obj.word, private_key)
                words.append(word)
        self.render("admin.html", words = words)
