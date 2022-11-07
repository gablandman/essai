import numpy as np
import pygame as pg

class Animal:
  def __init__(self,name,height,hp):
    self.hp = hp

  def feed(self):
    self.hp += 1


