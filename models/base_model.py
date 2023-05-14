#!/usr/bin/env python3
# Written by EnGentech and Chime
from datetime import datetime
import uuid
from models import storage
"""This program defines the console/command line
	interpreter for the AirBnB project
"""

class BaseModel:
    """
	BaseModel class defines the  attributes and methods
	to be inherited by childclasses and instances

	@args:
		`id`: assigns a universally unique identity for every Basemodel object
		`created_at`: this assigns the current time of creation for every
					object or child class of BaseModel
		`updated_at`: this initially takes same value as `created_at` and 
					keeps track of the time of any update on attributes
	"""
    global for_mat
    for_mat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
		An instantiation of the Base Model

		@args:
			`args`: takes variable number of argument
			`kwargs`: takes a key-value pair of argument in the form of a dict
		"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key_num, value_val in kwargs.items():
                if key_num != "__class__":
                    if key_num in ["created_at", "updated_at"]:
                        value_val = datetime.strptime(value_val, for_mat)
                    setattr(self, key_num, value_val)

    def __str__(self):
        """String representation of the BaseModel
		`cls_name` is a variable that stores the name of our current class
			It's content is the class name of the instance class or object.
		`return`: it returns a printable format like this: 
				[<class name>] (<self.id>) <self.__dict__>
		"""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """
		Updating time and date at the point of saving
		When this method is called, current datetime is 
			assigned to `updated_at'
		`return`: returns the time that last call to save method occurred
		"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
		Redefining dictionary
		This method makes a copy of the self.__dict__ of the calling subclass
		Then updates it's own dict without affecting the initial self.__dict__
		@args:
			`__class__`: key with value as class name
			`created_at`: key with isoformat str rep of creation datetime
			`updated_at`: key with isoformat str rep of updation datetime
			`return`: updated dictionary with three added key-value pairs
		"""
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "created_at": str(self.created_at.isoformat()),
            "updated_at": str(self.updated_at.isoformat())
            })
        return my_dict
