# Theory

Suppose there are <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.83004pt height=14.10255pt/> monomers species. Let
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/5e84bf2b027b638b5e40f2cedd0ab2ac.svg?invert_in_darkmode" align=middle width=206.1279pt height=18.842505pt/></p>
denote the vector of monomer concentrations, and
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/64ea9a5b35748bfcf3b90474062f868f.svg?invert_in_darkmode" align=middle width=218.03595pt height=18.842505pt/></p>
denote the vector of concentrations of chains terminating in monomer <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/a933dc57e0fa5fbc6ae48b7b0038de3f.svg?invert_in_darkmode" align=middle width=127.882425pt height=24.56553pt/> respectively.
Let us also write the rate constant matrix as
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/20f0db10c38e56c1ca28203ee50c110d.svg?invert_in_darkmode" align=middle width=73.389855pt height=14.524257pt/></p>
We shall assume that <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode" align=middle width=15.080505pt height=22.38192pt/> is in general position, i.e. <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode" align=middle width=15.080505pt height=22.38192pt/> is invertible and diagonalizable (which happens almost surely if this is measured with some random error)

Then, the generalized <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.83004pt height=14.10255pt/>-monomer Mayo-Lewis reaction is given by
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/9a74184f414210ecb7997d642036870f.svg?invert_in_darkmode" align=middle width=280.137pt height=25.22586pt/></p>

The rate equations are the following system of ODEs (written in vector form)
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/97ad7569d6df2a8af65e4efeb9533ebe.svg?invert_in_darkmode" align=middle width=259.71495pt height=74.15694pt/></p>
where <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/7422f922e82da6b0da5df4c35a7601c9.svg?invert_in_darkmode" align=middle width=24.58302pt height=27.59823pt/> is the transpose of the matrix <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode" align=middle width=15.080505pt height=22.38192pt/> amd <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/c0463eeb4772bfde779c20d52901d01b.svg?invert_in_darkmode" align=middle width=8.188554pt height=14.55762pt/> denotes vector Hadamard product, i.e. for vectors <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.359955pt height=14.10255pt/> and <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode" align=middle width=8.61696pt height=14.10255pt/>, <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/04322f29343f369175e1846b92969819.svg?invert_in_darkmode" align=middle width=33.471075pt height=14.55762pt/> is a vector with components <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/b65ec886f981876caa046c714ba46ff9.svg?invert_in_darkmode" align=middle width=211.426545pt height=24.56553pt/>.

Now, let us denote by <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/396ac573e737dfe2f2af06b7e4c7ac91.svg?invert_in_darkmode" align=middle width=9.416715pt height=21.10812pt/> the vector of all <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode" align=middle width=8.188554pt height=21.10812pt/>'s, i.e. <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/d0b5a78bf0fbce55b3eca6dd5509b4b3.svg?invert_in_darkmode" align=middle width=112.37391pt height=24.56553pt/>. Then, the monomer mole fraction is a vector
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/e3934e7f6bcd5ba174c38416c6e4cfbf.svg?invert_in_darkmode" align=middle width=71.17704pt height=33.5874pt/></p>
Similarly, the fraction of chains terminating in monomers <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/190083ef7a1625fbc75f243cffb9c96d.svg?invert_in_darkmode" align=middle width=9.780705pt height=22.74591pt/> is
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/a1e70a8cf8efef8c897764a9156d0872.svg?invert_in_darkmode" align=middle width=86.29137pt height=33.695805pt/></p>
Finally, under the steady-state condition the mole fraction of incorporated moonomer is a vector
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/7846a305e93ee090c6fcfcf929d54c1d.svg?invert_in_darkmode" align=middle width=104.55819pt height=38.773515pt/></p>
We shall assume that <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/fb97d38bcc19230b0acd442e17db879c.svg?invert_in_darkmode" align=middle width=17.67348pt height=22.38192pt/>, <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/b6d68c2b15646d339cd78f94165f4d74.svg?invert_in_darkmode" align=middle width=24.390135pt height=22.59873pt/> and <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/ec34ab0666d95c576d7aac361cec926f.svg?invert_in_darkmode" align=middle width=47.91732pt height=24.56553pt/> are not identically 0 so that the above expressions for <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/23c1e9d32c733e4f9f4cb37e6dc66794.svg?invert_in_darkmode" align=middle width=53.602065pt height=22.74591pt/> are well-defined.

Using the steady-state approximation, we may set <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/c5808e1db45faee8e3332cb190de7128.svg?invert_in_darkmode" align=middle width=86.44614pt height=24.56553pt/>. This allows us to write, using the ODE system, the following equations
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/a0c733eb57205c8c52d7bd7d70484333.svg?invert_in_darkmode" align=middle width=200.508pt height=64.711845pt/></p>
The last equation can be rewritten
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/631c9d51db3f7fdb5cafdeb79762df16.svg?invert_in_darkmode" align=middle width=161.63697pt height=19.315725pt/></p>
where for any vector <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.359955pt height=14.10255pt/>, <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/050292e4bb2e097b8726151db22c0646.svg?invert_in_darkmode" align=middle width=20.98536pt height=22.38192pt/> denotes the diagonal matrix formed by having <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode" align=middle width=9.359955pt height=14.10255pt/> on the diagonal and <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode" align=middle width=8.188554pt height=21.10812pt/> everywhere else. Since <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode" align=middle width=15.080505pt height=22.38192pt/> is in general position, the matrix <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/0d3d5fb26b0b67ab96c169b3f9a69765.svg?invert_in_darkmode" align=middle width=192.372345pt height=27.59823pt/> has a one-dimensional null-space, whose basis we denote by the vector <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/977a273d1ba0c715398789c02dc6e6fa.svg?invert_in_darkmode" align=middle width=59.298195pt height=24.56553pt/>. Then, we immediately have
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/f4ed84b507d6a7b2517ebb3c3edf9bd0.svg?invert_in_darkmode" align=middle width=120.46947pt height=38.773515pt/></p>

Therefore, we have the relashionship between <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/b8bc815b5e9d5177af01fd4d3d3c2f10.svg?invert_in_darkmode" align=middle width=12.80598pt height=22.38192pt/> and <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/190083ef7a1625fbc75f243cffb9c96d.svg?invert_in_darkmode" align=middle width=9.780705pt height=22.74591pt/>
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/042dc6f3360e8c5248ea6efe0adc0916.svg?invert_in_darkmode" align=middle width=146.96682pt height=40.289865pt/></p>

Conversely, given <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/b8bc815b5e9d5177af01fd4d3d3c2f10.svg?invert_in_darkmode" align=middle width=12.80598pt height=22.38192pt/> we can also determine <img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/190083ef7a1625fbc75f243cffb9c96d.svg?invert_in_darkmode" align=middle width=9.780705pt height=22.74591pt/>, but this is in general no longer a one-to-one mapping, hence we may resort to solving the optimization problem
<p align="center"><img src="https://rawgit.com/in	git@github.com:LiQianxiao/Generalized-Mayo-Lewis-Calculator/master/svgs/49418cf47001438c0393d4993a55c170.svg?invert_in_darkmode" align=middle width=342.45585pt height=40.289865pt/></p>
which can be solved numerically by the L-BFGS-B method.

---

# Program Usage

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
