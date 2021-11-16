#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os.path
from collections import namedtuple

from persistent_dict import PersistentDict


HOST, PORT = 'localhost', 9993
#HOST, PORT = 'eliacheff.dyndns.org', 9993


Mode = namedtuple('Mode', ['name', 'src', 'type'])

MODES = [
    Mode("Standard <-> Dotted", '../data/norm-dot.html', '__NDN__'),
    Mode("Expr -> Graphique", '../data/norm-graph.html', '__NG__'),
    Mode("Graphique -> Expr", '../data/graph-norm.html', '__GN__'),
        ]


DATA_DIR = '../data/'

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

CM_DATA = PersistentDict(DATA_DIR + 'cm.dat')
CM_BDD  = PersistentDict(DATA_DIR + 'cm-bdd.dat')

CM_DATA.setdefault('userlist', [])
CM_DATA.setdefault('connexion_params', {'host': HOST, 'port': PORT})

CM_DATA.sync()
# print(CM_DATA)
