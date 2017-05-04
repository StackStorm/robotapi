# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body5 import Body5
from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestPivotController(BaseTestCase):
    """ PivotController integration test stubs """

    def test_change_pivot(self):
        """
        Test case for change_pivot

        Set pivot location
        """
        body = Body5()
        response = self.client.open('/v1/arm/pivot',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_read_pivot(self):
        """
        Test case for read_pivot

        Get pivot location
        """
        response = self.client.open('/v1/arm/pivot',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
