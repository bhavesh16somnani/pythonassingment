import pandas as pd
squad={'Batsmen':{'Rohit Sharma':{'Matches':'206','runs':'8010','average':'47.4','highest_score':'264'},'Shikar dhawan':{'Matches':'128','runs':'5355','average':'44.62','highest_score':'143'},'Virat Kohli':{'Matches':'227','runs':'10843','average':'59.58','highest_score':'183'}}}
df=pd.DataFrame(squad['Batsmen'])
print(df)
c=[]
for i in squad.keys():
    for j in squad[i].keys():
        c.append(squad[i][j]['highest_score'])
print(max(c))

