## Huawei_NPU_vit_base_patch32_224
This reposity is a copy of my codes for the project about migration and deployment of vit_base_patch32_224 to Huawei Ascend NPU.<br>
#### About this project
This project has two parts: training and infer. Training is on Ascend310 and infer is on Ascend910.
- Training part
1. Validate official accuracy and test performance of training on GPU.
2. Migrate the model to NPU and implement training script for it.
3. Validate its accuracy and performance in NPU. If there exists a gap between NPU and GPU result, the source code should be revised.

- Infer part
1. Validate official accuracy and test performance of infer on GPU.
2. Transfer the pretrained model parameters to ONNX model (sometimes ONNX-SIMPLIFY is necessary), and then transfer the ONNX model to OM model by using CANN of Huawei.
3. Process the dataset. Transfer images input to binary files.
4. Validate the infer result usig benchmark by Huawei. Compare its accuracy and performance with GPU. The source code should be revised if necessary.<br>

You can find my contribute in gitee, see: [vit_base gitee source code](https://gitee.com/ascend/modelzoo/tree/master/contrib/PyTorch/Research/cv/image_classification/vit_base_patch32_224).<br>

#### About the model
This model, vit_base_patch32_224, is an image classification algorithm from timm package. In this project, I didn't change the structure of this model. Therefore, it should be consistent with the [source code](https://github.com/rwightman/pytorch-image-models/blob/master/timm/models/vision_transformer.py).<br>
The article of this model is available at [AN IMAGE IS WORTH 16 X 16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE](https://arxiv.org/pdf/2010.11929.pdf).
