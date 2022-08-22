# Copyright 1999-2015 Alibaba Group Holding Ltd.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8
import logging
from webullsdkcore.auth.signers.signer import Signer

logger = logging.getLogger(__name__) 

class AppKeySigner(Signer):
    def __init__(self, app_key_credential):
        self._credential = app_key_credential

    def sign(self, request):
        cred = self._credential
        host = request.get_endpoint()
        header = request.get_signed_header(host, cred.app_key_id, cred.app_key_secret)
        return header