# from pycss import PyCSS
# from pyjavascript import PyJavascript

def filter(contents):
    contents = str(contents)
    contents = contents.replace('/line-change', '<br>')
    contents = contents.replace('/lc', '<br>')
    return contents

version = '0.0.1'
print(f"pyhtml version {version}")

class PyHTML:
    def __init__(self, filename="index.html", lang="en", title="Document"):
        self.filename = filename
        self.lang = f'"{lang}"'
        self.title = title
        self.body = ""
        self.__code = f'<!DOCTYPE html>\n<html lang={str(self.lang)}>\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>{self.title}</title>\n</head>\n<body>\n{self.body}\n</body>\n</html>'
        file = open(filename, mode="w+")
        file.write(self.__code)
        file.close()
        print('텍스트 사이에 /line-change: <br>이다.')
        # self.tags = Tags()
    
    def update(self, filename="index.html", lang='"en"', title="Document"):
        self.__code = f'<!DOCTYPE html>\n<html lang={str(self.lang)}>\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>{self.title}</title>\n</head>\n<body>\n{self.body}\n</body>\n</html>'
        file = open(filename, mode="w+")
        file.write(self.__code)
        file.close()
        
    @property
    def code(self):
        return self.__code
    
    def add(self, contents, line_change: bool=True):
        self.body += f"\n" if line_change else f""
        self.contents = str(contents)
        self.contents = self.contents.split('\n')
        for i in self.contents:
            i = i.split('\n')
            for j in i:
                self.body += f"\t{j}\n"
        self.update(filename=self.filename, lang=self.lang, title=self.title)

