#!/usr/bin/python3
""" classs strcutre for BaseModel
for all classes in the project"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """ Creates Base Model Class, which other classes will inherit from """

    def __init__(self, *args, **kwargs):
        """this initalizes the class ~(^-^)~"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            s = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(self.created_at, s)
            self.updated_at = datetime.strptime(self.updated_at, s)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        """returns a string"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """updates the public instance attribute with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returing a dictionary containing all keys/values of __dict__ """
        dict_cpy = self.__dict__.copy()
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        dict_cpy['__class__'] = self.__class__.__name__
        return dict_cpy
