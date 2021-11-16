#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import sys

try:
    from PySide6.QtCore import *
    from PySide6.QtGui import *
    from PySide6.QtWidgets import *
except:
    print ("Error: This program needs PySide6 module.", file=sys.stderr)
    sys.exit(1)

from cm_globals import CM_BDD
from cm_connexion import *
from cm_exercice import ex_loads


def update_bdd():
    raw_exos = get_exercices()
    
    if raw_exos is None: # TODO: prevent if unable to connect to network
        return
        
    # print(raw_exos.keys())
    if raw_exos.keys() - CM_BDD.keys():
        # QMessageBox.information(None, "Info", "De nouveaux exercices sont disponibles.")
        print("De nouveaux exercices sont disponibles.")
        dct = {uid: ex_loads(serialized) for uid, serialized in raw_exos.items() if uid not in CM_BDD}
        CM_BDD.update(dct); # print(dct)
        CM_BDD.sync()
