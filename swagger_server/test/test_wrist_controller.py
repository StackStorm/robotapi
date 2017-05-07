# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.location import Location
from swagger_server.models.state import State
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestWristController(BaseTestCase):
    """ WristController integration test stubs """

    def test_change_wrist(self):
        """
        Test case for change_wrist

        Set wrist location
        """
        body = Location()
        response = self.client.open('/v1/arm/wrist',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_change_wrist_torque(self):
        """
        Test case for change_wrist_torque

        Set wrist torque
        """
        body = State()
        response = self.client.open('/v1/arm/wrist/torque',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_wrist(self):
        """
        Test case for read_wrist

        Get wrist location
        """
        response = self.client.open('/v1/arm/wrist',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_wrist_torque(self):
        """
        Test case for read_wrist_torque

        Get wrist torque
        """
        response = self.client.open('/v1/arm/wrist/torque',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
