#!/usr/bin/env python
# -*- coding: utf-8 -*-
from redisco import models
class Ball(models.Model):
	x = models.FloatField()
	y = models.FloatField()
	vx = models.FloatField()
	vy = models.FloatField()

class Player(models.Model):
	side = models.Attribute()
	unum = models.IntegerField()
	
	type_ = models.IntegerField()
	state = models.Attribute()
	x = models.FloatField()
	y = models.FloatField()
	vx = models.FloatField()
	vy = models.FloatField()
	body = models.FloatField()
	neck = models.FloatField()
	
	point_x = models.FloatField()
	point_y = models.FloatField()

	view_quality = models.Attribute()
	view_width = models.IntegerField()

	stamina = models.FloatField()
	effort = models.FloatField()
	recovery = models.FloatField()
	stamina_capacity = models.FloatField()

	focus_side = models.Attribute()
	focus_unum = models.IntegerField()

	kick_count = models.IntegerField()
	dash_count = models.IntegerField()
	turn_count = models.IntegerField()
	catch_count = models.IntegerField()
	move_count = models.IntegerField()
	turn_neck_count = models.IntegerField()
	change_view_count = models.IntegerField()
	say_count = models.IntegerField()
	tackle_count = models.IntegerField()
	pointto_count = models.IntegerField()
	attentionto_count = models.IntegerField()


class Show(models.Model):
	time = models.IntegerField(required = True)
	ball = models.ReferenceField(Ball)
	players = models.ListField(Player)
