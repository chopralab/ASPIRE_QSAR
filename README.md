# ASPIRE_QSAR
QSAR models for the ASPIRE Grant Project

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

  ![image](https://user-images.githubusercontent.com/69520909/181805262-2ccc023b-9eb2-45f0-9dd7-65936a974ea6.png)
  
- Morgan Fingerprint Bit Vector

  ![image](https://user-images.githubusercontent.com/69520909/181805431-1025ef69-9a04-4d0b-9b3e-d5cb6a6108b8.png)


## Clustering technique
- Due to the spherical nature of the clusters, K-means performs the best when clustering the data.
- True Labels are paired with predicted clusters based on their cluster count to determine quality clusters.
- Mol2vec
  
  ![image](https://user-images.githubusercontent.com/69520909/181806173-287d101e-1db0-40f1-a479-036f4fe0bbbd.png)

- Morgan Fingerprint Bit Vector

  ![image](https://user-images.githubusercontent.com/69520909/181806239-bcdc8c3c-6484-47c0-99de-9ee01f750bc5.png)
 
  

  
   
  
