import gensim
import pandas as pd
import os
import string
import matplotlib as mpl
import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import nltk
from gensim.utils import tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string as s
import re
import pickle
import gensim.corpora as corpora
from emot.emo_unicode import UNICODE_EMOJI, EMOTICONS_EMO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.feature_selection import mutual_info_classif
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

from sklearn.model_selection import cross_val_score

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import os

# mpl.use('TkAgg')  # !IMPORTANT

all_emojis = []
all_emoticons = []

#combine and drop datasets
def create_dataset(file_list, dataset_descriptions):
    for file in file_list:
                if file == '.DS_Store':
                    continue
                df_temp = pd.read_csv(file_path_metadata + file)
                dataset_descriptions = dataset_descriptions.append(df_temp, ignore_index=True)

    if not dataset_descriptions.empty:
        dataset_descriptions = dataset_descriptions.drop_duplicates('videoId', keep='last')

    dataset_descriptions = dataset_descriptions.reset_index(drop=True)

    dataset_descriptions.to_csv("../data/Thesis-Dataset/Combined/Combined_metadata.csv")
    dataset_descriptions = dataset_descriptions.drop(['Unnamed: 0'], axis=1)

    #print(dataset_descriptions)

    return dataset_descriptions



#Data preprocessing
def remove_punctuation(text):
    txt_nopunct="".join([c for c in text if c not in string.punctuation])
    return txt_nopunct


def convert_to_lowercase(text):
    text = text.lower()
    return text


# Function for converting emojis into word
def convert_emojis(text):
    for emot in UNICODE_EMOJI:
        if emot in text:
            text = text.replace(emot, " "+"_".join(UNICODE_EMOJI[emot].replace(","," ").replace(":","").split())+" ")
            all_emojis.append(UNICODE_EMOJI[emot])
    return text


# Function for converting emoticons into word
def convert_emoticons(text):
    for emot in EMOTICONS_EMO:
        if emot in text:
            text = text.replace(emot, " "+"_".join(EMOTICONS_EMO[emot].replace(",","").replace(":","").split())+" ")
            all_emoticons.append(EMOTICONS_EMO[emot])
    return text


def tokenization(text):
    text_list = text.split()
    return text_list


def remove_stopwords(text_list):
    stop = stopwords.words('english')
    new_list=[]
    for i in text_list:
        if i not in stop:
            new_list.append(i)
    return new_list


def remove_spaces(text_list):
    new_list=[]
    for i in text_list:
        i=i.strip()
        new_list.append(i)
    return new_list

#topic-modelling results are printed in the terminal
def topic_modeling(X_train, X_test):

    X_train = X_train.apply(tokenization)
    X_train = X_train.apply(remove_stopwords)

    # Create Dictionary
    id2word = corpora.Dictionary(X_train)
    # Create Corpus
    texts = X_train
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    print([[(id2word[id], freq) for id, freq in cp] for cp in corpus[:1]])

    # number of topics
    num_topics = 10
    # Build LDA model
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)
    # Print the Keyword in the 10 topics
    print(lda_model.print_topics())

    return lda_model

#clustering implementation
def text_clustering(X_train, X_test):

    #id2word = corpora.Dictionary(X_train)

    X_train = X_train.apply(tokenization)
    X_train = X_train.apply(remove_stopwords)

    vectorizer = TfidfVectorizer()
    #X = vectorizer.fit_transform([','.join(map(str, l)) for l in X_train])
    X = vectorizer.fit_transform([','.join(map(str, l)) for l in X_train])

    model = gen_model(X, 6)

    # to get centroid and features

    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()

    # Printing in the cluster they belong
    '''
    for i in range(3):
        print(" Cluster : " + str(i)),
        for ind in order_centroids[i, :10]:
            print(terms[ind])'''

    #print("\n")
    #print("Prediction")
    #print("Title to test:", ([','.join(map(str, l)) for l in X_test]))

    X_test = X_test.apply(tokenization)
    X_test = X_test.apply(remove_stopwords)
    X = vectorizer.transform([','.join(map(str, l)) for l in X_test])
    data = load_digits().data
    pca = PCA(2)

    # Transform the data
    df = pca.fit_transform(data)


    predicted = model.fit_predict(df)

    # Getting unique labels

    u_labels = np.unique(predicted)
    #for i in u_labels:
     #   plt.scatter(df[predicted == i, 0], df[predicted == i, 1], predicted=i)
    #plt.legend()
    #plt.show()


    # Load Data


    # plotting the results:
    # filter rows of original data
    filtered_label0 = df[predicted == 0]
    filtered_label1 = df[predicted == 1]
    filtered_label2 = df[predicted == 2]

    print("Filtered Label 0 is", filtered_label0)

    # plotting the results
    plt.scatter(filtered_label0[:, 0], filtered_label0[:, 1], color='red')
    plt.scatter(filtered_label1[:, 0], filtered_label1[:, 1], color='black')
    plt.scatter(filtered_label2[:, 0], filtered_label2[:, 1], color='blue')
    plt.show()

    return predicted

