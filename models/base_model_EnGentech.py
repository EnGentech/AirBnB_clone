#!/usr/bin/env python3
# Written by EnGentech and Chime
from datetime import datetime
import uuid
"""This program defines the console/command line
	interpreter for the AirBnB project
"""

class BaseModel:
    """
	BaseModel class defines the  attributes and methods
	to be inherited by childclasses and instances

<<<<<<< HEAD
class BaseModel:
    """BaseModel class defined here"""
    global for_mat
    for_mat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """created the instantiation stage"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key_num, value_val in kwargs.items():
                if key_num != "__class__":
                    if key_num in ["created_at", "updated_at"]:
                        value_val = datetime.strptime(value_val, for_mat)
                    setattr(self, key_num, value_val)

=======
	@args:
		`id`: assigns a universally unique identity for every Basemodel object
		`created_at`: this assigns the current time of creation for every
					object or child class of BaseModel
		`updated_at`: this initially takes same value as `created_at` and 
					keeps track of the time of any update on attributes
	"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __int__(self, *args, **kwargs):
        """
		An instantiation of the Base Model

		@args:
			`args`: takes variable number of argument
			`kwargs`: takes a key-value pair of argument in the form of a dict
        """
        #self.id = id 
        #self.created_at = created_at
        #self.updated_at = updated_at
        """line 33-35 since we have defined the above below, i think it's duplicity without effects"""
        if not kwargs or len(kwargs) < 1:
		# kwargs can exist && be empty; with < 1 we are checking
		#+ both non-existence and emptiness
            self.id = id
            self.created_at = created_at
            self.updated_at = updated_at
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == ["created_at", "updated_at"]:
			        #Need explanation. Was thinking `in` should be used or
					#+ if key == "created_at" or key == "updated_at"
                        value = datetime.strftime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    elif key == "id": # I added this line
                        self.id = value #+ so that kwargs id can override
										#+ default id
                setattr(self, key, value)
>>>>>>> 71d49abf209610f64fd32a8eff294fafb0dcaed1
    def __str__(self):
        """String representation of the BaseModel
		`cls_name` is a variable that stores the name of our current class
			It's content is the class name of the instance class or object.
		`return`: it returns a printable format like this: 
				[<class name>] (<self.id>) <self.__dict__>
		"""
        cls_name = self.__class__.__name__ 
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """
		Updating time and date at the point of saving
		When this method is called, current datetime is 
			assigned to `updated_at'
		`return`: returns the time that last call to save method occurred
		"""
        self.updated_at = datetime.now()
        return self.updated_at

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
