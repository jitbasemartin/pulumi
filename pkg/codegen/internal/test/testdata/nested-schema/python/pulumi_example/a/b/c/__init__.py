# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .... import _utilities
import typing
# Export this package's modules as members:
from .resource import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_example.a.b.c.d as __d
    d = __d
else:
    d = _utilities.lazy_import('pulumi_example.a.b.c.d')

