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



class TagDefinition(object):
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
        'id': 'Str',
        'is_control_tag': 'Bool',
        'name': 'Str',
        'description': 'Str',
        'applicable_object_types': 'List[Str]',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'id': 'id',
        'is_control_tag': 'isControlTag',
        'name': 'name',
        'description': 'description',
        'applicable_object_types': 'applicableObjectTypes',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, id=None, is_control_tag=None, name=None, description=None, applicable_object_types=None, audit_logs=None):  # noqa: E501
        """TagDefinition - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._is_control_tag = None
        self._name = None
        self._description = None
        self._applicable_object_types = None
        self._audit_logs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_control_tag is not None:
            self.is_control_tag = is_control_tag
        self.name = name
        self.description = description
        if applicable_object_types is not None:
            self.applicable_object_types = applicable_object_types
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def id(self):
        """Gets the id of this TagDefinition.  # noqa: E501


        :return: The id of this TagDefinition.  # noqa: E501
        :rtype: Str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TagDefinition.


        :param id: The id of this TagDefinition.  # noqa: E501
        :type: Str
        """


        self._id = id

    @property
    def is_control_tag(self):
        """Gets the is_control_tag of this TagDefinition.  # noqa: E501


        :return: The is_control_tag of this TagDefinition.  # noqa: E501
        :rtype: Bool
        """
        return self._is_control_tag

    @is_control_tag.setter
    def is_control_tag(self, is_control_tag):
        """Sets the is_control_tag of this TagDefinition.


        :param is_control_tag: The is_control_tag of this TagDefinition.  # noqa: E501
        :type: Bool
        """


        self._is_control_tag = is_control_tag

    @property
    def name(self):
        """Gets the name of this TagDefinition.  # noqa: E501


        :return: The name of this TagDefinition.  # noqa: E501
        :rtype: Str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagDefinition.


        :param name: The name of this TagDefinition.  # noqa: E501
        :type: Str
        """


        self._name = name

    @property
    def description(self):
        """Gets the description of this TagDefinition.  # noqa: E501


        :return: The description of this TagDefinition.  # noqa: E501
        :rtype: Str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TagDefinition.


        :param description: The description of this TagDefinition.  # noqa: E501
        :type: Str
        """


        self._description = description

    @property
    def applicable_object_types(self):
        """Gets the applicable_object_types of this TagDefinition.  # noqa: E501


        :return: The applicable_object_types of this TagDefinition.  # noqa: E501
        :rtype: List[Str]
        """
        return self._applicable_object_types

    @applicable_object_types.setter
    def applicable_object_types(self, applicable_object_types):
        """Sets the applicable_object_types of this TagDefinition.


        :param applicable_object_types: The applicable_object_types of this TagDefinition.  # noqa: E501
        :type: List[Str]
        """

        allowed_values = ["ACCOUNT", "ACCOUNT_EMAIL", "BLOCKING_STATES", "BUNDLE", "CUSTOM_FIELD", "INVOICE", "PAYMENT", "TRANSACTION", "INVOICE_ITEM", "INVOICE_PAYMENT", "SUBSCRIPTION", "SUBSCRIPTION_EVENT", "SERVICE_BROADCAST", "PAYMENT_ATTEMPT", "PAYMENT_METHOD", "TAG", "TAG_DEFINITION", "TENANT", "TENANT_KVS"]  # noqa: E501
        if not set(applicable_object_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `applicable_object_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(applicable_object_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._applicable_object_types = applicable_object_types

    @property
    def audit_logs(self):
        """Gets the audit_logs of this TagDefinition.  # noqa: E501


        :return: The audit_logs of this TagDefinition.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this TagDefinition.


        :param audit_logs: The audit_logs of this TagDefinition.  # noqa: E501
        :type: List[AuditLog]
        """


        self._audit_logs = audit_logs

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
        if not isinstance(other, TagDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
