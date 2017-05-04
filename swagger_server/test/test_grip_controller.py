# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body import Body
from swagger_server.models.inline_response200 import InlineResponse200
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
        body = Body()
        response = self.client.open('/v1/arm/grip',
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


if __name__ == '__main__':
    import unittest
    unittest.main()
