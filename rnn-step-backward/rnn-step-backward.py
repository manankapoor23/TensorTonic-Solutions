import numpy as np

def rnn_step_backward(dh, cache):
    """
    Returns:
        dx_t: gradient wrt input x_t      (shape: D,)
        dh_prev: gradient wrt previous h (shape: H,)
        dW: gradient wrt W               (shape: H x D)
        dU: gradient wrt U               (shape: H x H)
        db: gradient wrt bias            (shape: H,)
    """
    # Write code here
    x_t , h_prev , W_xh,W_hh,h_t = cache
    da_t = dh *(1-h_t**2)

    dw_xh = np.outer(da_t,x_t)
    dw_hh =np.outer(da_t , h_prev.T)
    db=da_t
    dx_t = W_xh.T @ da_t
    dh_prev = W_hh.T @ da_t

    return (dx_t,dh_prev,dw_xh,dw_hh,db)

    pass
