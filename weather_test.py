#!/home/ece-student/anaconda3/bin/python
#chmod 755 splitargs
# -*- coding: utf-8 -*-


# Created by: Pat Rick Ntwari
# Homework 1, EC500


# Converting numbers from arabic to roman numerals

import pytest
import weather

def cityTest():
    assert weather.cityCall("Montreal,CA") == "Found"

