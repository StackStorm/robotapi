# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body2 import Body2
from swagger_server.models.inline_response200 import InlineResponse200
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
        body = Body2()
        response = self.client.open('/v1/arm/hand',
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


if __name__ == '__main__':
    import unittest
    unittest.main()
