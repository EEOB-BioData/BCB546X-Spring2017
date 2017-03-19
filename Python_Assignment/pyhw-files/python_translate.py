######################## BCB 546X: Python Assignment Details ########################

## Your Mission: Complete Python code in a Jupyter Notebook ##
## 1. Document Dr. X's function with comments and with markdown text in your Jupyter notebook
## 2. Write a function that translates a string of nucleotides to amino acids based on Dr. X's pseudo-code suggestion
## 3. Write an alternative translation function
## 4. Write a function (or 3 functions) that calculates the proportion of each of 3 amino acid categories in a sequence
## 5. In the MAIN part of the script, call your functions from 3 (or 2) and 4 and complete the empty columns in the dataframe
## 6. Plot a bar-chart of adult mass per species
## 7. Plot a graph that shows the amino-acid type proportions
## 8. Write the entire dataframe to a new CSV file
## 9. BONUS: What other visualizations, functions or tasks would you do with this dataset? Add something interesting for fun. 
## ** Do all of this in a Jupyter notebook and push it to a GitHub repository
## ** Be sure to cite (by providing URLs) information appropriately in your documented notebook.
## ** Commit and push your completed work in the Jupyter notebook to your repository
## ** Create a link to your completed Jupyter notebook using https://nbviewer.jupyter.org
## ** Send the above link *AND* the URL to your git repository to the instructors via Slack by the end of the day on March 31.

## Not all of these tasks have been covered in class and you will 
## have to use online resources to find out how to do some of these tasks.


######################## Python Translate Script ########################

## Here's the start of our Python script. Thanks for completing it for me! - Dr. X
## IMPORTANT: install biopython so that this will work

from Bio import SeqIO
from Bio.Data import CodonTable
import pandas as pd

#%%%%%%%%%%%%%%%#
### FUNCTIONS ###
#%%%%%%%%%%%%%%%#

## 1 ##
## Dr. X: this gets sequences 
## please finish documenting this function with comments, or in notebook markdown text
## be sure to provide details on return types and arguments
def get_sequences_from_file(fasta_fn):
    sequence_data_dict = {}
    for record in SeqIO.parse(fasta_fn, "fasta"):
        description = record.description.split()
        species_name = description[1] + " " + description[2]
        sequence_data_dict[species_name] = record.seq
    return(sequence_data_dict)

## 2 ##
####### YOUR STRING-TRANSLATE FUNCTION ########
## Write a function that translates sequences
## All sequences start at codon position 1
## Complete a function that does this using loop over the string of nucleotides
## Here is  some pseudo-code and suggestions
## feel free to change the function and variable names
# def translate_function(string_nucleotides): 
#     mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"] # this should work using BioPython (be sure to check what this returns)
#     for-loop through every 3rd position in string_nucleotides to get the codon using range subsets
#         # IMPORTANT: if the sequence has a stop codon at the end, you should leave it off
#         # this is how you can retrieve the amino acid: mito_table.forward_table[codon]
#         add the aa to aa_seq_string
#     return(aa_seq_string)

## 3 ##
####### YOUR ALTERNATIVE FUNCTION ########
## Is there a better way to write the translation function? (Hint: yes there is.) 
## Perhaps using available BioPython library utilities?
## Please also write this function.


## 4 ##
####### YOUR COUNT AA FUNCTION ########
## Write a function that takes an amino-acid sequence (as a BioPython Seq or as a string) 
## and computes the proportion of the 3 different categories of amino acid
## (you may want to write this as 3 separate functions instead of just 1, it's up to you)
## These categories are based on the 
# def get_proportion_aa_type_function(aa_seq):
#     charged = ['R','K','D','E']
#     polar = ['Q','N','H','S','T','Y','C','M','W']
#     hydrophobic = ['A','I','L','F','V','P','G']
#     for aa in charged:
#         # count the number of times that aa appears, add to the total for charged
#     # repeat for polar and hydrophobic
#     return proportion_charged, proportion_polar, proportion_hydro 


#%%%%%%%%%%%%%%#
###   MAIN   ###
#%%%%%%%%%%%%%%#

cytb_seqs = get_sequences_from_file("bears_cytb.fasta") 

bear_df = pd.read_csv("bears_data.csv") # Includes only data for body mass currently and empty cells for other columns
species_list = list(bear_df.species)

## 5 ##
## Write a for-loop that translates each sequence and also gets the proportion
## of each aa type in that translated sequence and adds those data to dataframe
# for key, value in cytb_seqs.items():
#     aa_seq = nuc2aa_translate_function(vale)
#     # get proportions of each aa type
#     set the value of each proportion in the dataframe (i.e., fill in empty cells in DF)

# %matplotlib inline # uncomment for jupyter nb.

## 6 ##
## Plot a bar-chart of the mass with the x-axes labeled with species names.
## What is the largest bear species? What else is interesting about this species?

## 7 ##
## Plot a visualization of the proportions for amino-acid type for the bear species
## What does this show about cytochrome-b for the bears?

## 8 ##
## Save the new dataframe to a file called "bears_mass_cytb.csv"

## BONUS ##
## What else can we do with this dataset in Python? 
## Add functions or anything that might be interesting and fun. (optional)

