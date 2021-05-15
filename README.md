# DeePromClass

DeePromClass is a deep learning based promoter finding tool developed for 5 different organisms namely c-elegans, homo-sapiens, drosophila-melanogaster, mus-musculus, yeast.

IMPORTANT:-

1.)Prior to running the file with the name "Promoter_Finder_and_classifier.ipynb" install the required files listed in the requirements.tx file using the command "pip install -r requirements.txt".

2.)Input the genome data in the file "Input_data.txt".

3.)Open the file "Promoter_Finder_and_classifier.ipynb" , run all the cells in a sequence and select the organism of choice.

4.)Wait for the code to run completely as it may take a few minutes based on the size of the input data.

5.)All the output of possible promoters, along with their indexes in the genome and also with the classification of which known promoter elements are present in the predicted promoter sequence is saved to the file named "Motif_list_with_indexes_and_classification.txt".

DO NOT MODIFY THE CONTENTS OF MODELS FOLDER AS IT MAY ALTER OR DAMAGE THE OUTPUT.

Training Files folder contains the main code with which the 5 models are developed and the data used to train and test the models.
##Comment out the first cell of each train.ipynb file if you are using jupyter notebook and not google colab.
