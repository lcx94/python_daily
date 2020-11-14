# -*- coding:utf-8 _*-
'''
@author: lcx
@file: data-process.py
@time: 2020/11/14 15:10
@desc:  AI专利报告数据处理

'''

import cx_Oracle as cx

import os
os.environ['path'] = r'D:\navicat\Navicat Premium 12\instantclient_12_2'

conn = cx.connect('PATSTAT_GROUP2', 'D7zVwMR8', 'db.imcluster.cc:1521/patstat2020a')
cursor = conn.cursor()
cursor.execute('SELECT * FROM PATSTAT2020A.AI_PAT_TITLE')


def get_data():
    data = cursor.fetchmany(10)
    count = 0
    while count <= 200000 and data is not None:
        data = cursor.fetchmany(10)
        do_calculate(data, count)
        count += 1
    cursor.close()
    conn.close()


def do_calculate(data, count):
    # 统计总体数据缺失
    statistic_all(data, count)
    # 统计分类情况
    # statistic_class(data)
    # 统计和IPC表的交集、差集情况
    # statistic_IPC(data)
    # 验证抽取准确率的问题   抽样10
    statistic_TITLE(data[0][1], count)


total_number = 0
total_loss_title = 0
total_short_title = 0
short_title_list = []
def statistic_all(data, count):
    global total_number
    global total_loss_title
    global total_short_title
    global short_title_list
    for item in data:
        total_number += 1
        if item[0] and not item[1]:
            total_loss_title += 1
        if item[0] and len(item[1]) < 16:
            total_short_title += 1
            short_title_list.append(item[1])
    # title 缺失率：
    title_loss_rate = total_loss_title/total_number * 100
    # short title rate
    short_title_rate = total_short_title/total_number * 100
    if count == 200000:
        print('-----total title list length is {}------'.format(total_number))
        print('-----title loss rate is ------{}%======'.format(round(title_loss_rate, 3)))
        print('-----short title rate is ------{}%======'.format(round(short_title_rate, 3)))
        print('-----short title list length is {}------'.format(len(short_title_list)))
        print(short_title_list)


