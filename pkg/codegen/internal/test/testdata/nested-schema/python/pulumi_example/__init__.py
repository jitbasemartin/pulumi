# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_example.a as __a
    a = __a
else:
    a = _utilities.lazy_import('pulumi_example.a')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "example",
  "mod": "a/b/c",
  "fqn": "pulumi_example.a.b.c",
  "classes": {
   "example:a/b/c:Resource": "Resource"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "example",
  "token": "pulumi:providers:example",
  "fqn": "pulumi_example",
  "class": "Provider"
 }
]
"""
)
