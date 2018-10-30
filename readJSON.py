#! /usr/bin/env python3
# coding: utf-8

import json
import os
import path

def jsonToDictionary():
    """Open a json file and set its datas in a dictionary"""

    #We set the path where we'll get the title screen image
    directory = os.path.dirname(__file__)
    filePath = os.path.join(directory, "conf.json")

    #We open the json file
    jsonFile = open(filePath)
    data = json.load(jsonFile)
    data["title_screen_path"] = path.setTitleScreenPath("title_screen.png")

    return data