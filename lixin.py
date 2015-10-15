import numpy as np

data = np.loadtxt(file("keywords.csv"), delimiter=",",dtype=str)
field = 13
fields = np.array([0,1,field])
title_abstract_domain = data[1:,fields]
keywords = dict()
keyword_to_title = dict()
domain_to_keyword = dict()
title_to_keyword = dict()
for i in range(0,len(title_abstract_domain)):
    row = title_abstract_domain[i]
    discipline = row[2]
    title = row[0]
    keys = [x.strip() for x in row[1].split(';')]
    title_to_keyword[title] = set(keys)
    if not discipline in domain_to_keyword:
        domain_to_keyword[discipline] = set()
    for k in keys:
        domain_to_keyword[discipline].add(k)
        if not k in keywords:
            keywords[k] = dict()
        keywords[k][discipline] = 1 + keywords[k].get(discipline,0) 
        if not k in keyword_to_title:
            keyword_to_title[k] = set()
        keyword_to_title[k].add(title)

np.savetxt('tad.csv',title_abstract_domain,delimiter=",",fmt="%s,%s,%s")

wf = file('arcs.csv','w')
for title in title_to_keyword:
    if title == "":
        continue
    col = title_to_keyword[title]
    for c in col:
        wf.write("%s,%s\n" % (title,c))
for discip in domain_to_keyword:
    if discip == "":
        continue
    col = domain_to_keyword[discip]
    for c in col:
        wf.write("%s,%s\n" % (discip,c))
wf.close()


# who uses the keyword
def uses_keyword(keyword):
    return keyword_to_title[keyword]

    
# dictionary
keyword_counts = { k: sum(keywords[k].values()) for k in keywords }
# tuples
keyword_counts_t = [(k, sum(keywords[k].values())) for k in keywords ]
# sort keyword counts
keyword_counts_t.sort(key=lambda x: x[1])

wf = file('counts.csv','w')
for t in keyword_counts_t:
    wf.write("%s,%s\n" % t)
wf.close()



    
wf = file('arcs.csv','w')
for title in title_to_keyword:
    if title == "":
        continue
    col = title_to_keyword[title]
    for c in col:
        wf.write("%s,%s\n" % (title,c))
for discip in domain_to_keyword:
    if discip == "":
        continue
    col = domain_to_keyword[discip]
    for c in col:
        wf.write("%s,%s\n" % (discip,c))
wf.close()
wf = file('discipline_keyword.csv','w')
for k in keywords:
    for discipline in keywords[k]:
        wf.write("%s,%s,%s\n" % (k,discipline,keywords[k][discipline]))
wf.close()
