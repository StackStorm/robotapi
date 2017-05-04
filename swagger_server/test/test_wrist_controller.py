# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body1 import Body1
from swagger_server.models.inline_response200 import InlineResponse200
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
        body = Body1()
        response = self.client.open('/v1/arm/wrist',
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


if __name__ == '__main__':
    import unittest
    unittest.main()
