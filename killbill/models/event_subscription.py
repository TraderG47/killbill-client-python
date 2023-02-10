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

    OpenAPI spec version: 0.24.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class EventSubscription(object):
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
        'event_id': 'Str',
        'billing_period': 'Str',
        'effective_date': 'Datetime',
        'catalog_effective_date': 'Datetime',
        'plan': 'Str',
        'product': 'Str',
        'price_list': 'Str',
        'event_type': 'Str',
        'is_blocked_billing': 'Bool',
        'is_blocked_entitlement': 'Bool',
        'service_name': 'Str',
        'service_state_name': 'Str',
        'phase': 'Str',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'event_id': 'eventId',
        'billing_period': 'billingPeriod',
        'effective_date': 'effectiveDate',
        'catalog_effective_date': 'catalogEffectiveDate',
        'plan': 'plan',
        'product': 'product',
        'price_list': 'priceList',
        'event_type': 'eventType',
        'is_blocked_billing': 'isBlockedBilling',
        'is_blocked_entitlement': 'isBlockedEntitlement',
        'service_name': 'serviceName',
        'service_state_name': 'serviceStateName',
        'phase': 'phase',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, event_id=None, billing_period=None, effective_date=None, catalog_effective_date=None, plan=None, product=None, price_list=None, event_type=None, is_blocked_billing=None, is_blocked_entitlement=None, service_name=None, service_state_name=None, phase=None, audit_logs=None):  # noqa: E501
        """EventSubscription - a model defined in Swagger"""  # noqa: E501

        self._event_id = None
        self._billing_period = None
        self._effective_date = None
        self._catalog_effective_date = None
        self._plan = None
        self._product = None
        self._price_list = None
        self._event_type = None
        self._is_blocked_billing = None
        self._is_blocked_entitlement = None
        self._service_name = None
        self._service_state_name = None
        self._phase = None
        self._audit_logs = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if billing_period is not None:
            self.billing_period = billing_period
        if effective_date is not None:
            self.effective_date = effective_date
        if catalog_effective_date is not None:
            self.catalog_effective_date = catalog_effective_date
        if plan is not None:
            self.plan = plan
        if product is not None:
            self.product = product
        if price_list is not None:
            self.price_list = price_list
        if event_type is not None:
            self.event_type = event_type
        if is_blocked_billing is not None:
            self.is_blocked_billing = is_blocked_billing
        if is_blocked_entitlement is not None:
            self.is_blocked_entitlement = is_blocked_entitlement
        if service_name is not None:
            self.service_name = service_name
        if service_state_name is not None:
            self.service_state_name = service_state_name
        if phase is not None:
            self.phase = phase
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def event_id(self):
        """Gets the event_id of this EventSubscription.  # noqa: E501


        :return: The event_id of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this EventSubscription.


        :param event_id: The event_id of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._event_id = event_id

    @property
    def billing_period(self):
        """Gets the billing_period of this EventSubscription.  # noqa: E501


        :return: The billing_period of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this EventSubscription.


        :param billing_period: The billing_period of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._billing_period = billing_period

    @property
    def effective_date(self):
        """Gets the effective_date of this EventSubscription.  # noqa: E501


        :return: The effective_date of this EventSubscription.  # noqa: E501
        :rtype: Datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this EventSubscription.


        :param effective_date: The effective_date of this EventSubscription.  # noqa: E501
        :type: Datetime
        """


        self._effective_date = effective_date

    @property
    def catalog_effective_date(self):
        """Gets the catalog_effective_date of this EventSubscription.  # noqa: E501


        :return: The catalog_effective_date of this EventSubscription.  # noqa: E501
        :rtype: Datetime
        """
        return self._catalog_effective_date

    @catalog_effective_date.setter
    def catalog_effective_date(self, catalog_effective_date):
        """Sets the catalog_effective_date of this EventSubscription.


        :param catalog_effective_date: The catalog_effective_date of this EventSubscription.  # noqa: E501
        :type: Datetime
        """


        self._catalog_effective_date = catalog_effective_date

    @property
    def plan(self):
        """Gets the plan of this EventSubscription.  # noqa: E501


        :return: The plan of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this EventSubscription.


        :param plan: The plan of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._plan = plan

    @property
    def product(self):
        """Gets the product of this EventSubscription.  # noqa: E501


        :return: The product of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this EventSubscription.


        :param product: The product of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._product = product

    @property
    def price_list(self):
        """Gets the price_list of this EventSubscription.  # noqa: E501


        :return: The price_list of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._price_list

    @price_list.setter
    def price_list(self, price_list):
        """Sets the price_list of this EventSubscription.


        :param price_list: The price_list of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._price_list = price_list

    @property
    def event_type(self):
        """Gets the event_type of this EventSubscription.  # noqa: E501


        :return: The event_type of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventSubscription.


        :param event_type: The event_type of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._event_type = event_type

    @property
    def is_blocked_billing(self):
        """Gets the is_blocked_billing of this EventSubscription.  # noqa: E501


        :return: The is_blocked_billing of this EventSubscription.  # noqa: E501
        :rtype: Bool
        """
        return self._is_blocked_billing

    @is_blocked_billing.setter
    def is_blocked_billing(self, is_blocked_billing):
        """Sets the is_blocked_billing of this EventSubscription.


        :param is_blocked_billing: The is_blocked_billing of this EventSubscription.  # noqa: E501
        :type: Bool
        """


        self._is_blocked_billing = is_blocked_billing

    @property
    def is_blocked_entitlement(self):
        """Gets the is_blocked_entitlement of this EventSubscription.  # noqa: E501


        :return: The is_blocked_entitlement of this EventSubscription.  # noqa: E501
        :rtype: Bool
        """
        return self._is_blocked_entitlement

    @is_blocked_entitlement.setter
    def is_blocked_entitlement(self, is_blocked_entitlement):
        """Sets the is_blocked_entitlement of this EventSubscription.


        :param is_blocked_entitlement: The is_blocked_entitlement of this EventSubscription.  # noqa: E501
        :type: Bool
        """


        self._is_blocked_entitlement = is_blocked_entitlement

    @property
    def service_name(self):
        """Gets the service_name of this EventSubscription.  # noqa: E501


        :return: The service_name of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this EventSubscription.


        :param service_name: The service_name of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._service_name = service_name

    @property
    def service_state_name(self):
        """Gets the service_state_name of this EventSubscription.  # noqa: E501


        :return: The service_state_name of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._service_state_name

    @service_state_name.setter
    def service_state_name(self, service_state_name):
        """Sets the service_state_name of this EventSubscription.


        :param service_state_name: The service_state_name of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._service_state_name = service_state_name

    @property
    def phase(self):
        """Gets the phase of this EventSubscription.  # noqa: E501


        :return: The phase of this EventSubscription.  # noqa: E501
        :rtype: Str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this EventSubscription.


        :param phase: The phase of this EventSubscription.  # noqa: E501
        :type: Str
        """


        self._phase = phase

    @property
    def audit_logs(self):
        """Gets the audit_logs of this EventSubscription.  # noqa: E501


        :return: The audit_logs of this EventSubscription.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this EventSubscription.


        :param audit_logs: The audit_logs of this EventSubscription.  # noqa: E501
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
        if not isinstance(other, EventSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
