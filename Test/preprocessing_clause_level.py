import urllib
import urllib.request
import re
import nltk.data
from nltk.tag import pos_tag
from bisect import bisect_left
# TotalCount

TotalCount=0
def main(count):
    # theurl = "http://www.espncricinfo.com/england-v-sri-lanka-2014/content/story/753287.html"
    # content(theurl)
    line_number = 1
    s1 = ""
    entities = set()
    entities = {'shakib', 'sakib', 'sakibs', 'salib', 'shakid'}
    # entities = {'lankan', 'lanka', 'kusal', 'sanga', 'thiri', 'upul', 'tharanga', 'sl', 'srilanka', 'bangladesh', 'ireland',
    #             'dil', 'jaya', 'mathews', 'kulasekara', 'thisara', 'sachithra', 'kula', 'australia', 'johnson'
    #             'jayasuriya', 'murtagh', 'kushal', 'irish'}
    # with open('ODIComments.txt', encoding='utf-8') as a_file:

    import openpyxl
    wb = openpyxl.load_workbook('shakib_comments.xlsx')
    sheet = wb.active
    global TotalCount
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    clauses = []
    while(TotalCount <= count):
        TotalCount += 1
        s = '''Fall of one and rise of another seem fit to describe Pandya brothers. Hardik was drafted into the side not long ago with all sorts of comarisons to good current day allrounders, documentaries aired about his fairy tale of finding the pinnacle and limelight, influential binny was sent home but Hardik has lost his aroma too fast. On the other hand his brother looks a much better prospect both with the bat and the ball. Bumrah continues to impress and I hope he will be given an opportunity to perform outside India and pitches will not made placid to support indian batsmen. I am sure Gambhir will make his way to indian side again to add experience on the back of this IPL season. He seems to be more motivated by the downfall of Dhawan
'''
        # a_line = sheet["B"+str(TotalCount)].value
        # # for a_line in a_file:
        # # for a_line in test_comment:
        # if a_line is not None:
        #     s = a_line.strip()
        # # print("test: " + s)
        # if(s==""):
        #     continue
        # if (s != " "):
        try:
            text = tokenizer.tokenize(s)        # break big comments into separate sentences
            num=0
            clauses += [""]
            for t in text:
                t = re.split('\s+', t)          # removing extra spaces between words
                t = ' '.join(t)
                num += 1
                print(str(num))
                print(t)

                tags = pos_tag(t.split())
                print(tags)                     # part-of-speech tags by nltk
                verb_in_clause = False          # verb present in current clause so far?
                cur_entity = ""                 # entity/entities mentioned in current clause so far
                pronoun_in_clause = False       # third-person pronoun in current clause so far?
                comma_found = False             # comma found in current clause so far?
                clause_starts = 0               # index where current clause starts
                cur_index = 0                   # index of t currently
                tags_index=-1
                verbs_at = []
                commas_at = []
                connecting_words_at = []
                for word,pos in tags:
                    tags_index += 1
                    if pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ':
                        verbs_at += [tags_index]
                    if word.endswith(','):
                        commas_at += [tags_index]
                    if pos == 'CC':
                        connecting_words_at += [tags_index]

                tags_index = -1
                for word,pos in tags:
                    tags_index += 1
                    if word[len(word)-1] == ',':
                        comma_found = True
                    word_original = word.strip(",'\".()!?").lower()
                    if word_original.endswith("'s"):
                        word_original = word_original[:-2]                  # the base form of the word e.g. "shakib", "player" instead of
                                                                                                            # "shakib's", "player,"
                    if pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ':
                        verb_in_clause = True
                        verb = word_original            # current word is a verb
                        if comma_found:
                            comma_found = False         # comma itself can't determine clause length if a verb appears after comma
                    elif (pos == 'PRP' or pos == 'PRP$')and (word_original == "he" or word_original == "him" or word_original == "his"
                                                             or word_original == "they" or word_original == "them" or word_original == "their"):
                        pronoun_in_clause = True
                    elif word_original in entities:
                        if(cur_entity == ""):
                            cur_entity = word_original
                        elif word_original not in cur_entity:
                            cur_entity += ", " + word_original

                    # print("tags_index: " + str(tags_index))
                    if tags_index == len(tags)-3:         #last clause in text, can't make a new clause later on with just a few words left

                        clause = t[clause_starts:].strip(',')
                        clauses += [clause]
                        if(cur_entity != ""):
                            print(cur_entity.upper() + ": " + clause)
                        elif (pronoun_in_clause):
                            print("pronoun: " + clause)
                        else:
                            print("indirect_context: " + clause)

                    elif comma_found or verb_in_clause:
                        # print("cur_word: " + word)
                        if word_original == 'that' and tags_index+1 != len(tags) and tags[tags_index+1][1] == 'NN':     # e.g. "that boy" -> can't end clause at 'that'
                            cur_index += len(word)+1                # updating current index for next iteration
                            continue
                        if (comma_found and pos_tag(t[clause_starts:].split()[0].split())[0][1] == 'IN') or (comma_found and verb_in_clause):
                            #verb present or clause starts with preposition
                                # print(word)
                                if (((tags_index>0 and tags[tags_index-1][1][:2] == 'JJ') or (tags_index>1 and tags[tags_index-2][1][:2] == 'JJ') or (tags_index>2 and tags[tags_index-3][1][:2] == 'JJ'))
                                   and (tags_index+1 < len(tags) and tags[tags_index+1][1] != 'VB' and tags[tags_index+1][1] != 'VBG' and tags[tags_index+1][1] != 'VBD' and tags[tags_index+1][1] != 'VBN' and tags[tags_index+1][1] != 'VBP' and tags[tags_index+1][1] != 'VBZ')):
                                        cur_index += len(word)+1
                                        comma_found = False
                                        continue
                                clause_ends = cur_index + len(word_original)
                                clause = t[clause_starts:clause_ends].strip(',')
                                if ((verb_in_clause is False and len(clause.split()) <= 5)
                                        or (verb_in_clause is True and len(clause.split()) <= 1)):                 #too small to be meaningful
                                    cur_index += len(word)+1
                                    comma_found = False
                                    continue
                                clause_starts = clause_ends
                                # clause = clause.lstrip()
                                clauses += [clause]
                                # print("verb: " + verb)
                                print("COMMA")
                                if(cur_entity != ""):
                                    print(cur_entity.upper() + ": " + clause)
                                elif (pronoun_in_clause):
                                    print("pronoun: " + clause)
                                else:
                                    print("indirect_context: " + clause)                # may or may not be connected to previouly mentioned entity
                                verb_in_clause = False
                                verb=""
                                cur_entity = ""
                                pronoun_in_clause = False

                        elif verb_in_clause and ((pos == 'CC' and                            # connecting words like 'and' & 'but' can define new clause
                                                      tags_index+1 < len(tags) and
                                                      (tags[tags_index+1][1] == 'PRP' or tags[tags_index+1][1] == 'VBD'     # if next word is a pronoun or verb
                                                       or tags[tags_index+1][1] == 'VBP' or tags[tags_index+1][1] == 'VBZ'
                                                       or (tags_index!=0 and (tags[tags_index+1][1][:2] != tags[tags_index-1][1][:2]
                                                                              or (tags[tags_index+1][1][:2] == 'NN' and tags[tags_index+1][1] != tags[tags_index-1][1])))))  # if
                                or (pos == 'IN' or pos == 'TO' or pos == 'WDT' or pos == 'WP' or pos == 'WRB' or word_original == 'outside')):              # prepositions can define new clauses too
                            if(word_original == 'like' or word_original == 'in'):
                                cur_index += len(word)+1
                                continue

                            next_connecting_word_at = bisect_left(connecting_words_at, tags_index)

                            if (pos=='CC' and ((tags_index>0 and tags[tags_index-1][1][:2] == 'JJ') or (tags_index>1 and tags[tags_index-2][1][:2] == 'JJ') or (tags_index>2 and tags[tags_index-3][1][:2] == 'JJ'))
                                   and (tags_index+1 < len(tags) and tags[tags_index+1][1] != 'VB' and tags[tags_index+1][1] != 'VBG' and tags[tags_index+1][1] != 'VBD' and tags[tags_index+1][1] != 'VBN' and tags[tags_index+1][1] != 'VBP' and tags[tags_index+1][1] != 'VBZ')):
                                        cur_index += len(word)+1
                                        continue

                            # print(str(tags_index) + " -> " + word)
                            # print("pos0: " + pos + ", pos1: " + tags[tags_index+1][1])
                            next_comma_at = bisect_left(commas_at, tags_index)
                            next_verb_at = bisect_left(verbs_at, tags_index)
                            # print("test1: " + str(next_comma_at))
                            if(next_comma_at < len(commas_at) and commas_at[next_comma_at] > tags_index
                               and  commas_at[next_comma_at] - tags_index <= 5):
                                # print(word)
                                # print("next comma after: " + str(commas_at[next_comma_at] - tags_index))
                                cur_index += len(word)+1
                                continue
                            # print("test2: " + str(next_verb_at))
                            if(next_verb_at < len(verbs_at) and verbs_at[next_verb_at] > tags_index
                               and  verbs_at[next_verb_at] - tags_index <= 2):
                                # print(word)
                                # print("next verb after: " + str(commas_at[next_comma_at] - tags_index))
                                cur_index += len(word)+1
                                continue


                            if (pos == 'IN' or pos == 'TO' or pos == 'WDT' or pos == 'WP' or pos == 'WRB' or word_original == 'outside'):              # prepositions can define new clauses too
                                if ((next_connecting_word_at < len(connecting_words_at) and connecting_words_at[next_connecting_word_at] > tags_index
                                and  connecting_words_at[next_connecting_word_at] - tags_index <= 3)):
                                    cur_index += len(word)+1
                                    continue
                                clause_ends = cur_index
                            else:
                                clause_ends = cur_index+len(word)
                            # print("ends at: " + t[clause_ends:])
                            clause = t[clause_starts:clause_ends].strip(',')
                            if len(clause.split()) <= 5:                        #too small to be meaningful
                                cur_index += len(word)+1
                                continue
                            clause_starts = clause_ends
                            # clause = clause.lstrip()
                            clauses += [clause]
                            # print("verb: " + verb)
                            # print("last word: " + word)
                            if(cur_entity != ""):
                                print(cur_entity.upper() + ": " + clause)
                            elif (pronoun_in_clause):
                                print("pronoun: " + clause)
                            else:
                                print("indirect_context: " + clause)
                            verb_in_clause = False
                            verb=""
                            cur_entity = ""
                            pronoun_in_clause = False

                    comma_found = False

                    cur_index += len(word)+1
                    # print("rest: " + t[cur_index:])
                # propernouns = []
                # pronouns = []
                # num_entities = num_pronouns = 0
                # latest_entity = ""
                # verbs_at = []
                # clauses = []
                # prev_verb_at = 0
                # for word,pos in tags:
                #     if (pos == 'NNP' or pos == 'NN') and word.strip(",'.()!?").lower() in entities:
                #         propernouns.append(word.strip(",'.()!?"))
                #         num_entities += 1
                #         latest_entity = word.strip(",'.()!?")
                #         # print("test: " + latest_entity)
                #     elif pos == 'PRP' or pos == 'PRP$':
                #         num_pronouns += 1
                #         pronouns.append(word.strip(",'.()!?"))
                #     elif pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ':
                #         cur_verb_at = t.rfind(word, prev_verb_at)
                #         verbs_at += [cur_verb_at]
                #         prev_verb_at = cur_verb_at + len(word)
                #     #     print(pos + ": " + word.strip(",'.()!?"))
                # # verbs_at = ', '.join(verbs_at)
                # # print(verbs_at)
                # # for i in range(len(verbs_at)):
                # #     print(t[verbs_at[i]]+ "  ")
                # if(num_entities==0 and num_pronouns > 0):
                #     pronouns = ', '.join(pronouns)
                #     print("pronouns: " + pronouns)
                #     #add current sentiment to latest_entity if latest_entity_sentiment =
                #
                #
                #
                # prev_entity_at = 0
                # start=0
                # for k in propernouns:
                #     # entity_at = propernouns.index(k)
                #     cur_entity_at =  t.rfind(k)
                #     last_comma_at = t.rfind(',', start, cur_entity_at)      ## start or prev_entity_at ??
                #     start = max(last_comma_at, prev_entity_at)
                #     if(start==last_comma_at):
                #         start += 1
                #     if(propernouns.index(k)!=len(propernouns)-1):       #more elements coming
                #         next_entity_at = t.rfind(propernouns[propernouns.index(k)+1])
                #         flag = True
                #         for i in verbs_at:
                #             if(start<=i and i<next_entity_at):
                #                 flag=False
                #                 break
                #         if(flag):               #no verb in this portion of text
                #             continue
                #         print(k + ": " + t[start:next_entity_at].strip())
                #     else:
                #         print(k + ": " + t[start:].strip())
                #
                #     prev_entity_at = cur_entity_at
                # propernouns = ', '.join(propernouns)
                # print(propernouns)
            line_number += 1
            # if(line_number > 100):          # dealing with 100 comments at the moment
            #     print("clauses: " + str(len(clauses)))
            #     for c in clauses:
            #         print(c)
            #     return
            print(str(line_number))
        except Exception as e:
            print("Here " + str(e))
            import sys, os
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
# print("Total Count : ",TotalCount)

    return clauses

main(1)

def test():
    s = "@ncpasan, Jayasuriya came as a bowler and played lower down in the batting order, during the first few years of his career"
    tags = pos_tag(s.split())
    propernouns = [word.strip(",'.()!?") for word,pos in tags if (pos == 'NNP' or pos == 'NN')]
    propernouns = ', '.join(propernouns)
    print(propernouns)



# test()