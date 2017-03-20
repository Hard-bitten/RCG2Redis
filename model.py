#!/usr/bin/env python
# -*- coding: utf-8 -*-
from show import *
from redisco import models

class Model(models.Model):
	filename = models.Attribute(required = True)
	show = models.ListField(Show)