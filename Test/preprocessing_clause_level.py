import urllib
import urllib.request
import re
import nltk.data
from nltk.tag import pos_tag
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
        # test_comment = ["@Akila93, Are you saying, SL should eliminate an established young player with so much experience, solid international track-record to prove his consistency & skills"]
        a_line = sheet["B"+str(TotalCount)].value
        # for a_line in a_file:
        # for a_line in test_comment:
        if a_line is not None:
            s = a_line.strip()
        # print("test: " + s)
        if(s==""):
            continue
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
                cur_entity = ""                 # enitity/enitities mentioned in current clause so far
                pronoun_in_clause = False       # third-person pronoun in current clause so far?
                comma_found = False             # comma found in current clause so far?
                clause_starts = 0               # index where current clause starts
                cur_index = 0                   # index of t currently
                for word,pos in tags:
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

                    if comma_found or verb_in_clause:
                        # print("cur_word: " + word)
                        if word_original == 'that' and tags.index((word,pos))+1 != len(tags) and tags[tags.index((word,pos))+1][1] == 'NN':     # e.g. "that boy" -> can't end clause at 'that'
                            cur_index += len(word)+1                # updating current index for next iteration
                            continue
                        if (comma_found and pos_tag(t[clause_starts:].split()[0].split())[0][1] == 'IN') or (comma_found and verb_in_clause):
                            #verb present or clause starts with preposition
                                # print(word)
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

                        elif verb_in_clause and ((pos == 'CC' and tags.index((word,pos))+1 != len(tags) and         # connecting words like 'and' & 'but' can define new clause
                                                      (tags[tags.index((word,pos))+1][1] == 'PRP' or tags[tags.index((word,pos))+1][1] == 'VBD'     # if next word is a pronoun or verb
                                                       or tags[tags.index((word,pos))+1][1] == 'VBP' or tags[tags.index((word,pos))+1][1] == 'VBZ'))
                                or (pos == 'IN' or pos == 'TO' or pos == 'WDT' or pos == 'WP' or pos == 'WRB' or word_original == 'outside')):              # prepositions can define new clauses too
                            if(word_original == 'like'):
                                cur_index += len(word)+1
                                continue
                            clause_ends = cur_index
                            # print("ends at: " + t[clause_ends:])
                            clause = t[clause_starts:clause_ends].strip(',')
                            if len(clause.split()) <= 5:                        #too small to be meaningful
                                cur_index += len(word)+1
                                continue
                            clause_starts = clause_ends
                            # clause = clause.lstrip()
                            clauses += [clause]
                            # print("verb: " + verb)
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

                    if tags.index((word,pos)) == len(tags)-1:         #last clause in text
                        clause = t[clause_starts:].strip(',')
                        clauses += [clause]
                        if(cur_entity != ""):
                            print(cur_entity.upper() + ": " + clause)
                        elif (pronoun_in_clause):
                            print("pronoun: " + clause)
                        else:
                            print("indirect_context: " + clause)
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
# print("Total Count : ",TotalCount)

    return clauses

# main()

def test():
    s = "@ncpasan, Jayasuriya came as a bowler and played lower down in the batting order, during the first few years of his career"
    tags = pos_tag(s.split())
    propernouns = [word.strip(",'.()!?") for word,pos in tags if (pos == 'NNP' or pos == 'NN')]
    propernouns = ', '.join(propernouns)
    print(propernouns)

# test()