from django.shortcuts import render
import os
from .forms import CorporaForm


def project(engfile, hindifile):
    import random

    import numpy as np
    from collections import defaultdict

    vector_length = 200

    # engfile = 'ir_english .txt'
    # hindifile = 'ir_hindi.txt'

    def finding_ascii_value(str1):
        val = ""
        for i in str1:
            val = val + str(ord(i))
        return int(val)

    def getIndexVector(i):
        binary = list(bin(i))
        s = []
        for i in range(2, len(binary)):
            s.append(int(binary[i]))
        rl = vector_length - len(s)
        temp = [1] * rl
        s = temp + s
        return s

    def getFirstChar(sentence):
        sentence = sentence.strip()
        if len(sentence) > 0:
            s = sentence[0]
            # s = ''
            for i in range(len(sentence)):
                if sentence[i] == ' ':
                    try:
                        s = s + sentence[i + 1]
                    except IndexError:
                        s = s + 'a'
                    finally:
                        s = s + 'a'

            return s.lower()
        else:
            return ' '

    dict1 = defaultdict(list)
    sentence_random_vector = {}
    cv_each_word = {}
    punctuation = [',', '"', "''", "\n", "!", "-", ]
    file = open(engfile, 'r')
    content = file.read()
    file.close()

    for i in punctuation:
        content = content.replace(i, '')

    content = content.lower().split(".")

    # words in sentence
    for i in range(len(content)):
        sen = content[i]
        sen = sen.strip()
        sen = sen.split(" ")
        for word in sen:
            dict1[word].append(i)

    # for i in range(len(content)):
    #     sentence_random_vector[i] = getIndexVector(i)
    c = 0
    for sen in content:
        li = []
        comp = getFirstChar(sen)
        asci = finding_ascii_value(comp)

        for k in range(vector_length):
            random.seed(asci)
            li.append(random.randint(-1, 1))
            asci = asci + 1
        sentence_random_vector[c] = li
        c += 1

    # print(sentence_random_vector)
    # print(dict1)
    for word in dict1.keys():
        temp = [0] * vector_length
        for i in dict1[word]:
            temp = np.add(temp, sentence_random_vector[i])
        cv_each_word[word] = temp

    # For hindi document

    dict1_hindi = defaultdict(list)
    cv_each_word_hindi = {}
    file_hindi = open(hindifile, 'r', errors='ignore')
    content_hindi = file_hindi.read()
    for i in punctuation:
        content_hindi = content_hindi.replace(i, '')
    content_hindi = content_hindi.split("।")

    # words in sentence
    for i in range(len(content_hindi)):
        sen = content_hindi[i]
        sen = sen.split(" ")
        for word in sen:
            dict1_hindi[word].append(i)

    for word in dict1_hindi.keys():
        temp = [0] * vector_length
        for i in dict1_hindi[word]:
            temp = np.add(temp, sentence_random_vector[i])
        cv_each_word_hindi[word] = temp

    final_result_dict = {}

    for i in cv_each_word:
        result = {}
        for j in cv_each_word_hindi:
            # print(i, j)
            result[j] = np.dot(cv_each_word[i], cv_each_word_hindi[j]) / (
                    np.linalg.norm(cv_each_word[i]) * np.linalg.norm(cv_each_word_hindi[j]))
        final_result_dict[i] = result

    for i in final_result_dict:
        final_result_dict[i] = sorted(final_result_dict[i].items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    # print(sentence_random_vector)
    final_list = []
    for i in final_result_dict:
        i_list = [i]
        # print(i, end="--->>")
        for j in range(5):
            i_list.append(final_result_dict[i][j][0])
            # print(final_result_dict[i][j][0], end=' | ')
        # print()
        final_list.append(i_list)
    return final_list


# project('deepesh_english.txt','deepesh_hindi.txt')


def getFiles(request):
    if request.method == 'POST':
        corpora = CorporaForm(request.POST, request.FILES)

        if corpora.is_valid():
            corpora_object = corpora.save(commit=True)
            print(corpora_object.lang1)
            english = 'media/' + str(corpora_object.lang1)
            hindi = 'media/' + str(corpora_object.lang2)
            final_list = project(english, hindi)
            os.remove(english)
            os.remove(hindi)
            return render(request, 'home/table.html', {'final_list': final_list})

            # return HttpResponse("File uploaded successfuly")  
    else:
        corpora = CorporaForm()
        return render(request, "home/home.html", {'form': corpora})
