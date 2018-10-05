import numpy as np


def compute_F(f, *args):
    K, = args
    f = f / np.sum(f)
    A = np.diag(f) @ K.T - np.diag(K @ f)
    eigvals, eigvecs = np.linalg.eig(A)
    zero_id = np.argmin(np.abs(eigvals.real))
    fs = eigvecs[:, zero_id].real
    fs = fs / np.sum(fs)
    F = f * (K.T @ fs) / (f.T @ K.T @ fs)
    return F


if __name__ == "__main__":
    # read config
    K = np.loadtxt('rate_constants.csv', delimiter=',')
    n = K.shape[0]
    f_batch = np.loadtxt('monomer_inputs.csv', delimiter=',')

    # Compute and save output
    F_batch = []
    for f in f_batch:
        F_batch.append(compute_F(f, K))
    np.savetxt('product_outputs.csv', F_batch, fmt='%.3f', delimiter=', ')
    print('Saved output to <product_outputs.csv>.')