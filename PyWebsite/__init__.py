import pyhtml
import pyjavascript
import pycss
from pyhtml import tags

class TagObject:
    def __init__(self, tag: tags.ClosableTags | tags.UnclosableTags):
        self.events = {}
        self.js_script = ""
        
        self.code = tag.code
        
        self.getElementByID = f'document.getElementByID("{tag.id}")'
        self.getElementByClass = f'document.getElementByID("{tag.cls}")'
        
        self.style = tag.style
        self.properties = tag.properties
        self.tag_name = tag.tag_name
        self.css_script = ''
        
    def decorate(self, type: str='class', style: dict={}, addition: str=''):
        __style_property = ''
        for i in list(style.items()):
            __style_property += f'\n\t{i[0]}: {i[1]};'
        self.css_script += f'.{self.properties['class']}{addition} ' + '{' + __style_property + '\n}\n' if type == 'class' else f'#{self.properties['id']} ' + '{' + __style_property + '\n}\n'
        
        f'.{self.properties['class']} ' + '{' + __style_property + '\n}\n' if type == 'class' else f'#{self.properties['id']} ' + '{' + __style_property + '\n}\n'
    def add_event(self, event_name, action, start: str="function() "):
        __event_script = {}
        __event_script['on'+event_name] = '' if 'on' + event_name not in __event_script else __event_script['on'+event_name]
        self.events['on'+event_name] = [action] if 'on' + event_name not in self.events else self.events['on'+event_name].append(action+';')
        # for i in list(self.events.values()):
        __event_script['on'+event_name] += f'\n\t{str(self.events['on'+event_name])[2:-2]}'
        # for i in list(self.events.keys()):
        self.js_script += f'{self.getElementByID}.{'on'+event_name} = {start} ' + '{' + __event_script['on'+event_name] + '\n}\n'
            
        return f'{self.getElementByID}.{'on'+event_name} = {start}' + '{' + __event_script['on'+event_name] + '\n}\n'
        
    def add_event_listener(self, event_name, type: str='mouse', key: str='This parameter needs only when type is "key"'):
        if type == 'key':
            def wrapper(func):
                script = func()
                self.add_event(event_name, script, start=f"({key}) => ")
                return script
            return wrapper
        else:
            def wrapper(func):
                script = func()
                self.add_event(event_name, script)
                return script
            return wrapper
        
    def add_style(self, type: str, addition: str=""):
        def wrapper(func):
            style = func()
            self.decorate(type, style, addition)
            
        return wrapper
    
    def add_to(self, app, type="html"):
        if type.lower() == "html":
            app.add(self.code)
            
        elif type.lower() == "css":
            app.add(self.css_script)
            
        elif type.lower() == 'javascript' or type.lower() == 'js':
            app.add(self.js_script)
        