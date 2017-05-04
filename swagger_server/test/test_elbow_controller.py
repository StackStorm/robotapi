# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body3 import Body3
from swagger_server.models.inline_response200 import InlineResponse200
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
        body = Body3()
        response = self.client.open('/v1/arm/elbow',
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


if __name__ == '__main__':
    import unittest
    unittest.main()
