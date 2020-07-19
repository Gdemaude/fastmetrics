# python_fastssim
This is an implementation of the Structural Similarity Index based on the skimage implementation: [https://github.com/scikit-image/scikit-image] but using the library numexpr: [https://github.com/pydata/numexpr] 

This reimplementation is around 25% faster than the skimage implementation (tested with i5-7300HQ CPU and 8GB of RAM). 

The usage is the same as the skimage function (skimage version '0.17.2').

Requirements: scikit-image >= 0.17.2, numexpr >= 2.7.1

