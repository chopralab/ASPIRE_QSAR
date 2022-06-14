# # loop for Fisher’s LDA
# rand_score_list = []
# shrink_list = np.round_(np.cumsum([0.1 for x in range(10)]), decimals=2)
# train_size_list = np.round(np.cumsum([0.1 for x in range(10)]), decimals=2)

# for shrink in shrink_list:
#     shrink_temp_list = []
#     for train_size in train_size_list:
#         # scaler = StandardScaler()
#         # df_mol2vec_scaled = pd.DataFrame(scaler.fit_transform(df_mol2vec))
#         try:
#             df_mol2vec_scaled['action_gen'] = df['action_gen']

#             X_train, X_test, y_train, y_test = train_test_split(df_mol2vec_scaled.iloc[:, :-1], df_mol2vec_scaled.iloc[:, -1], train_size=train_size, random_state=42)
#             n_comp = 2
#             lda = LDA(n_components=n_comp, solver='eigen', shrinkage=shrink).fit(X_train, y_train)
            
#             df_mol2vec_scaled.drop("action_gen", axis=1, inplace=True)
#             lda_results = lda.transform(df_mol2vec_scaled)

#             lda_results = pd.DataFrame(lda_results, columns=['ld' + str(i) for i in range(1, n_comp+1)])

#             clustering_kmeans = KMeans(n_clusters=4)
#             lda_results['clusters'] = clustering_kmeans.fit_predict(lda_results)
#             rd_sc = rand_score(df.action_gen, lda_results.clusters)
#             shrink_temp_list.append(rd_sc)
#         except:
#             shrink_temp_list.append(0)


#     rand_score_list.append(shrink_temp_list)

# # sns.lineplot(x_val, rand_score_list)
# # plt.grid()
# # plt.show()

# rand_score_df = pd.DataFrame(rand_score_list, columns=train_size_list, index=shrink_list)
# f, ax = plt.subplots(figsize=(20, 15))
# s = sns.heatmap(rand_score_df, annot=True)
# s.set(xlabel='train_size_list', ylabel='shrink_list')



#---------------------------------------------------------------------------------


# sample_size_list = [x for x in range(10, 170, 10)]
# rand_score_list = []

# np.random.seed(42)
# for sample_size in sample_size_list:
#     df_mol2vec_scaled['action_gen'] = df['action_gen']

#     df_sample = df_mol2vec_scaled.sample(n=sample_size)
#     lda = LDA(n_components=2).fit(df_sample.iloc[:, :-1], df_sample.iloc[:, -1])

#     df_mol2vec_scaled.drop("action_gen", axis=1, inplace=True)
#     lda_results = lda.transform(df_mol2vec_scaled)



#     lda_results = pd.DataFrame(lda_results, columns=['lda1', 'lda2'])

#     clustering_kmeans = KMeans(n_clusters=4)
#     lda_results['clusters'] = clustering_kmeans.fit_predict(lda_results)
#     rd_sc = rand_score(df.action_gen, lda_results.clusters)
#     rand_score_list.append(rd_sc)

# sns.lineplot(sample_size_list, rand_score_list)
# plt.grid()
# plt.show()
    