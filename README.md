# Hoog-Finder
A Python Program to detect mismodeled Hoogsteen base pair from nucleic acids containing PDB structures.

#### MANUAL of Hoog-Finder Python Script ####
Copyright @ Honglue Shi 2021

Contact: honglue.shi@duke.edu / lvelve0901@gmail.com

Citation:

Shi, H., et al. (2021). "Revealing A-T and G-C Hoogsteen base pairs in stressed protein-bound duplex DNA." bioRxiv: 2021.2006.2005.447203.

Lu, X. J., et al. (2015). "DSSR: an integrated software tool for dissecting the spatial structure of RNA." Nucleic Acids Res 43(21).

#### Warning ####
The current version of program has only been benchmarked for DNA Watson-Crick base pairs.

#### Python Dependency ####
```
Python 2.7.16
json 2.0.9
numpy 1.16.6
pandas 0.24.2
```

#### Other Requirement ####
To run this Python program, you need to install x3dna-dssr.
x3dna-dssr is developed and maintained by Dr. X.J.Lu at Columbia Univ.
Use x3dna-dssr to parse the structure parameters from a nucleic acids containing PDB.
Under their policies, the software program and all files in the program may only be licensed and distributed through Columbia Technology Ventures of Columbia University. 
Please go to http://forum.x3dna.org/site-announcements/download-instructions for the download instruction. 
Please also make sure to cite: Lu, X. J., et al. (2015). 
“DSSR: an integrated software tool for dissecting the spatial structure of RNA.” Nucleic Acids Res 43(21). 
For the demo, we provided some output JSON files as examples in the “example” folder.

#### Manual ####
### Step 1: Use DSSR to parse structure and generate JSON file ###
example command:
```
x3dna-dssr -i=example/5a0w.pdb -o=example/5a0w.json --more --json
x3dna-dssr --cleanup
```

after this step, a JSON file called XXXX.json will be generated.

Reminder:
For structures with palindromic double-stranded DNA that were deposited as single chains in the assymmetric unit,
you need to download the biological assembly file.
For example, for PDB 5HP4, you need to download the biological assembly file (5hp4.pdb1) in RCSB.
When you process the 5hp4.pdb1, you also need to turn on the --symm flag in x3dna-dssr.

example command:
```
x3dna-dssr -i=example/5hp4.pdb1 -o=example/5hp4.json --more --json --symm
x3dna-dssr --cleanup
```


### Step 2: Use the Python Script hg_finder.py to analyze the JSON file ###
example command:
```
python hg_finder.py example/5hp4.json
```

example output:
```
Start to process JSON file: 5hp4.json

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Detected potential mismodeled Hoogsteen!
Model ID:Chain ID.Residue
Nucleotide 1   1:X.DT5
Nucleotide 2   3:X.DA6
shear=3.024 opening=52.505 C1C1_dist=8.158
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Detected potential mismodeled Hoogsteen!
Model ID:Chain ID.Residue
Nucleotide 1   1:X.DA6
Nucleotide 2   3:X.DT5
shear=3.024 opening=52.505 C1C1_dist=8.158
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
```
