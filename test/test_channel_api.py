"""
    DSB Message Broker API

    Swagger documentation for the DSB Message Broker API  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import dsb_client
from dsb_client.api.channel_api import ChannelApi  # noqa: E501


class TestChannelApi(unittest.TestCase):
    """ChannelApi unit test stubs"""

    def setUp(self):
        self.api = ChannelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_channel_controller_create_channel(self):
        """Test case for channel_controller_create_channel

        """
        pass

    def test_channel_controller_get_accessible_channels(self):
        """Test case for channel_controller_get_accessible_channels

        """
        pass

    def test_channel_controller_get_channel(self):
        """Test case for channel_controller_get_channel

        """
        pass

    def test_channel_controller_remove_channel(self):
        """Test case for channel_controller_remove_channel

        """
        pass

    def test_channel_controller_update_channel(self):
        """Test case for channel_controller_update_channel

        """
        pass


if __name__ == '__main__':
    unittest.main()