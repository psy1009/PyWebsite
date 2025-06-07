import pyhtml, pycss, pyjavascript

app = pyhtml.PyHTML()
style = pycss.PyCSS()

div = pyhtml.tags.ClosableTags('div', [pyhtml.tags.H1('Hello')], properties={'class': 'class', 'id': 'id'})
div = pyhtml.TagObject(div)

h1 = pyhtml.tags.H1('Hello World!').add_to(app)


datalist = pyhtml.tags.ClosableTags('datalist', [pyhtml.tags.ClosableTags('option', i) for i in range(1, 10)])
datalist.add_to(app)

@div.add_style('code')
def div_style():
    return {
        'color': 'blue'
    }

app.add(div.code)
style.add(div.css_script)
