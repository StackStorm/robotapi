# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.location import Location
from swagger_server.models.state import State
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestShoulderController(BaseTestCase):
    """ ShoulderController integration test stubs """

    def test_change_shoulder(self):
        """
        Test case for change_shoulder

        Set shoulder location
        """
        body = Location()
        response = self.client.open('/v1/arm/shoulder',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_change_shoulder_torque(self):
        """
        Test case for change_shoulder_torque

        Set shoulder torque
        """
        body = State()
        response = self.client.open('/v1/arm/shoulder/torque',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_shoulder(self):
        """
        Test case for read_shoulder

        Get shoulder location
        """
        response = self.client.open('/v1/arm/shoulder',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_shoulder_torque(self):
        """
        Test case for read_shoulder_torque

        Get shoulder torque
        """
        response = self.client.open('/v1/arm/shoulder/torque',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