title_list = [
        'artificial Intelligence',
        'AI',
        'Depth learning',
        'Natural language processing',
        'Computer vision',
        'Gesture control',
        'expert system',
        'Intelligent search',
        'Smart Search',
        'smart robot',
        'intelligent robot',
        'Machine learning',
        'Speech Recognition',
        'PATTERN IDENTIFY',
        'PATTERN RECOGNIT',
        'intelligent processor',
        'sound',
        'voice',
        'speech',
        'audio',
        'Video',
        'Image',
        'process',
        'synthesis',
        'recognit',
        'identif',
        'Code',
        'analys',
        'interact',
        'assess',
        'Evaluat',
        'enhance',
        'Text to Speech',
        'man-machine',
        'dialog',
        'conversation',
        'interact',
        'voiceprint',
        'sound groove',
        'recognit',
        'identif',
        'vision',
        'visual',
        'biometric',
        'biologic',
        'face',
        'facial',
        'expression',
        'Fingerprint',
        'Iris',
        'hand vein',
        'Behavior',
        'Human',
        'gesture',
        'object',
        'recognit',
        'identif',
        'gesture control',
        'video',
        'recognit',
        'identif',
        'abstract',
        'synopsis',
        'handwrit',
        'character',
        'text',
        'word',
        'recognit',
        'identif',
        'eye track',
        'image',
        'picture',
        'process',
        'identif',
        'classif',
        'Restore',
        'recover',
        'SLAM',
        'simultaneous localization and map',
        'Concurrent Mapping and Localization',
        '3-D',
        'three-dimensional',
        'scan',
        'reconstruct',
        'Natural Language Process',
        'NLP',
        'Natural language generation',
        'NLG',
        'Natural language interact',
        'Natural language understand',
        'knowledge domain',
        'knowledge map',
        'CORPUS',
        'semantic',
        'understand',
        'comprehens',
        'analys',
        'computation',
        'text',
        'document',
        'linguistic',
        'mining',
        'analysProcess',
        'translat',
        'computer',
        'machine',
        'information',
        'retriev',
        'extract',
        'Multi-document summariz',
        'Automatic summariz',
        'linguistic',
        'language',
        'model',
        'Knowledge Reasoning',
        'knowledge inference',
        'Semi-Supervised Learn',
        'Density-based',
        'Hierarchical',
        'Fuzzy',
        'cluster',
        'Dimensionality reduction algorithm',
        'Linear',
        'nonlinear',
        'dimensionality reduction',
        'regress',
        'Apriori',
        'eclat',
        'fp-grouth',
        'Collaborative filtering',
        'algorithm',
        'Supervised learn',
        'unsupervised learn',
        'neural network',
        'Bayes Classif',
        'Support Vector Machine',
        'Decision tree',
        'Decision stump',
        'k nearest neighbor',
        'knn classification',
        'Logistic Regression',
        'Least squares regression',
        'Classification and regression tree',
        'CART',
        'Linear Discriminant',
        'Kernelized Linear Discriminant',
        'KLDA',
        'LDA',
        'Collaborative training algorithm',
        'kernel regression',
        'Spectral Clustering',
        'minimum cut',
        'policy iteration',
        'Deep',
        'depth',
        'Transfer',
        'Ensemble',
        'prior',
        'reinforcement',
        'intensive',
        'learning',
        'Generative adversarial network',
        'numeric optimization',
        'Heterogeneous Computing',
        'large-scale distributed computing',
        'cognitive computing',
        'Support Vector Machine',
        'Expectation Maximization',
        'AdaBoost',
        'metric learning',
        'outlier detect',
        'causality analysi',
        'Ordinary Least Square',
        'Logistic Regression',
        'Stepwise Regression',
        'Multivariate Adaptive Regression Splines',
        'Locally Estimated Scatterplot Smoothing',
        'Learning Vector Quantization',
        'Self-Organizing Map',
        'Ridge Regression',
        'Least Absolute Shrinkage and Selection Operator',
        'Elastic Net',
        'Iterative Dichotomiser 3',
        'ID3',
        'Chi-squared Automatic Interaction Detection',
        'Random Forest',
        'Decision Stump',
        'Gradient Boosting Machine',
        'Bayesian Belief Network',
        'Averaged One-Dependence Estimators',
        'Radial Basis Function',
        'k-Means',
        'Back Propagation',
        'Hopfield',
        'Self-Organizing Map',
        'Learning Vector Quantization',
        'Restricted Boltzmann Machine',
        'Deep Belief Networks',
        'Convolutional Network',
        'Stacked Auto-encoders',
        'Principle Component Analysis',
        'Partial Least Square Regression',
        'Multi-Dimensional Scaling',
        'Projection Pursuit',
        'Random Forest',
        'Gradient Boosting Machine',
        'anomaly detect',
        'PCA',
        'principal component analysis',
        'principal component regress',
        'recommend system',
        'recommend engine',
        'large scale machine learn',
        'Learning Curve',
        'error analys',
        'celling analys',
        'tensorflow',
        'theano',
        'keras',
        'transfer learn',
        'bootstrap aggregat',
        'factor analys',
        'learn automata',
        'adversarial network',
        'bias vairance',
        'CNN',
        'Convolution Neural Network',
        'Deep Neural Networks',
        'DNN',
        'Back Propagation',
        'generative model',
        'co-training',
        'low-density separat',
        'temporal difference learn',
        'self organizing map',
        'hierachical cluster',
        'birch',
        'dbscan',
        'perception',
        'learning machine',
        'bayesian',
        'intelligent sensor',
        'smart sensor',
        'smart chip',
        'Intelligent Chip',
        'AI chip',
        'artificial intelligent chip',
        'GPU',
        'FPGA',
        'ASIC',
        'brain-inspired chip',
        'brain like chip',
        'neuromorphic chip',
        'intelligent hardware',
        'AI hardware',
        'smart hardware',
        'sentiment analysi',
        'motion control',
        'Context Aware',
        'cognitive context',
        'affective',
        'affection',
        'emotion',
        'comput',
        'interact',
        'model',
        'classify',
        'synthesis',
        'express',
        'identify',
        'recognit',
        'understand',
        'comprehens',
        'feedback',
        'transfer',
        'annotation',
        'tag',
        'segment',
        'artificial emotion',
        'intelligent interact',
        'affective dialogue',
        'affective lexicon',
        'kansei engineering',
        'affective neuroscience',
        'affective ontology',
        'intelligent',
        'automatic',
        'man-machine',
        'system',
        'Question Answer',
        'Text Classif',
        'Text Cluster',
        'SYNTACTIC ANALYS',
        'automatic summariz',
        'question answer',
        'information filter',
        'information extract',
        'public opinion analys',
        'metaphorical comput',
        'automatic proofread',
        'driving'
    ]
title_statistic = dict.fromkeys(title_list, 0)
not_found_title = []
def statistic_TITLE(title, count):
    global title_statistic
    global not_found_title
    title_upper = title.upper()
    # 标识 title 与检索词是匹配的
    is_in_keywords = False
    for item in title_list:
        item_upper = item.upper()
        if item_upper in title_upper:
            title_statistic[item] += 1
            # 找到了对应的检索词
            is_in_keywords = True
    if not is_in_keywords:
        # 当前title不在tile list 中
        not_found_title.append(title)
    title_statistic_list = []
    for dic in title_statistic.items():
        title_statistic_list.append(dic)
    title_statistic_list.sort(key=lambda k: k[1], reverse=True)
    # 最多 最少 的十个检索词
    if count == 200000:
        max_ten_list = title_statistic_list[:10]
        min_ten_list = title_statistic_list[-10:]
        print('=====the max ten classes of AI title is =========')
        print(max_ten_list)
        print('=====the min ten classes of AI title is =========')
        print(min_ten_list)
        # 没有内容的所有检索词
        empty_list = []
        for item in title_statistic_list:
            if item[1] == 0:
                empty_list.append(item)
        print('=====the empty list of AI search keywords is =======')
        print(empty_list)
        print('=====not found title number is =========')
        print(len(not_found_title))



if __name__ == '__main__':
    get_data()
