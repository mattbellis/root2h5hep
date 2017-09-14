import ROOT
import numpy as np

import sys


infilename = sys.argv[1]

infile = ROOT.TFile(infilename)

tree = infile.Get("T")

branch_names = []

branch_list = tree.GetListOfBranches();
nbranches = branch_list.GetEntries();

for br in range(0, nbranches):
    br_name = branch_list[br].GetName()
    br_type = branch_list[br].GetLeaf(br_name).GetTypeName()
    #br_name = branch_list[br].GetName()
    branch_names.append((br_name,br_type))

print(branch_names)


