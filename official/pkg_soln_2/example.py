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
Solution 2: Shared, symlinked glue import.

Pros:
  * Reasonably robust. We can put in arbitrary code, so any edge case that we
    can think of can be addressed.
  * Fairly pythonic. A single import doesn't look too terrible.

Cons:
  * The symlink has to be present. This can really clutter up a directory
    structure, and not everything plays nice with symlinks (for instance rsync
    will not copy them by default) which can make the code more brittle.
  * The import is kind of "magic", so one could easily do something like name
    a subdirectory something that suddenly breaks imports, and have no idea why.
"""
import glue_import
from official.resnet import Model
print("Import succeeded!")
