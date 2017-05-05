# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body4 import Body4
from swagger_server.models.inline_response200 import InlineResponse200
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
        body = Body4()
        response = self.client.open('/v1/arm/shoulder',
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


if __name__ == '__main__':
    import unittest
    unittest.main()
