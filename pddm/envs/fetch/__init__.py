# Copyright 2019 Google LLC
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

from gym.envs.registration import register

register(
    id='MB_FetchSlideEnv-v1',
    entry_point='pddm.envs.fetch.slide:FetchSlideEnv',
    max_episode_steps=50,
)

register(
    id='MB_FetchPush-v1',
    entry_point='pddm.envs.fetch.push:FetchPushEnv',
    max_episode_steps=50,
)

register(
    id='MB_FetchPickAndPlaceEnv-v1',
    entry_point='pddm.envs.fetch.pick_and_place:FetchPickAndPlaceEnv',
    max_episode_steps=50,
)

register(
    id='MB_FetchReachEnv-v1',
    entry_point='pddm.envs.fetch.reach:FetchReachEnv',
    max_episode_steps=50,
)

