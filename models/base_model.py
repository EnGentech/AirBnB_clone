#!/usr/bin/env python3
from datetime import datetime
import uuid
# This program defines the command line
# interpreter for the AirBnB project
# Written by EnGentech and Chime


class BaseModel:
    """BaseModel class defined here"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __int__(self, *args, **kwargs):
        """An instantiation of the Base Model"""
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """String instantiation of the BaseModel"""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """Updating time and date at the point of saving"""
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """Redefining dictionary"""
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": __class__.__name__,
            "created_at": str(self.created_at.isoformat()),
            "updated_at": str(self.updated_at.isoformat())
            })
        return my_dict
