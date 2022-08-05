# ASPIRE_QSAR
QSAR models for the ASPIRE Grant Project

## Background
Aims to utilize machine learning methodology for candidate Non-Addictive Opioid MOA prediction, in which major clusters used for separation are full agonist, paritial agonist, antagonist. Both Unsupervised and Supervised learning techniques are used for prediction, then grid search performed on the best model to conduct hyperparameter optimization. Current work only supports **mu opioid receptors**. 

## Installation and Setup
1. Create conda enviroment using the yml file provided

`conda env create -f ASPIRE_QSAR.yml`

2. Run `morganFP_analysis2.ipynb` or `mol2vec_analysis3.ipynb` to view the full analysis on MOA prediction.


## Features
- Mol2Vec 
  - Corpus is generated from morgan identifiers (up to selected radius) which represents words (molecules and sentences). 
    It is an unsupervised machine learning approach to obtain high dimensional embeddings of chemical substructures.
  - Reference: https://github.com/samoturk/mol2vec
- Morgan Fingerprint Bit Vector
   - Generated from Rdkit, is built by applying the Morgan algorithm to a set of user-supplied atom invariants. 
   - `AllChem.GetMorganFingerprintAsBitVect()`
   
## Preprocessing
- Mol2Vec 
  - Mol obj -> Sentence -> Word2Vec training -> Vector embedding
- Morgan Fingerprint Bit Vector
  - Bit Vector (1024-bit) -> Truncated SVD

## Dimensionality reduction technique
- **Linear Discriminant Analysis (LDA) - (Fisher Variation)** creates the best separation between classes. (50:50 train:test)
- **T-distributed Stochastic Neighbor Embedding (TSNE)** is used in visualization
- Mol2vec

  ![image](https://user-images.githubusercontent.com/69520909/183004871-ae49e036-7290-43d8-ad9b-ae3148da26b4.png)
  
- Morgan Fingerprint Bit Vector

  ![image](https://user-images.githubusercontent.com/69520909/183003987-d1cdb81d-3cfe-443b-ad0f-0937d7573ce0.png)

## Clustering technique
- Due to the spherical nature of the clusters, K-means performs the best when clustering the data.
- True Labels are paired with predicted clusters based on their cluster count to determine quality clusters.
- Mol2vec
  
  ![image](https://user-images.githubusercontent.com/69520909/183005234-1ab6f285-186d-4778-b148-81da1a935b04.png)

- Morgan Fingerprint Bit Vector

  ![image](https://user-images.githubusercontent.com/69520909/183005318-c6a1ae64-3161-40bf-b37e-cb8ffe802281.png)
  
## Supervised classification + Grid Search
- Random Forest, Support Vector Classifier, Decision Tree, K-neighbors classifier, Naive Bayes, Gradient Boosting Classifier, Linear Discriminant Analysis (top model from unsupervised) are placed on Grid Search for hyperparameter optimization and tuning.
- Multiple runs on grid search shows that major classifiers stated did not outperform LDA by a significant margin, only raising or lowering classification accuracy and f1_macro metrics by 2-3%.
  
   
  
