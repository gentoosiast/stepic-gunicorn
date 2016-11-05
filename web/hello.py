#!/usr/bin/python3
# coding=utf-8

def app(environ, start_response):
    """ WSGI приложение должно возвращать документ с MIME-типом text/plain, содержащий все GET параметры, по одному на каждую строку. """
    data = str(environ['QUERY_STRING']).replace('&', '\n')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
