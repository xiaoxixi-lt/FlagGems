import logging

import triton
import triton.language as tl

from ..utils.pointwise_dynamic import pointwise_dynamic


@pointwise_dynamic(promotion_methods=[(0, "INT_TO_FLOAT")])
@triton.jit
def cos_func(x):
    return tl.cos(x.to(tl.float32))


def cos(A):
    logging.debug("GEMS COS")
    return cos_func(A)


def cos_(A):
    logging.debug("GEMS COS_")
    cos_func(A, out0=A)
    return A
