

from .gmx import Gmx

def login(username, password):
    gmx = Gmx()
    gmx.login(username, password)
    return gmx

def authenticate(username, access_token):
    gmx = Gmx()
    gmx.authenticate(username, access_token)
    return gmx