class tags:
    def __init__(self):
        '''Tags.'''
        pass
    
    class link:
        def __init__(self, rel="stylesheet", href="style.css", app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.rel = rel
            self.href = href
            self.cls = cls
            self.id = id
            self.code = f'<link rel="{self.rel}" href="{self.href}" cls="{self.cls}" id="{self.id}">'
            
            if add_to_app:
                app.add(self.code)
            # return self.main
        
        def add_to_app(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
    
    class H1:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = str(contents)
            self.cls = str(cls)
            self.id = str(id)
            
            self.contents = self.contents.replace('/line-change', '<br>')
            self.contents = self.contents.replace('/lc', '<br>')
            self.code = f'<h1 class="{self.cls}" id="{self.id}">{self.contents}</h1>'
            
            if add_to_app:
                app.add(self.code)
            # return self.main
        
        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
            
    class H2:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = str(contents)
            self.cls = str(cls)
            self.id = str(id)
            
            self.contents = self.contents.replace('/line-change', '<br>')
            self.contents = self.contents.replace('/lc', '<br>')
            self.code = f'<h2 class="{self.cls}" id="{self.id}">{self.contents}</h2>'
            
            if add_to_app:
                app.add(self.code)
            # return self.main

        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
                
    class H3:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = str(contents)
            self.cls = str(cls)
            self.id = str(id)
            
            self.contents = self.contents.replace('/line-change', '<br>')
            self.contents = self.contents.replace('/lc', '<br>')
            self.code = f'<h3 class="{self.cls}" id="{self.id}">{self.contents}</h3>'
            
            if add_to_app:
                app.add(self.code)
            # return self.code

        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
        
    class H4:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = str(contents)
            self.cls = str(cls)
            self.id = str(id)
            
            self.contents = self.contents.replace('/line-change', '<br>')
            self.contents = self.contents.replace('/lc', '<br>')
            self.code = f'<h4 class="{self.cls}" id="{self.id}">{self.contents}</h4>'
            
            if add_to_app:
                app.add(self.code)
            return self.code

        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
        
    class H5:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = str(contents)
            self.cls = str(cls)
            self.id = str(id)
            
            self.contents = self.contents.replace('/line-change', '<br>')
            self.contents = self.contents.replace('/lc', '<br>')
            self.code = f'<h5 class="{self.cls}" id="{self.id}">{self.contents}</h5>'
            
            if add_to_app:
                app.add(self.code)
            # return self.code

        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
        
    class H6:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = str(contents)
            self.cls = str(cls)
            self.id = str(id)
            
            self.contents = self.contents.replace('/line-change', '<br>')
            self.contents = self.contents.replace('/lc', '<br>')
            self.code = f'<h6 class="{self.cls}" id="{self.id}">{self.contents}</h6>'
            
            if add_to_app:
                app.add(self.code)
            # return self.code

        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
        
    class Div:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = list(map(str, contents)) if type(contents) == list else [contents]
            self.cls = str(cls)
            self.id = str(id)
            
            for i in range(len(self.contents)):
                self.contents[i] = self.contents[i].replace('/line-change', '<br>')
                self.contents[i] = self.contents[i].replace('/lc', '<br>')
                
            self.__returning_contents = ""
            for i in self.contents:
                i = i.code.split('\n')
                for j in i:
                    self.__returning_contents += f"\t{j}\n"
            
            self.__returning_contents = self.__returning_contents[:len(self.__returning_contents)-1]
            self.code = f'<div class="{self.cls}" id="{self.id}">\n{self.__returning_contents}\n</div>'
            
            if add_to_app:
                app.add(self.code)
            # return self.code

        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
            
    class Form:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", action=None, add_to_app: bool=False):
            self.contents = list(map(str, [i.code for i in contents])) if type(contents) == list else [contents]
            self.cls = str(cls)
            self.id = str(id)
            self.action = str(action)
            
            for i in range(len(self.contents)):
                self.contents[i] = self.contents[i].replace('/line-change', '<br>')
                self.contents[i] = self.contents[i].replace('/lc', '<br>')
                
            self.__returning_contents = ""
            for i in self.contents:
                i = i.split('\n')
                for j in i:
                    self.__returning_contents += f"\t{j}\n"
            
            self.__returning_contents = self.__returning_contents[:len(self.__returning_contents)-1]
            self.code = f'<form class="{self.cls}" id="{self.id}" action="{self.action}">\n{self.__returning_contents}\n</form>'
            
            if add_to_app:
                app.add(self.code)
            # return self.code

        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
        
    class FieldSet:
        def __init__(self, contents, app: PyHTML=None, cls="", id="", add_to_app: bool=False):
            self.contents = list(map(str, [i.code for i in contents])) if type(contents) == list else [contents]
            self.cls = str(cls)
            self.id = str(id)
            
            for i in range(len(self.contents)):
                self.contents[i] = self.contents[i].replace('/line-change', '<br>')
                self.contents[i] = self.contents[i].replace('/lc', '<br>')
                
            self.__returning_contents = ""
            for i in contents:
                i = i.code.split('\n')
                for j in i:
                    self.__returning_contents += f"\t{j}\n"
            
            self.__returning_contents = self.__returning_contents[:len(self.__returning_contents)-1]
            self.code = f'<fieldset class="{self.cls}" id="{self.id}">\n{self.__returning_contents}\n</fieldset>'
            
            if add_to_app:
                app.add(self.code)
            # return self.code
        
        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
        
    class Input:
        def __init__(self, placeholder, app: PyHTML=None, type: str="", cls: str="", id: str="", required: bool=False, add_to_app: bool=False):
            self.placeholder = str(placeholder)
            self.type = str(type)
            self.cls = str(cls)
            self.id = str(id)
            
            if required:
                self.code = f'<input type="{self.type}" class="{self.cls}" id="{self.id}" placeholder="{self.placeholder}" required>'
                
                if add_to_app:
                    app.add(self.code)
                # return self.code
            else:
                self.code = f'<input type="{self.type}" class="{self.cls}" id="{self.id}" placeholder="{self.placeholder}">'
                
                if add_to_app:
                    app.add(self.code)
                # return self.code
        
        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
            
    class ClosableTags:
        def __init__(self, tag_name, contents, app: PyHTML=None, line_change: bool=False, style: dict={}, properties: dict={'class': "", 'id': ""}, add_to_app: bool=False):
            self.tag_name = tag_name
            self.contents = filter(contents)
            
            properties['class'] = "" if not 'class' in properties else properties['class']
            properties['id'] = "" if not 'id' in properties else properties['id']
            self.id, self.cls = properties['id'], properties['class']
            __property_length = len(properties)
            __property_items = list(properties.items())
            __tag_properties = ""
            
            self.style = style
            self.properties = properties
            
            __style_length = len(style)
            __style_items = list(style.items())
            __style_properties = 'style="'
            
            for i in range(__style_length):
                __style_properties += f'{__style_items[i][0]}: {__style_items[i][1]}; '
            __style_properties = __style_properties[:-1:]
            __style_properties += '" '
            
            for i in range(__property_length):
                __tag_properties += f'{__property_items[i][0]}="{__property_items[i][1]}" '
            
            __tag_properties += __style_properties if __style_length != 0 else ""
            __tag_properties = __tag_properties[:-1:]
            
            if (not line_change) and (len(self.contents) == 1):
                self.code = f'<{self.tag_name} {__tag_properties}>{self.contents}</{self.tag_name}>'
            else:
                __returning_contents = ""
                if type(contents) == str:
                    contents = [contents]
                for i in contents:
                    i = i.code.split('\n')
                    for j in i:
                        __returning_contents += f"\t{j}\n"
                __returning_contents = __returning_contents[:len(__returning_contents)-1:]
                self.code = f'<{self.tag_name} {__tag_properties}>\n{__returning_contents}\n</{self.tag_name}>'
                
            if add_to_app:
                app.add(self.code)
            # return self.code
            
        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)
            
    class UnclosableTags:
        def __init__(self, tag_name, app: PyHTML=None, line_change: bool=False, style: dict={}, properties: dict={'class': "", 'id': ""}, add_to_app: bool=False):
            self.tag_name = tag_name
            
            properties['class'] = "" if not 'class' in properties else properties['class']
            properties['id'] = "" if not 'id' in properties else properties['id']
            self.id, self.cls = properties['id'], properties['class']
            __property_length = len(properties)
            __property_items = list(properties.items())
            __tag_properties = ""
            
            self.style = style
            self.properties = properties
            
            __style_length = len(style)
            __style_items = list(style.items())
            __style_properties = 'style="'
            
            for i in range(__style_length):
                __style_properties += f'{__style_items[i][0]}: {__style_items[i][1]}; '
            __style_properties = __style_properties[:-1:]
            __style_properties += '" '
            
            for i in range(__property_length):
                __tag_properties += f'{__property_items[i][0]}="{__property_items[i][1]}" '
            
            __tag_properties += __style_properties if __style_length != 0 else ""
            __tag_properties = __tag_properties[:-1:]
            
            self.code = f'<{self.tag_name} {__tag_properties}>'
            
            if add_to_app:
                app.add(self.code)
            # return self.code
            
        def add_to(self, app: PyHTML, line_change: bool=True):
            app.add(self.code, line_change=line_change)

# class HTMLObject(tags):
    # def __init__(self, closable, tag_name, contents=None, style: dict={}, properties: dict={'class': "", 'id': ""}):
        # super().__init__()
        # if closable:
            # self.main = self.ClosableTags(tag_name, contents, style=style, properties=properties)
            # self.contents = contents
            # 
        # else:
            # self.main = self.UnclosableTags(tag_name, style=style, properties=properties)
        # self.style = style
        # self.properties = properties
        # self.events = {}
        # self.script = ""
        # self.id = properties['id']
        # self.cls = properties['class']
        # self.event_actions = ""
        # 
    # def get_contents(self):
        # return self.contents
    # 
    # def get_styles(self):
        # return self.style
    # 
    # def get_properties(self):
        # return self.properties
    # 
    # def get_script(self):
        # return self.script
    # 
    # def get_code(self):
        # return self.main
    # 
    # def get_this_object(self, type="id"):
        # assert type in ['id', 'class']
        # return f'document.getElementById("{self.id}")' if type == "id" else f'document.getElementByClass("{self.cls}")'
    # 
    # def add_event(self, event_name, action):
        # '''event_name --> click: O, onclick: X'''
        # self.events['on'+event_name] = [action+';'] if 'on' + event_name not in list(self.events.keys()) else self.events['on'+event_name].append(action+';')
        # for i in list(self.events.values()):
            # self.event_actions += f'\n\t{str(i)[2:-2]}'
        # for i in list(self.events.keys()):
            # self.script += f'{self.get_this_object()}.{i} = function() ' + '{' + self.event_actions + '\n}\n'

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
        
# Tags = tags()

# class Color:
#     def __init__(self):
#         pass
    
#     def rgb(r, g, b):
#         return f'rgb({r}, {g}, {b})'
    
#     def hex_color(r, g, b):
#         return f'#{r}{g}{b}'

# Color 클래스는 PyCSS에 들어가야 한다.

class collections:
    def __init__(self):
        pass
    
    class Divs(tags):
        def __new__(self, number: int=3):
            self.contents = []
            for i in range(1, number+1):
                self.contents.append(self.Div([]).code)
                
            self.code = self.Div(self.contents).code
                
            return self.code
        
    class OrderedList(tags):
        def __new__(self, number: int=3):
            self.li = self.ClosableTags('li', []).code
            self.code = self.ClosableTags('ol', [self.li]*number).code
            
            return self.code

    class UnorderedList(tags):
        def __new__(self, number: int=3):
            self.li = self.ClosableTags('li', []).code
            self.code = self.ClosableTags('ul', [self.li]*number).code
            
            return self.code
        
    class Box(tags):
        def __new__(self, width: 100, height: 100, color: str='red', cls: str="box"):
            __div = self.ClosableTags('div', [], properties={'class': cls})
            self.box = TagObject(__div)
            self.html = __div.code
            self.box.decorate(style={'width': f'{width}px', 'height': f'{height}px', 'color': f'"{color}"'})
            self.css = self.box.css_script
            
            return {'HTML': self.html, 'CSS': self.css}
        
    