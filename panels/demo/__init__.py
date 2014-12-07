from ..common import modules
from tornado.web import UIModule


class Demo(UIModule):
    _id = 'demo'
    name = 'Demo'
    
    def render(self):
        return self.render_string('./panels/demo/demo.html', _id=_id)

modules['demo'] = Demo