from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import *


class kappa():

    hunger = 0

    def __init__(self, pos, scale, model, walk, render, hunger, social):
        self.actor = Actor(model, {"walk": walk})
        self.actor.setPos(pos)
        self.actor.setScale(scale)
        self.actor.reparentTo(render)
