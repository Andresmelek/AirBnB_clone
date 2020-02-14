#!/usr/bin/python3
"""
Contains the BaseModel class
"""

import uuid
from datetime import datetime

class BaseModel():
    """ defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, val.strftime("%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ prints as string """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        aux = {}
        copy = self.__dict__
        for key, val in copy.items():
            if copy[key] == 'created_at' or copy[key] == 'updated_at':
                aux[key] = val.isoformat()
            else:
                aux[key] = val
        aux['__class__'] = self.__class__.__name__
        return aux