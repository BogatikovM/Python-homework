from urllib.parse import urlparse


def make(url):
    return urlparse(url)

def get_scheme(data):
    return data.scheme

def set_scheme(data, sch):
    return data._replace(scheme = sch)

def get_host(data):
    return data.netloc

def set_host(data, host):
    return data._replace(netloc = host)

def get_path(data):
    return data.path

def set_path(data, pth):
    return data._replace(path = pth)

def to_string(data):
    return data.geturl()

if __name__ == '__main__':
    u = make("https://docs.python.org:80/3/library/urllib.parse.html?""highlight=params#url-parsing")
    u = set_scheme(u, 'http')
    print(to_string(u))
    u = set_path(u, '/404')
    print(to_string(u))
