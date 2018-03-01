# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os
import sys


"""
Why is this traversal necessary? Why not just call:
  os.path.split(os.path.realpath(__file__))[0]
and know that that is official/ ?

The reason is that is python 2, __file__ can be either the .py or .pyc file.
When this script is invoked through a symlink, the .pyc file is not in official/
so instead a more involved process is necessary.
"""
_cwd = os.path.abspath(__file__)
while True:
  _cwd, resid = os.path.split(_cwd)
  if resid == "":
    raise NameError("TensorFlow model glue import failed.")
  if _cwd.endswith("official"):
    _cwd = os.path.split(_cwd)[0]
    if _cwd not in sys.path:
      sys.path.append(_cwd)
    break
