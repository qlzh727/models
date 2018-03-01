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


"""
Solution 1: Path hacking based on the current file.

IMPORTANT:
  In python 2, __file__ may point either to a .py file or a .pyc file. This
  means that this path hack will not function properly if a file is symlinked
  and then run, because python will put the .pyc file next to the symlink rather
  than the original file.

Pros:
  * Self contained. (Does not rely on any other files or structure.)
  * Reasonably compact.
  
Cons:
  * Fails if "models/official" is earlier in the file path, or if the root is 
    not named "models".
  * Must come before imports, violating style guides.
  * Is hacky.

"""

import os
import re
import sys

_ROOT = re.sub(r"models/official.*", r"models", os.path.abspath(__file__))
if _ROOT not in sys.path: sys.path.append(_ROOT)

# Variant.
#   Eliminates the dependence on re, at the expense of being even hackier.
_ROOT = os.path.abspath(__file__).split("models/official")[0] + "models"
if _ROOT not in sys.path: sys.path.append(_ROOT)

from official.resnet import Model
print("Import succeeded!")
