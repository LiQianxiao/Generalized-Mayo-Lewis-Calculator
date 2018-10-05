# README

## Computing Product mole fractions from monomer mole fractions

### Config files

1. Put the rate constants into ```rate_constants.csv```
    Example (3 monomers):

        k11, k12, k13
        k21, k22, k23
        k31, k32, k33

2. Put the monomer mole fractions into ```monomer_inputs.csv```
    Example: (3 monomers, 2 different configs):

        f1, f2, f3
        g1, g2, g3

### Usage

Run ```compute.py```

        python compute_F.py

The results are saved to ```product_outputs.csv```, in the format

        F1, F2, F3
        G1, G2, G3

## Computing monomer mole fractions from product mole fractions

### Config files

1. Put the rate constants into ```rate_constants.csv```
    Example (3 monomers):

        k11, k12, k13
        k21, k22, k23
        k31, k32, k33

2. Put the monomer mole fractions into ```monomer_inputs.csv```
    Example: (3 products, 2 different configs):

        F1, F2, F3
        G1, G2, G3

### Usage

Run ```compute.py```

        python compute_f.py

The results are saved to ```monomer_outputs.csv```, in the format

        f1, f2, f3
        g1, g2, g3
