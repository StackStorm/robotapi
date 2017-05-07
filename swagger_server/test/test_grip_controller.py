# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.location import Location
from swagger_server.models.state import State
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGripController(BaseTestCase):
    """ GripController integration test stubs """

    def test_change_grip(self):
        """
        Test case for change_grip

        Set grip location
        """
        body = Location()
        response = self.client.open('/v1/arm/grip',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_change_grip_torque(self):
        """
        Test case for change_grip_torque

        Set grip torque
        """
        body = State()
        response = self.client.open('/v1/arm/grip/torque',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_grip(self):
        """
        Test case for read_grip

        Get grip location
        """
        response = self.client.open('/v1/arm/grip',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_grip_torque(self):
        """
        Test case for read_grip_torque

        Get grip torque
        """
        response = self.client.open('/v1/arm/grip/torque',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
