#!C:/Python3/python

import cgi, cgitb

if __name__ == '__main__':
    try:
        cgitb.enable()
        import main
    except:
        cgi.print_exception()
