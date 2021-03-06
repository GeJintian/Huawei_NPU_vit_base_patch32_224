"""
Copyright 2020 Huawei Technologies Co., Ltd

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import torch
import timm
import argparse


parser = argparse.ArgumentParser(description='Path', add_help=False)
parser.add_argument('--model-path', default="B_32-i21k-300ep-lr_0.001-aug_medium1-wd_0.03-do_0.0-sd_0.0--imagenet2012-steps_20k-lr_0.03-res_224.npz", metavar='DIR',
                    help='path to model')
parser.add_argument('--batch-size',default="1", type=int,
                    help='batch size')


def main():
    args = parser.parse_args()
    model = timm.create_model('vit_base_patch32_224')
    model.load_pretrained(args.model_path)
    model.eval()
    tensor = torch.zeros(args.batch_size,3,224,224)
    torch.onnx.export(model, tensor, "vit_bs"+str(args.batch_size)+".onnx", opset_version=11,
                      do_constant_folding=True, input_names=["input"], output_names=["output"])


if __name__ == "__main__":
    main()
