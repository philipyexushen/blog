from lxml import etree

_has_load = False
engine_name = None
database_name = None
user_name = None
password_name = None
host_name = None
port_name = None

def lazy_load():
    global _has_load
    if _has_load:
       return
    et = etree.parse("./myblog/password.xml")
    root = et.getroot()

    global engine_name, database_name, user_name, password_name, host_name, port_name
    engine_name = root.find("ENGINE").text
    database_name = root.find("NAME").text
    user_name = root.find("USER").text
    password_name = root.find("PASSWORD").text
    host_name = root.find("HOST").text
    port_name = root.find("PORT").text

    _has_load = True


def get_password():
    lazy_load()
    return password_name

def get_engine_name():
    lazy_load()
    return engine_name

def get_user_name():
    lazy_load()
    return user_name

def get_database_name():
    lazy_load()
    return database_name

def get_host():
    lazy_load()
    return host_name

def get_port():
    lazy_load()
    return port_name