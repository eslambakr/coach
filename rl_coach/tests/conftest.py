#
# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""PyTest configuration."""

import configparser as cfgparser
import os
import platform
import shutil
import pytest
import rl_coach.tests.utils.args_utils as a_utils
import rl_coach.tests.utils.presets_utils as p_utils
from rl_coach.tests.utils.definitions import Definitions as Def
from os import path


def pytest_collection_modifyitems(config, items):
    """pytest built in method to pre-process cli options"""
    global test_config
    test_config = cfgparser.ConfigParser()
    str_rootdir = str(config.rootdir)
    str_inifile = str(config.inifile)
    # Get the relative path of the inifile
    # By default is an absolute path but relative path when -c option used
    config_path = os.path.relpath(str_inifile, str_rootdir)
    config_path = os.path.join(str_rootdir, config_path)
    assert (os.path.exists(config_path))
    test_config.read(config_path)


def pytest_runtest_setup(item):
    """Called before test is run."""
    if (item.get_marker("unstable") and
            "unstable" not in item.config.getoption("-m")):
        pytest.skip("skipping unstable test")

    if item.get_marker("linux_only"):
        if platform.system() == 'Windows':
            pytest.skip("Skipping test that not Linux OS.")

    if item.get_marker("golden_test"):
        """ do some custom configuration for golden tests. """
        # TODO: add custom functionality
        pass


@pytest.fixture(scope="module", params=list(p_utils.collect_presets()))
def preset_name(request):
    """
    Return all preset names
    """
    return request.param


@pytest.fixture(scope="function", params=list(a_utils.collect_args()))
def flag(request):
    """
    Return flags names in function scope
    """
    return request.param


@pytest.fixture(scope="module", params=list(a_utils.collect_preset_for_args()))
def preset_args(request):
    """
    Return preset names that can be used for args testing only; working in
    module scope
    """
    return request.param


@pytest.fixture(scope="function")
def clres(request):
    """
    Create both file csv and log for testing
    :yield: class of both files paths
    """

    class CreateCsvLog:
        """
        Create a test and log paths
        """
        def __init__(self, csv, log, pattern):
            self.csv_path = csv
            self.stdout = log
            self.fn_pattern = pattern

    # get preset name from test request params
    idx = 0 if 'preset' in list(request.node.funcargs.items())[0][0] else 1
    p_name = list(request.node.funcargs.items())[idx][1]

    p_valid_params = p_utils.validation_params(p_name)

    test_name = 'ExpName_{}'.format(p_name)
    test_path = os.path.join(Def.Path.experiments, test_name)
    if path.exists(test_path):
        shutil.rmtree(test_path)

    # get the stdout for logs results
    log_file_name = os.path.join(Def.Path.experiments,
                                 'test_log_{}.txt'.format(p_name))
    stdout = open(log_file_name, 'w')
    fn_pattern = 'worker_0*.csv' if p_valid_params.num_workers > 1 else '*.csv'

    res = CreateCsvLog(test_path, stdout, fn_pattern)

    yield res

    # clean files
    if path.exists(res.csv_path):
        shutil.rmtree(res.csv_path)

    if os.path.exists(res.csv_path):
        os.remove(res.stdout)
