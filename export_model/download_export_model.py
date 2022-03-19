# coding: utf8
# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import os
from paddleseg.utils.download import _uncompress_file
import gdown

LOCAL_PATH = os.path.join(os.getcwd(), 'export_model')


def download(use_cpu):
    if use_cpu:
        _id = '1HnJLlwptmAIw4HstjDwymTBWqx6jBMTu'
    else:
        _id = '1nQEWtsywGE_Bn54rRk_ynTuYejusFblx'

    output = os.path.join(LOCAL_PATH, 'model.zip')
    gdown.download(id=_id, output=output)
    _uncompress_file(
        filepath=output,
        extrapath=LOCAL_PATH,
        delete_file=True,
        print_progress=True,
    )

    print("Export model download success!")
