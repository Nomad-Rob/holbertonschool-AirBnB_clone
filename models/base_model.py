#!/usr/bin/python3
""" Base model Module for AirBnB clone """

import datetime
import uuid
import models
timestamp = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Creates Base Model, define attributes for project """
    def __init__(self, *args, **kwargs):
        """ is the constructor that initializes base instance """
        if kwargs:
            """constructor that initializes a new instance of the class.
            If kwargs is provided, it iterates over the key-value
            pairs and sets the corresponding attributes of the instance. If the
            key is 'created_at', it converts the value to a datetime object
            using the specified timestamp format. Similarly, if the key is
            'updated_at', it converts the value to a datetime object. If the
            key is not '__class__', it sets the attribute using setattr(). If
            kwargs is empty, it generates a unique id, sets created_at and
            updated_at attributes to the current datetime, and adds the
            instance to the storage"""
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__[key] = datetime.datetime.strptime(value,
                                                                    timestamp)
                elif key == 'updated_at':
                    self.__dict__[key] = datetime.datetime.strptime(value,
                                                                    timestamp)
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self):
        """ converts to human readable string returning class name, id, dict"""
        message = "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
        return message

    def save(self):
        """ updates public instance to current date/time and saves to json """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returing a dictionary containing all keys/values of __dict__ """
        dict_cpy = self.__dict__.copy()
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        dict_cpy['__class__'] = self.__class__.__name__
        return dict_cpy
