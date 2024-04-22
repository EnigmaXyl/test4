# Copyright 2022 Webull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from webullsdkcore.client import ApiClient
from webullsdkcore.exception.exceptions import ServerException
from webullsdktrade.api import API

optional_api_endpoint = "</optional_api_endpoint>"
your_app_key = "</your_app_key>"
your_app_secret = "</your_app_secret>"

# 'hk' or 'us'
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
api_client.add_endpoint(region_id, optional_api_endpoint)


class TestResetKey(unittest.TestCase):

    def test_reset_key(self):
        api = API(api_client)
        try:
            response = api.reset_operation.reset_key()
            print(response.json())
        except ServerException as se:
            print(se)