#Kmeans-clusters model
def gen_model(X, n_clusters, init='k-means++', max_iter=100, n_init=1):
    print(n_clusters)
    model = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=max_iter, n_init=n_init)
    model.fit(X)
    return model

#function to perform supervised classification
def classify(test):
    train = pd.read_csv('/Users/tabziasmac/Downloads/Thesis-Dataset/Training_dataset_02272023.csv')
    val = pd.read_csv('/Users/tabziasmac/Downloads/Thesis-Dataset/Validation_dataset_02272023.csv')

    '''
    train['Title_Description'] = train['Title_Description'].apply(tokenization)
    val['Title_Description'] = val['Title_Description'].apply(tokenization)
    test['Title_Description'] = test['Title_Description'].apply(tokenization)

    train['Title_Description'] = train['Title_Description'].apply(remove_stopwords)
    val['Title_Description'] = val['Title_Description'].apply(remove_stopwords)
    test['Title_Description'] = test['Title_Description'].apply(remove_stopwords)

    train['Title_Description'] = train['Title_Description'].apply(remove_spaces)
    val['Title_Description'] = val['Title_Description'].apply(remove_spaces)
    test['Title_Description'] = test['Title_Description'].apply(remove_spaces)
    '''

    print(train.groupby('category').Title_Description.count())

    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 3), stop_words='english')
    #print(train['Title_Description'])
    features = tfidf.fit_transform(train['Title_Description']).toarray()
    labels = train.category
    print(features.shape)

    category_to_id = {'Unrelated': 0, 'Donkey_Path': 1, 'Dunki_Movie':2}
    print(category_to_id.items())

    N = 2
    for category, category_id in category_to_id.items():
        features_chi2 = chi2(features, labels == category_id)
        indices = np.argsort(features_chi2[0])
        feature_names = np.array(tfidf.get_feature_names_out())[indices]
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
        trigrams = [v for v in feature_names if len(v.split(' ')) == 3]
        print("# '{}':".format(category))
        print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-5:])))
        print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-5:])))
        print("  . Most correlated trigrams:\n. {}".format('\n. '.join(trigrams[-5:])))

    X_train = train['Title_Description']
    X_test = test['Title_Description']
    X_val = val['Title_Description']
    y_val = val['category']
    y_test = test['category']
    y_train = train['category']

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = MultinomialNB().fit(X_train_tfidf, y_train)

    val_set = count_vect.transform(X_val)
    predictions  = clf.predict(val_set)
    #print(clf.predict(val_set))

    predictions = pd.Series(predictions)

    print(type(y_val))
    print(type(predictions))
    correct_count = 0
    for i in range(0,len(y_val) -1):
        if y_val[i] == predictions[i]:
            correct_count += 1
        else:
            print("Original Label of " + str(X_val[i]) + " was: " + str(y_val[i]))
            print("Prediction of " + str(X_val[i]) + " is: " + str(predictions[i]))

    print(classification_report(y_val, predictions))

    accuracy = correct_count / len(y_val)
    print("Accuracy is:", accuracy)

    test_set_prediction = count_vect.transform(X_test)
    test_predictions = pd.Series(clf.predict(test_set_prediction))
    print(test_predictions)

    #predictions = pd.Series(predictions)

    y_test = test_predictions
    print(type(test_predictions))
    #for i in test_predictions:

    test['preds'] = test_predictions.values

    test.to_csv(r''
                r'Test_results_classifier_03112023.csv')

    #print(clf.predict(count_vect.transform([ "This company refuses to provide me verification and validation of debt per my right under the FDCPA. I do not believe this debt is mine."])))

