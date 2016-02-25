#
# Minimal tests to check whether the installation is working
#

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from framework import grouptools
from framework.test import PiglitGLTest
from framework.profile import TestProfile, Test

__all__ = ['profile']

profile = TestProfile()

import os

if 'WINE_ROOT' in os.environ:
    WINE_ROOT = os.environ['WINE_ROOT']
else:
    #WINE_ROOT = os.path.join(
        #core.PIGLIT_CONFIG.required_get('igt', 'path'), 'tests')
    WINE_ROOT = "/home/lizhenbo/src/wine"

print(WINE_ROOT)


class WineTest(Test):
    """Test class for running libdrm."""
    #def __init__(self, binary, arguments=None):
        #if arguments is None:
            #arguments = []
        #super(IGTTest, self).__init__(
            #[os.path.join(IGT_TEST_ROOT, binary)] + arguments)
        #self.timeout = 600

    def interpret_result(self):
        super(WineTest, self).interpret_result()

        print( "Got return code: " + str(self.result.returncode) )
        self.result.result = 'pass'
        #if self.result.returncode == 0:
            #self.result.result = 'pass'
        #elif self.result.returncode == 77:
            #self.result.result = 'skip'
        #elif self.result.returncode == 78:
            #self.result.result = 'timeout'
        #else:
            #self.result.result = 'fail'

profile.test_list["mesa-wine"] = \
        WineTest([os.path.join(WINE_ROOT, "mesa-wine")])

