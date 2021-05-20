# coding: utf-8

#
# Copyright 2010-2014 Ning, Inc.
# Copyright 2014-2020 Groupon, Inc
# Copyright 2020-2021 Equinix, Inc
# Copyright 2014-2021 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.22-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class UserRoles(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'username': 'Str',
        'password': 'Str',
        'roles': 'List[Str]'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'roles': 'roles'
    }

    def __init__(self, username=None, password=None, roles=None):  # noqa: E501
        """UserRoles - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._password = None
        self._roles = None
        self.discriminator = None

        self.username = username
        self.password = password
        self.roles = roles

    @property
    def username(self):
        """Gets the username of this UserRoles.  # noqa: E501


        :return: The username of this UserRoles.  # noqa: E501
        :rtype: Str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserRoles.


        :param username: The username of this UserRoles.  # noqa: E501
        :type: Str
        """


        self._username = username

    @property
    def password(self):
        """Gets the password of this UserRoles.  # noqa: E501


        :return: The password of this UserRoles.  # noqa: E501
        :rtype: Str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserRoles.


        :param password: The password of this UserRoles.  # noqa: E501
        :type: Str
        """


        self._password = password

    @property
    def roles(self):
        """Gets the roles of this UserRoles.  # noqa: E501


        :return: The roles of this UserRoles.  # noqa: E501
        :rtype: List[Str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserRoles.


        :param roles: The roles of this UserRoles.  # noqa: E501
        :type: List[Str]
        """


        self._roles = roles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserRoles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
