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
"""
Definitions file:

It's main functionality are:
1) housing project constants and enums.
2) housing configuration parameters.
3) housing resource paths.
"""


class Definitions:
    GROUP_NAME = "rl_coach"
    PROCESS_NAME = "coach"

    class Flags:
        css = "checkpoint_save_secs"
        crd = "checkpoint_restore_dir"
        et = "environment_type"
        ept = "exploration_policy_type"
        cp = "custom_parameter"
        seed = "seed"
        dccp = "distributed_coach_config_path"

        """
        Arguments that can be tested for python coach command
         ** None    = Flag - no need for string or int
         ** {}      = Add format for this parameter
        """
        cmd_args = {
            '-l': None,
            # '-e': '{}',
            '-r': None,
            # '-n': '{' + enw + '}',
            '-c': None,
            '-ew': None,
            '--play': None,
            '--evaluate': None,
            '-v': None,
            '-tfv': None,
            '--nocolor': None,
            '-s': '{' + css + '}',
            '-crd': '{' + crd + '}',
            '-dg': None,
            '-dm': None,
            '-et': '{' + et + '}',
            '-ept': '{' + ept + '}',
            # '-lvl': '{level}',
            '-cp': '{' + cp + '}',
            '--print_networks_summary': None,
            '-tb': None,
            '-ns': None,
            '-d': None,
            '--seed': '{' + seed + '}',
            '-onnx': None,
            '-dc': None,
            '-dcp': '{' + dccp + '}',
            '-asc': None,
            '--dump_worker_logs': None,
            '-ns -asc': '{} {}'
        }

    class Presets:
        # Preset list for testing the flags/ arguments of python coach command
        args_test = [
            "CartPole_A3C",
            # "CartPole_NEC",
        ]

    class Path:
        experiments = "./experiments"

    class Consts:
        ASSERT_MSG = "Expected {}, Actual {}."

    class TimeOuts:
        test_time_limit = 60 * 60
