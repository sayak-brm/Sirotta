def html_top(title='', lang='en', charset='utf-8', head=''):
    mime_type()
    print("""<!DOCTYPE html>
<html>
    <head lang="{lang}">
        <meta charset="{charset}" />
        <title>{title}</title>
        {head}
    </head>
    <body>""".format(title=title, lang=lang, charset=charset, head=head))

def html_bottom():
    print("""   </body>
</html>""")

def mime_type(t='text/html'):
    print("Content-Type: {}\n\n".format(t))
