#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    # this is so that django has permissions to create the test database
    settings.DATABASES['default']['USER'] = 'root'
    settings.DATABASES['default']['PASSWORD'] = 'docker_root'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["apiapp"])
    sys.exit(bool(failures))
