# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.location import Location
from swagger_server.models.state import State
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestElbowController(BaseTestCase):
    """ ElbowController integration test stubs """

    def test_change_elbow(self):
        """
        Test case for change_elbow

        Set elbow location
        """
        body = Location()
        response = self.client.open('/v1/arm/elbow',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_change_elbow_torque(self):
        """
        Test case for change_elbow_torque

        Set elbow torque
        """
        body = State()
        response = self.client.open('/v1/arm/elbow/torque',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_elbow(self):
        """
        Test case for read_elbow

        Get elbow location
        """
        response = self.client.open('/v1/arm/elbow',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_elbow_torque(self):
        """
        Test case for read_elbow_torque

        Get elbow torque
        """
        response = self.client.open('/v1/arm/elbow/torque',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
