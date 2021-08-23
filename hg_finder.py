
import os
import re
import sys
import json
import pandas as pd
import numpy as np
import learnna.learnna_json as lna_json

json_f = sys.argv[1]
if json_f.endswith('.json') == False:
    json_f = json_f + '.json'

najson = lna_json.NA_JSON()  #initialize class objects
with open(json_f) as json_data:  #read each json file
    data1 = json.load(json_data)

najson.set_json(data1)  #pass json file to class pbject
najson.read_idx()  #set index from own json file

isMismodel = False

print("Start to process JSON file: %s"%json_f)

bps = najson.json_file['pairs']
for bp in bps:
    
    bp_type = bp['bp'][0]+bp['bp'][2]
    shear, stretch, stagger, buckle, propell, opening = bp['bp_params']
    c1c1_dist = bp['C1C1_dist']
    LW = bp['LW']
    if bp_type in ['TA','tA','Ta','ta','CG','cG','Cg','cg']:
        shear = shear * -1
        buckel = buckle * -1
    
    if bp_type.upper() in ['AT','TA','CG','GC']:
        if LW in ['cWW','cWS','cSW','cW.','c.W']:
            if shear >= 0.5 and opening >= 10 and c1c1_dist <= 10:
                print("")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Detected potential mismodeled Hoogsteen!")
                if ':' in bp['nt1']:
                    print("Model ID:Chain ID.Residue")
                else:
                    print("Chain ID.Residue")
                print("Nucleotide 1   %s"%(bp['nt1']))
                print("Nucleotide 2   %s"%(bp['nt2']))
                print("shear=%.3f opening=%.3f C1C1_dist=%.3f"%(shear,opening,c1c1_dist))
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                isMismodel = True

if isMismodel == False:
    print("Didn't find any potential mismodeled Hoogsteen!")
