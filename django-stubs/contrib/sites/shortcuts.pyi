# Stubs for django.contrib.sites.shortcuts (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite
from django.http.request import HttpRequest
from typing import Optional, Union
def get_current_site(request: Optional[HttpRequest]) -> Union[RequestSite, Site]: ...
