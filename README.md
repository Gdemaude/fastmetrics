# fastmetrics
This is a python3 implementation of several image quality metrics: the Structural Similarity Index, the Peak Signal to Noise ratio and the Mean Squared Error are based on the skimage implementation: [https://github.com/scikit-image/scikit-image] but using the library numexpr: [https://github.com/pydata/numexpr] to improve performance.

The SSIM reimplementation is around 25% faster than the skimage implementation (tested with i5-7300HQ CPU and 8GB of RAM) and the MSE (and thus PSNR) is 10% faster. 
The usage is the same as the skimage function (skimage version '0.17.2') except for one more return argument: cs, the contrast sensitivity (used in the MS-SSIM).

The MS-SSIM isn't implemented in skimage. This implementation is based on the tensorflow implementation. However it is calling this SSIM function to run. (doc and tests required) 


Requirements: scikit-image >= 0.17.2, numexpr >= 2.7.1

This package does not use the GPU, it is only a CPU implementation.

# Installation

pip install git+https://github.com/ricardolsmendes/python-package-cheat-sheet
