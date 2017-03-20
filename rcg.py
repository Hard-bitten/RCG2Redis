#!/usr/bin/env python
# -*- coding: utf-8 -*-
from show import *
from model import *
import string
import os
import redisco
# from model import *

class Prase():
	def __init__(self,name):
		self.filename = os.path.split(name)[1]
		self.fs = open(name,'r+')
		self.showList = []

	def closeRCG(self):
		self.fs.close()

	def save2Redis(self):
		self.model.save()

	def release(self):
		for m in Model.objects.all():
			m.delete()
		for show in show.objects.all():
			show.delete()
		for player in Player.objects.all():
			player.delete()
		for ball in Ball.objects.all():
			Ball.delete()
		for players in Players.objects.all():
			players.delete()
		closeRCG()

	def praseShow(self,line):
		#(show 532 
		#((b) -18.9227 -34 0 0) 
		#((l 1) 0 0x9 -50.1301 -6.4431 0 0 -92.261 83 (v h 180) (s 8000 1 1 127276) (f l 7) (c 0 61 729 0 1 791 12 56 0 0 502)) 
		side = "";
		unum = "";
		type_ = "";
		state = "";
		x = "";
		y = "";
		vx = "";
		vy = "";
		body = "";
		neck = "";
		view_quality = "";
		view_width = "";
		stamina = "";
		effort = "";
		recovery = "";
		stamina_capacity = "";
		focus_side = "";
		focus_unum = "-1";
		kick_count = "";
		dash_count = "";
		turn_count = "";
		catch_count = "";
		move_count = "";
		turn_neck_count = "";
		change_view_count = "";
		say_count = "";
		tackle_count = "";
		pointto_count = "";
		attentionto_count = "";

		(time,buf) = line.split(' (',1) 
		time = time.split(' ',1)[1]     #(show 532 
		if buf[1] is 'b':
			(ball_,buf) = buf.split(') (',1) #((b) -18.9227 -34 0 0)
			ball_ = ball_.split('(b) ',1)[1]
		# print ball
			(ball_x,ball_y,ball_vx,ball_vy)=ball_.split(' ') #-18.9227 -34 0 0
		playerList = []
		players = buf[:-4].split(')) (')
		# print players
		for player in players:
			#(l 1) 0 0x9 -50.1301 -6.4431 0 0 -92.261 83 (v h 180) (s 8000 1 1 127276) (f l 7) (c 0 61 729 0 1 791 12 56 0 0 502
			if buf[1] is 'l' or 'r':
				(side,buf) = player.split(') ',1)
				(side,unum) = side[1:].split(' ')
			(type_,state,x,y,vx,vy,body,neck,buf) = buf.split(' ',8)
			if buf[1] is 'v':
				(view,buf) = buf.split(') (',1)
				(view_quality,view_width) = view[3:].split(' ')
			if buf[0] is 's':
				(stamina,buf) = buf.split(') (',1)
				(stamina,effort,recovery,stamina_capacity) = stamina[2:].split(' ')
			if buf[0] is 'f':
				(focus,buf) = buf.split(') (',1)
				(focus_side,focus_unum) = focus[2:].split(' ')
			# print buf
			if buf[0] is 'c':
				(kick_count,dash_count,turn_count,
				catch_count,move_count,turn_neck_count,
				change_view_count,say_count,tackle_count,
				pointto_count,attentionto_count) = buf[2:].split(' ')
			
			playerList.append(Player.objects.create(
				side = side,
				unum = int(unum),
				type_ = int(type_),
				state = state,
				x = float(x),
				y = float(y),
				vx = float(vx),
				vy = float(vy),
				body = float(body),
				neck = float(neck),
				view_quality = view_quality,
				view_width = int(view_width),
				stamina = float(stamina),
				effort = float(effort),
				recovery = float(recovery),
				stamina_capacity = float(stamina_capacity),
				focus_side = focus_side,
				focus_unum = int(focus_unum),
				kick_count = int(kick_count),
				dash_count = int(dash_count),
				turn_count = int(turn_count),
				catch_count = int(catch_count),
				move_count = int(move_count),
				turn_neck_count = int(turn_neck_count),
				change_view_count = int(change_view_count),
				say_count = int(say_count),
				tackle_count = int(tackle_count),
				pointto_count = int(pointto_count),
				attentionto_count = int(attentionto_count)))
			# print Player.objects.all()
		ball = Ball.objects.create(x=float(ball_x),y=float(ball_y),vx=float(ball_vx),vy=float(ball_vy))
		# playerList = Player.objects.all()
		# print playerList
		# Show.objects.create(time = time,ball = ball,players = [playerList])
		self.showList.append(Show.objects.create(time = int(time),ball =ball,players = playerList))

	def praseline(self,line):
		if cmp(line,'ULG5') is 1:
			return

		name = line.split(' ',1)[0].split('(')[1]

		if cmp(name,'show') is 0:
			print name
			show_ = self.praseShow(line)
			return
		else:
			return

	def prase(self):
		for line in self.fs.readlines():
			self.praseline(line)
		model = Model(filename = self.filename,show = self.showList)
		model.save()


if __name__=='__main__':
	redisco.connection_setup(host='localhost',port=6379,db=0)
	prase = Prase("./201703122259_32094.rcg")
	prase.prase()
	# prase.save2Redis()
	# prase.release()