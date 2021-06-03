from __future__ import absolute_import, division, print_function

import os
import pkg_resources

# OpenAI Python bindings.
#
# Originally forked from the MIT-licensed Stripe Python bindings.

# Configuration variables

api_key = os.environ.get("OPENAI_API_KEY")
organization = os.environ.get("OPENAI_ORGANIZATION")
client_id = None
api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com")
file_api_base = None
api_version = None
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None
enable_telemetry = True
max_network_retries = 0
ca_bundle_path =  pkg_resources.resource_filename(__name__,  "data/ca-certificates.crt")
debug = False

# Set to either 'debug' or 'info', controls console logging
log = None

# API resources
from openai.api_resources import *  # noqa

from openai.error import OpenAIError, APIError, InvalidRequestError
