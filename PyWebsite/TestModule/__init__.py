def make_file(filename):
    new_file = open(file=filename+'.html', mode='w+')
    new_file.write("<h1>This is test module.</h1>")
    new_file.close()
    
print("<h1>This is test module.</h1>")

__version__ = "0.0.1"

class HTMLObject:
    def __init__(self):
        self.main = '<h1>Hello World!</h1>'
        self.events = {}
        
    def get_content(self):
        return self.main
    
    def add_event(self, event_name, action):
        self.events[event_name] = action
        
    def ID(self):
        return '"id"'
        
h1 = HTMLObject()
h1.get_content()
clickCounter = 'function() {\n\
    \tclicks += 1;\n\
    }'
    
class script:
    def __new__(self, object: HTMLObject):
        return f'<script>\n\tdocument.getElementById({object.ID()}).onclick = {object.events['click']}\n</script>'
    
h1.add_event('click', clickCounter)
print(h1.events['click'])
print(script(h1))
