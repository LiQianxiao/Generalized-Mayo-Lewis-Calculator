import numpy as np
from scipy.optimize import minimize


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


def loss(f, *args):
    K, F = args
    F_compute = compute_F(f, K)
    return np.linalg.norm(F_compute - F)**2


def constraints(f):
    return f


def compute_f(F, *args):
    K, n = args
    F = F / np.sum(F)
    bounds = np.asarray([(0, 5),]*n)
    init = np.asarray([2.5,]*n)
    results = minimize(
        loss, init,
        method='L-BFGS-B',
        bounds=bounds, args=(K, F), options={'ftol': 1e-16, 'gtol': 1e-12})
    print(results['message'])
    print('Loss: ', results['fun'])
    f = results['x'] / np.sum(results['x'])
    return f


if __name__ == "__main__":
    # read config
    K = np.loadtxt('rate_constants.csv', delimiter=',')
    n = K.shape[0]
    F_batch = np.loadtxt('product_inputs.csv', delimiter=',')

    # Print Message
    print('\nRead rate constant matrix: ')
    print(K)

    print('\nRead input product mole fractions: ')
    for F in F_batch:
        print(F)

    # Compute and save output
    print('\nComputing output product mole fractions by L-BFGS-B...\n')
    f_batch = []
    for F in F_batch:
        f_batch.append(compute_f(F, K, n))

    print('\nComputed output product mole fractions: ')
    for f in f_batch:
        print(f)

    np.savetxt('monomer_outputs.csv', f_batch, fmt='%.3f', delimiter=', ')
    print('\nSaved output to <monomer_outputs.csv>.')
