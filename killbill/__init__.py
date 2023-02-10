# coding: utf-8

# flake8: noqa

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

from __future__ import absolute_import

base_uri = 'http://localhost:8080'
username = 'admin'
password = 'password'
api_key = 'bob'
api_secret = 'lazar'

try:
    import json
except ImportError:
# Python 2.5 compatibility (import your own json module, e.g. killbill.json=simplejson)
    pass

# Custom urllib opener, e.g.:
#   from killbill.grinder_http_handler import GrinderHTTPHandler
#   killbill.opener = GrinderHTTPHandler
opener = None

import logging

logging.basicConfig(level=logging.DEBUG)

# import apis into sdk package
from killbill.api.account_api import AccountApi
from killbill.api.admin_api import AdminApi
from killbill.api.bundle_api import BundleApi
from killbill.api.catalog_api import CatalogApi
from killbill.api.credit_api import CreditApi
from killbill.api.custom_field_api import CustomFieldApi
from killbill.api.export_api import ExportApi
from killbill.api.invoice_api import InvoiceApi
from killbill.api.invoice_item_api import InvoiceItemApi
from killbill.api.invoice_payment_api import InvoicePaymentApi
from killbill.api.nodes_info_api import NodesInfoApi
from killbill.api.overdue_api import OverdueApi
from killbill.api.payment_api import PaymentApi
from killbill.api.payment_gateway_api import PaymentGatewayApi
from killbill.api.payment_method_api import PaymentMethodApi
from killbill.api.payment_transaction_api import PaymentTransactionApi
from killbill.api.plugin_info_api import PluginInfoApi
from killbill.api.security_api import SecurityApi
from killbill.api.subscription_api import SubscriptionApi
from killbill.api.tag_api import TagApi
from killbill.api.tag_definition_api import TagDefinitionApi
from killbill.api.tenant_api import TenantApi
from killbill.api.usage_api import UsageApi

# import ApiClient
from killbill.api_client import ApiClient
from killbill.configuration import Configuration
# import models into sdk package
from killbill.models.account import Account
from killbill.models.account_email import AccountEmail
from killbill.models.account_timeline import AccountTimeline
from killbill.models.admin_payment import AdminPayment
from killbill.models.audit_log import AuditLog
from killbill.models.block_price import BlockPrice
from killbill.models.blocking_state import BlockingState
from killbill.models.bulk_subscriptions_bundle import BulkSubscriptionsBundle
from killbill.models.bundle import Bundle
from killbill.models.bundle_timeline import BundleTimeline
from killbill.models.catalog import Catalog
from killbill.models.catalog_validation import CatalogValidation
from killbill.models.catalog_validation_error import CatalogValidationError
from killbill.models.combo_hosted_payment_page import ComboHostedPaymentPage
from killbill.models.combo_payment_transaction import ComboPaymentTransaction
from killbill.models.custom_field import CustomField
from killbill.models.duration import Duration
from killbill.models.entity import Entity
from killbill.models.event_subscription import EventSubscription
from killbill.models.hosted_payment_page_fields import HostedPaymentPageFields
from killbill.models.hosted_payment_page_form_descriptor import HostedPaymentPageFormDescriptor
from killbill.models.invoice import Invoice
from killbill.models.invoice_dry_run import InvoiceDryRun
from killbill.models.invoice_item import InvoiceItem
from killbill.models.invoice_payment import InvoicePayment
from killbill.models.invoice_payment_transaction import InvoicePaymentTransaction
from killbill.models.limit import Limit
from killbill.models.node_command import NodeCommand
from killbill.models.node_command_property import NodeCommandProperty
from killbill.models.node_info import NodeInfo
from killbill.models.overdue import Overdue
from killbill.models.overdue_condition import OverdueCondition
from killbill.models.overdue_state import OverdueState
from killbill.models.overdue_state_config import OverdueStateConfig
from killbill.models.payment import Payment
from killbill.models.payment_attempt import PaymentAttempt
from killbill.models.payment_method import PaymentMethod
from killbill.models.payment_method_plugin_detail import PaymentMethodPluginDetail
from killbill.models.payment_transaction import PaymentTransaction
from killbill.models.phase import Phase
from killbill.models.phase_price import PhasePrice
from killbill.models.plan import Plan
from killbill.models.plan_detail import PlanDetail
from killbill.models.plugin_info import PluginInfo
from killbill.models.plugin_property import PluginProperty
from killbill.models.plugin_service_info import PluginServiceInfo
from killbill.models.price import Price
from killbill.models.price_list import PriceList
from killbill.models.product import Product
from killbill.models.role_definition import RoleDefinition
from killbill.models.rolled_up_unit import RolledUpUnit
from killbill.models.rolled_up_usage import RolledUpUsage
from killbill.models.session import Session
from killbill.models.simple_plan import SimplePlan
from killbill.models.subject import Subject
from killbill.models.subscription import Subscription
from killbill.models.subscription_usage_record import SubscriptionUsageRecord
from killbill.models.tag import Tag
from killbill.models.tag_definition import TagDefinition
from killbill.models.tenant import Tenant
from killbill.models.tenant_key_value import TenantKeyValue
from killbill.models.tier import Tier
from killbill.models.tier_price import TierPrice
from killbill.models.tiered_block import TieredBlock
from killbill.models.unit import Unit
from killbill.models.unit_usage_record import UnitUsageRecord
from killbill.models.usage import Usage
from killbill.models.usage_price import UsagePrice
from killbill.models.usage_record import UsageRecord
from killbill.models.user_roles import UserRoles
