#!/usr/bin/python3
"""Unittest for the base_model class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing the base_model class"""
    def test_base_model_id(self):
        """Test that id is assigned as a string"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_base_model_create(self):
        """Test that created_at is stored as datetime"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)

    def test_base_model_update(self):
        """Test that updated_at is stored as datetime"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_unique_id(self):
        """Test that each id is unique"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_init_time(self):
        """Test that created_at and updated_at are equal upon creation"""
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_save_update(self):
        """Test that updated_at is changed upon save"""
        bm1 = BaseModel()
        created = bm1.created_at
        updated = bm1.updated_at
        bm1.save()
        self.assertEqual(bm1.created_at, created)
        self.assertNotEqual(bm1.updated_at, updated)

    def test_to_dict(self):
        """Test that to_dict returns a dictionary with proper attributes"""
        bm1 = BaseModel()
        dict_model = bm1.to_dict()
        self.assertIsInstance(dict_model, dict)
        self.assertIsInstance(dict_model["updated_at"], str)
        self.assertIsInstance(dict_model["created_at"], str)

    def test_str_(self):
        """Test that the str method has the correct output"""
        bm1 = BaseModel()
        self.assertIn(bm1.id, str(bm1))

    def test_init_with_kwargs(self):
        """Test that you can create an instance with kwargs"""
        created_at = '2023-06-25T00:00:00.000000'
        updated_at = '2023-06-25T00:00:00.000000'
        template = {
            'id': 'Person',
            'created_at': created_at,
            'updated_at': updated_at,
            'name': 'Robert'
        }
        bm1 = BaseModel(**template)
        self.assertEqual(bm1.id, 'Person')
        self.assertEqual(bm1.created_at,
                         datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.updated_at,
                         datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.name, 'Robert')

    def test_to_dict_and_back(self):
        """Test for full path of recreating from dictionary """
        bm1 = BaseModel()
        bm1_str = str(bm1)
        bm2_template = bm1.to_dict()
        bm2 = BaseModel(**bm2_template)
        self.assertEqual(str(bm2), bm1_str)
        self.assertIsInstance(bm2.created_at, datetime)
        self.assertIsInstance(bm2.updated_at, datetime)
