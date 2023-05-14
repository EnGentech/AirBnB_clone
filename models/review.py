#!/usr/bin/python3
"""MODULE 9: MORE CLASSES!"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""Adds Review class that inherits from BaseModel. This is user's info"""
	place_id = " "
	user_id = " "
	text = " "
