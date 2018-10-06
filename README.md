# Program Usage

For theory, see [write-up](theory.pdf) in the repository

## 1. Computing product mole fractions from monomer mole fractions

### 1.1 Config files

1. Put the rate constants into ```rate_constants.csv```

    Example (3 monomers):

        k11, k12, k13
        k21, k22, k23
        k31, k32, k33

2. Put the monomer mole fractions into ```monomer_inputs.csv```

    Example: (3 monomers, 2 different configs):

        f1, f2, f3
        g1, g2, g3

### 1.2 Usage

Run ```compute.py```

        python compute_F.py

The results are saved to ```product_outputs.csv```, in the format

        F1, F2, F3
        G1, G2, G3

## 2. Computing monomer mole fractions from product mole fractions

### 2.1 Config files

1. Put the rate constants into ```rate_constants.csv```

    Example (3 monomers):

        k11, k12, k13
        k21, k22, k23
        k31, k32, k33

2. Put the monomer mole fractions into ```monomer_inputs.csv```

    Example: (3 products, 2 different configs):

        F1, F2, F3
        G1, G2, G3

### 2.2 Usage

Run ```compute.py```

        python compute_f.py

The results are saved to ```monomer_outputs.csv```, in the format

        f1, f2, f3
        g1, g2, g3

## 3. Computing K from f and F

### 3.1 Config files

1. Put the known rate constants into ```rc_inputs.csv```, and leave the unknown ones as ```NaN```

    Example (3 monomers):

        k11, NaN, NaN
        NaN, k22, k23
        k31, NaN, k33

2. Put the training data for f and F into ```rc_train_f.csv``` and ```rc_train_F.csv``` respectively in the following format. Note that the data for f and F should be matching.

    Example: (3 monomers, 2 training samples):

    In ```rc_train_f.csv```

        f1, f2, f3
        g1, g2, g3

    In ```rc_train_F.csv```

        F1, F2, F3
        G1, G2, G3

### 3.2 Usage

Run ```fit_K.py```

        python fit_K.py

The results are saved to ```rc_outputs.csv``` in the usual format.

        k11, k12, k13
        k21, k22, k23
        k31, k32, k33

Make sure that the test loss is small before trusting the results.

### Note

Can optionally run the debug flag ```python fit_K.py --debug``` to check against results from synthetic data (the original csv files included in this repository should not be altered for this check)