if __name__ == '__main__':
    dataset_descriptions = pd.DataFrame()
    file_path_metadata = "/Users/tabziasmac/Downloads/Thesis-Dataset/Metadata/"
    # list all the files from the directory
    file_list = os.listdir(file_path_metadata)
    i = 0

    #create_dataset
    #dataset_descriptions = create_dataset(file_list, dataset_descriptions)

    dataset_descriptions = pd.read_csv('/Users/tabziasmac/Downloads/Thesis-Dataset/Combined/Combined_metadata_comments.csv')
    dataset_descriptions = dataset_descriptions.dropna()

    dataset_descriptions = dataset_descriptions[dataset_descriptions.columns.drop(list(dataset_descriptions.filter(regex='Unnamed:')))]
    dataset_descriptions['Title_Desc_Comm'] = dataset_descriptions['title'].astype(str) + "  " + dataset_descriptions['description'].astype(str) + "  " + dataset_descriptions['new_comment']
    #classification_dataset = dataset_descriptions[['videoId', 'title', 'description']]
    '''
    category = [0] * classification_dataset.shape[0]
    classification_dataset['category'] = category

    classification_dataset['Title_Description'] = classification_dataset['title'].astype(str) + "  " + classification_dataset['description']

    print(classification_dataset['Title_Description'])

    X = classification_dataset[['Title_Description', 'videoId']]
    y = classification_dataset['category']
    
    '''

    # Import the wordcloud library
    from wordcloud import WordCloud

    # Join the different processed titles together.
    #long_string = ','.join(list(classification_dataset['Title_Description'].values))
    long_string = ','.join(list(dataset_descriptions['Title_Desc_Comm'].values))
    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
    # Generate a word cloud
    wordcloud.generate(long_string)
    # Visualize the word cloud
    image = wordcloud.to_image()
    image.show()

    # the following needs to be run during classification ONLY
    '''
    
    print((classification_dataset).shape)
    print(len(X))
    train = classification_dataset.sample(frac=0.8, random_state=200)
    train_1 = train
    test = classification_dataset.drop(train.index)
    train = train_1.sample(frac=0.75, random_state=200)
    val = train_1.drop(train.index)

    train['Title_Description'] = train['Title_Description'].apply(remove_punctuation)
    val['Title_Description'] = val['Title_Description'].apply(remove_punctuation)
    test['Title_Description'] = test['Title_Description'].apply(remove_punctuation)

    train['Title_Description'] = train['Title_Description'].apply(convert_to_lowercase)
    val['Title_Description'] = val['Title_Description'].apply(convert_to_lowercase)
    test['Title_Description'] = test['Title_Description'].apply(convert_to_lowercase)

    train['Title_Description'] = train['Title_Description'].apply(convert_emojis)
    val['Title_Description'] = val['Title_Description'].apply(convert_emojis)
    test['Title_Description'] = test['Title_Description'].apply(convert_emojis)

    train['Title_Description'] = train['Title_Description'].apply(convert_emoticons)
    val['Title_Description'] = val['Title_Description'].apply(convert_emoticons)
    test['Title_Description'] = test['Title_Description'].apply(convert_emoticons)

    #train.to_csv(r'/Users/tabziasmac/Downloads/Thesis-Dataset/Training_dataset_02272023_duplicate.csv')
    #val.to_csv(r'/Users/tabziasmac/Downloads/Thesis-Dataset/Validation_dataset_02272023.csv')


    #docLDA= topic_modeling(train['Title_Description'], test['Title_Description'])

    #print("Document LDA is:", docLDA)'''

    dataset_descriptions['Title_Desc_Comm'] = dataset_descriptions['Title_Desc_Comm'].apply(remove_punctuation)
    dataset_descriptions['Title_Desc_Comm'] = dataset_descriptions['Title_Desc_Comm'].apply(convert_to_lowercase)
    dataset_descriptions['Title_Desc_Comm'] = dataset_descriptions['Title_Desc_Comm'].apply(convert_emojis)
    dataset_descriptions['Title_Desc_Comm'] = dataset_descriptions['Title_Desc_Comm'].apply(convert_emoticons)

    y_test= text_clustering(dataset_descriptions['Title_Desc_Comm'], dataset_descriptions['Title_Desc_Comm'])
    print(y_test)

    test_2 = y_test

    test_2['preds'] = y_test
    test_2.to_csv(r'Test_results_cluster_03112023.csv')

    #to perform classification
    #classify(test)

    #print("All Emojis are:", set(all_emojis))
    #print("All Emoticons are:", all_emoticons)































