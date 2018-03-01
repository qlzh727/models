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
Solution 0: "It is left as an exercise to the reader..."

Pros:
  Clean. The python code doesn't have to contort itself.
  There is no extraneous code if the code is installed. (i.e. pip)

Cons:
  * Failure is frustrating. On import failure there is no opportunity to call
    our code, we can't provide a "Look here for PYTHONPATH info" message.
  * It can make the code brittle in subtle ways. For example:
      $ export PYTHONPATH="$PYTHONPATH:$HOME/TensorFlow/models"
      $ python example.py
      $ sudo python example.py  # Fails because the export doesn't affect root
  * Collisions can occur and are subtle. For instance:
      $ mkdir ~/collision_example; cd ~/collision example
      $ git clone https://github.com/tensorflow/models.git repo_0
      $ export PYTHONPATH="$PYTHONPATH:$HOME/collision_example/repo_0"
      ... Doing stuff, decide I want another copy
      $ git clone https://github.com/tensorflow/models.git repo_1
      $ export PYTHONPATH="$PYTHONPATH:$HOME/collision_example/repo_1"
      $ cd repo_1/official/pkg_soln_1
      $ python example.py  # Actually using repo_0 because it is first in the path

Basically, when everything works it is the best option. When things fail it is
either opaque (bad) or wrong but doesn't raise (much worse). Still a viable
option though.
"""

from official.resnet import Model
print("Import succeeded!")
