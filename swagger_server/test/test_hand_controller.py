# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.location import Location
from swagger_server.models.state import State
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestHandController(BaseTestCase):
    """ HandController integration test stubs """

    def test_change_hand(self):
        """
        Test case for change_hand

        Set hand location
        """
        body = Location()
        response = self.client.open('/v1/arm/hand',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_change_hand_torque(self):
        """
        Test case for change_hand_torque

        Set hand torque
        """
        body = State()
        response = self.client.open('/v1/arm/hand/torque',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_hand(self):
        """
        Test case for read_hand

        Get hand location
        """
        response = self.client.open('/v1/arm/hand',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_hand_torque(self):
        """
        Test case for read_hand_torque

        Get hand torque
        """
        response = self.client.open('/v1/arm/hand/torque',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
