from handlers.home import HomeHandler
from handlers.admin import AdminHandler

url_patterns = [
    (r"/", HomeHandler),
    (r"/admin", AdminHandler),
]
