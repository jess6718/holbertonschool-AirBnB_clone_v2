#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = User

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()  # replaced BaseModel with User
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()  # replaced BaseModel with User
        copy = i.to_dict()
        new = User(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()  # replaced BaseModel with User
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = User(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()  # replaced BaseModel with User
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()  # replaced BaseModel with User
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()  # replaced BaseModel with User
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    # def test_kwargs_one(self):
    #     """ """
    #     n = {'Name': 'test'}
    #     with self.assertRaises(KeyError):
    #         new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    # def test_updated_at(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.updated_at), datetime.datetime)
    #     n = new.to_dict()
    #     new = User(**n)
    #     self.assertFalse(new.created_at == new.updated_at)
