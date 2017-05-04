# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body4 import Body4
from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestSholderController(BaseTestCase):
    """ SholderController integration test stubs """

    def test_change_sholder(self):
        """
        Test case for change_sholder

        Set sholder location
        """
        body = Body4()
        response = self.client.open('/v1/arm/sholder',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_sholder(self):
        """
        Test case for read_sholder

        Get sholder location
        """
        response = self.client.open('/v1/arm/sholder',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
