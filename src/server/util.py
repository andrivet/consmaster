#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import getopt

from database import *

def usage():
    print('usage: {} --nick <nickname> --pass <password>'.format(__file__))

if __name__ == '__main__':
    " permet d'ajouter simplement un super-user en local "

    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["nick=", "pass="])
    except getopt.GetoptError as err:
        print(err, file=sys.stderr)
        usage()
        sys.exit(2)

    nick, pwd = None, None
    for o, a in opts:
        if o == "--nick":
            nick = a
        elif o == "--pass":
            pwd = a
        else:
            print("Option {} inconnue".format(o))
            sys.exit(2)

    if not nick or not pwd:
        usage()
        sys.exit(2)

    session = Session()
    session.add(User(nickname=nick, password=pwd, droit=0, nom=None, prenom=None, email=None))
    session.commit()
    session.close()
