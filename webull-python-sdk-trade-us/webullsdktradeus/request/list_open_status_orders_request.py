# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8
from webullsdkcore.request import ApiRequest


class ListTodayOrdersRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/trade/orders/list-open", method="GET", query_params={})

    def set_account_id(self, account_id):
        self.add_query_param("account_id", account_id)

    def set_last_order_id(self, last_order_id):
        self.add_query_param("last_order_id", last_order_id)

    def set_last_order_place_time(self, last_order_place_time):
        self.add_query_param("last_order_place_time", last_order_place_time)









