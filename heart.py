# # ===============================
# # loading dataset
# # ===============================
# import pandas as pd
# df = pd.read_csv("dataset/heart.csv")
# # print(df)

# # ==================================
# # Exploratory data analysis
# # ==================================
 
# # print(df.head())
# # print(df.tail())
# # print(df.columns)
# # df.info()
# print(df.describe())
# # print(df.shape)
# # print(df.index)
# # print(df.isnull().sum())
# # print(df.duplicated().sum()) 
# # there re 723 duplicates so remove it
# df = df.drop_duplicates()
# # print(df.shape)
# # check whether dataset is balanced or not
# # print(df['target'].value_counts())
# import matplotlib.pyplot as plt

# # df['target'].value_counts().plot(kind='bar')
# # plt.title('heart disease prediction')
# # plt.xlabel('target')
# # plt.ylabel('frequancy')
# # plt.show()

# # plt.boxplot(df['target'])
# # plt.title("heart disease")
# # plt.show()

# # check how numerical features are distributed based on info dtype

# # age
# # plt.hist(df['age'])
# # plt.title("Age distribution")
# # plt.show()

# # thalach
# # plt.hist(df['thalach'])
# # plt.title("thalach distribution")
# # plt.show()

# # restecg
# # plt.hist(df['restecg'])
# # plt.title("restecg distribution")
# # plt.show()
# # print(df['restecg'].describe())

# # ===================================
# # preprocessing
# # ===================================

# # encoding is not needed because all values are int or float

# # ========================================
# # train multiple models
# # ========================================

# # splitting dataset

# x = df.drop('target',axis=1)
# y = df['target']

# # test train split
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# # # importing models
# # # from sklearn.linear_model import LogisticRegression
# # # from sklearn.tree import DecisionTreeClassifier
# # # from sklearn.ensemble import RandomForestClassifier
# # # from sklearn.neighbors import KNeighborsClassifier
# # # from sklearn.svm import SVC
# from sklearn.naive_bayes import GaussianNB

# # # model dictionary
# # # models = {
# # #     'logisticRegression' : LogisticRegression(max_iter=1000,random_state=42),
# # #     'decisionTree' : DecisionTreeClassifier(),
# # #     'randomForest' : RandomForestClassifier(),
# # #     'KNN' : KNeighborsClassifier(),
# # #     'svm' : SVC(),
# # #     'naviebayes' : GaussianNB()
# # # }
# from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
# # # for name,model in models.items():
# # #     model.fit(x_train,y_train)
# # #     predict = model.predict(x_test)
# # #     accuracy = accuracy_score(y_test,predict)
# # #     print(name , ' : ',accuracy*100)

# # # logisticRegression  :  80.32786885245902
# # # decisionTree  :  75.40983606557377
# # # randomForest  :  85.24590163934425
# # # KNN  :  63.934426229508205
# # # svm  :  59.01639344262295
# # # naviebayes  :  85.24590163934425

# # # taking randomForest and naviebayes

# # # try with scaling

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# # scaling only on training data to prevent from leakage
# x_train_scaler = scaler.fit_transform(x_train)
# # transform test data based on training fit
# # # here fit is not written because to use same statistics of x_train mean and sd to x_test data too

# import seaborn as sns
# x_test_scaler = scaler.transform(x_test)
# # # for name,model in models.items():
# # #     model.fit(x_train_scaler,y_train)
# # #     predict = model.predict(x_test_scaler)
# # #     accuracy = accuracy_score(y_test,predict)
# # #     print(name , ' : ',accuracy*100)
# # #     print("classification report : ",classification_report(y_test,predict))
# # #     cm = confusion_matrix(y_test,predict)
# # #     plt.figure(figsize=(60,40))
# # #     sns.heatmap(cm,annot=True,cmap='coolwarm',fmt='d')
# # #     plt.xlabel('predicted')
# # #     plt.ylabel('actual')
# # #     plt.title(' Confusion matrix')
# # #     plt.show()

# # # logisticRegression  :  77.04918032786885
# # # classification report :                precision    recall  f1-score   support

# # #            0       0.88      0.66      0.75        32
# # #            1       0.70      0.90      0.79        29

# # #     accuracy                           0.77        61
# # #    macro avg       0.79      0.78      0.77        61
# # # weighted avg       0.79      0.77      0.77        61

# # # decisionTree  :  68.85245901639344
# # # classification report :                precision    recall  f1-score   support

# # #            0       0.70      0.72      0.71        32
# # #            1       0.68      0.66      0.67        29

# # #     accuracy                           0.69        61
# # #    macro avg       0.69      0.69      0.69        61
# # # weighted avg       0.69      0.69      0.69        61

# # # randomForest  :  83.60655737704919
# # # classification report :                precision    recall  f1-score   support

# # #            0       0.89      0.78      0.83        32
# # #            1       0.79      0.90      0.84        29

# # #     accuracy                           0.84        61
# # #    macro avg       0.84      0.84      0.84        61
# # # weighted avg       0.84      0.84      0.84        61

# # # KNN  :  73.77049180327869
# # # classification report :                precision    recall  f1-score   support

# # #            0       0.79      0.69      0.73        32
# # #            1       0.70      0.79      0.74        29

# # #     accuracy                           0.74        61
# # #    macro avg       0.74      0.74      0.74        61
# # # weighted avg       0.74      0.74      0.74        61

# # # svm  :  78.68852459016394
# # # classification report :                precision    recall  f1-score   support

# # #            0       0.83      0.75      0.79        32
# # #            1       0.75      0.83      0.79        29

# # #     accuracy                           0.79        61
# # #    macro avg       0.79      0.79      0.79        61
# # # weighted avg       0.79      0.79      0.79        61

# # # naviebayes  :  85.24590163934425
# # # classification report :                precision    recall  f1-score   support

# # #            0       0.87      0.84      0.86        32
# # #            1       0.83      0.86      0.85        29

# # #     accuracy                           0.85        61
# # #    macro avg       0.85      0.85      0.85        61
# # # weighted avg       0.85      0.85      0.85        61


# # # selects naviebayes which has higher precision and recall compared to all others
# name = 'Navie_bayes'
# model = GaussianNB()
# model.fit(x_train_scaler,y_train)
# predict = model.predict(x_test_scaler)
# accuracy = accuracy_score(y_test,predict)
# print(name," : ",accuracy)
# print('classification report : ',classification_report(y_test,predict))
# cm = confusion_matrix(y_test,predict)
# plt.figure(figsize=(30,30))
# sns.heatmap(cm,annot=True,cmap='Blues',fmt='d')
# plt.xlabel('predict')
# plt.ylabel('actual')
# plt.title('confusion matrix')
# plt.show()

# import joblib
# joblib.dump(model,'heart_prediction.pkl')

# import joblib
# model = joblib.load('heart_prediction.plk')
# new_patient = [[54,0,2,110,214,0,1,158,0,1.6,1,0,2]]
# predict = model.predict(new_patient)
# print(predict)
# if the target value is name then use label ecoder invers transformer
# disease = encoder.inverse_transform(predict)
# print(disease)