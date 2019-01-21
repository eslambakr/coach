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
"""Manage all command arguments."""

import os
from rl_coach.tests.utils.definitions import Definitions as Def


def collect_preset_for_args():
    """
    Collect presets that relevant for args testing only.
    :return: preset(s) list
    """
    for pn in Def.Presets.args_test:
        assert pn, Def.Consts.ASSERT_MSG.format("Preset name", pn)
        yield pn


def collect_args():
    """
    Collect args from the cmd args list - on each test iteration, it will
    yield one line (one arg).
    :yield: one arg foe each test iteration
    """
    for k, v in Def.Flags.cmd_args.items():
        cmd = []
        cmd.append(k)
        if v is not None:
            cmd.append(v)
        assert cmd, Def.Consts.ASSERT_MSG.format("cmd array", str(cmd))
        yield cmd


def add_one_flag_value(flag):
    """
    Add value to flag format in order to run the python command with arguments.
    :param flag: dict flag
    :return: flag with format
    """
    if not flag or len(flag) > 2 or len(flag) <= 0:
        return []

    if len(flag) == 1:
        return flag

    if Def.Flags.css in flag[1]:
        flag[1] = 30

    elif Def.Flags.crd in flag[1]:
        # TODO: check dir of checkpoint
        flag[1] = os.path.join(Def.Path.experiments)

    elif Def.Flags.et in flag[1]:
        # TODO: add valid value
        flag[1] = ""

    elif Def.Flags.ept in flag[1]:
        # TODO: add valid value
        flag[1] = ""

    elif Def.Flags.cp in flag[1]:
        # TODO: add valid value
        flag[1] = ""

    elif Def.Flags.seed in flag[1]:
        flag[1] = 0

    elif Def.Flags.dccp in flag[1]:
        # TODO: add valid value
        flag[1] = ""

    return flag


def validate_args_results():
    pass
