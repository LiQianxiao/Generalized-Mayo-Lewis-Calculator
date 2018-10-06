import numpy as np
from compute_F import compute_F
from scipy.optimize import minimize
from sklearn.model_selection import train_test_split


def loss(K_flat, *args):
    f_batch, F_batch, K_known = args
    n = np.sqrt(K_flat.size).astype(int)
    K = K_flat.reshape(n, n)
    nan_idx = np.isnan(K_known)
    K = np.where(nan_idx, K, K_known)
    l = 0
    for f, F in zip(f_batch, F_batch):
        l += np.linalg.norm(F - compute_F(f, K))**2
    return l


if __name__ == "__main__":
    # Read data
    K_known = np.genfromtxt('rc_inputs.csv', delimiter=',')
    print('Read K values (known=values, unknown=nan):')
    print(K_known)

    f_train = np.loadtxt('rc_train_f.csv', delimiter=',')
    F_train = np.loadtxt('rc_train_F.csv', delimiter=',')
    num_train = min(f_train.shape[0], F_train.shape[0])
    assert num_train > 0
    print('\nRead {} training samples.'.format(num_train))

    # Train-test split
    f_train, f_test, F_train, F_test \
        = train_test_split(f_train, F_train, test_size=0.1)
    print('Split into {} train and {} test samples'.format(
        f_train.shape[0], f_test.shape[0]))

    # Find K
    n = K_known.shape[0]
    K_init = np.random.uniform(size=(n**2,))
    bounds = [(0,10),]*(n**2)
    print('\nComputing K by L-BFGS-B...')
    results = minimize(
        loss, K_init,
        method='L-BFGS-B',
        bounds=bounds, args=(f_train, F_train, K_known),
        options={'ftol': 1e-16, 'gtol': 1e-12})
    print(results['message'])

    K_final = results['x'].reshape(n, n)
    K_final = np.where(np.isnan(K_known), K_final, K_known)

    print('\nRecovered K:')
    print(K_final)

    print('\nTest Error (should be small for the results to be valid): ',
          loss(K_final.flatten(), f_test, F_test, K_known))

    np.savetxt('rc_outputs.csv', K_final, delimiter=',')
    print('\nSaved output to <rc_outputs.csv>.')
