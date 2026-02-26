#This exercise showcases basic data analysis using pandas

import pandas as pd
 
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# Check to verify there are no duplicates in the database
df['dup'] = df.duplicated(subset=None,keep='first')
print(df['dup'].value_counts())

# Result:
# False    458
#Name: count, dtype: int64

#RESULT: No duplicates in the data

#------Filtering through data---------

# Adding a new row in the file:

add_row = pd.DataFrame([{"Name": "Mark Mason", "Team": "Utah Jazz", "Number": "14", "Position": "SF", "Age": "25", "Height": "NaN", "Weight": "NaN", "College": "NaN", "Salary": "300000", "dup" : "False"}], index=["458"])
df = pd.concat([df, add_row])

#Sorting by column: viewing all the names, ages and heights respectively

print(df[["Name", "Age", "Height"]].to_string())

#Indexing based on player name for easier handling of the data:

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv", index_col="Name")
print((df).to_string())

#Listing the first 20 players only

print(df.iloc[0:19])

#--- Data Analysis --------------------
 
#Looking at the data, I define the following questions:

# 1. Which college has most players in NBA and what are names of these players?

college_count = df.value_counts(["College"])
print(college_count)

'''
College
Kentucky            22
Duke                20
Kansas              18
North Carolina      16
UCLA                15
                    ..
Morehead State       1
Central Michigan     1
Weber State          1
Lehigh               1
Westchester CC       1
'''

kentucky_pl = df[df["College"] == "Kentucky"]
print(kentucky_pl)

# RESULT:
'''

                                          Team  Number Position   Age Height  Weight   College      Salary
Name
James Young                     Boston Celtics    13.0       SG  20.0    6-6   215.0  Kentucky   1749840.0
Nerlens Noel                Philadelphia 76ers     4.0       PF  22.0   6-11   228.0  Kentucky   3457800.0
Patrick Patterson              Toronto Raptors    54.0       PF  27.0    6-9   235.0  Kentucky   6268675.0
Julius Randle               Los Angeles Lakers    30.0       PF  21.0    6-9   250.0  Kentucky   3132240.0
Eric Bledsoe                      Phoenix Suns     2.0       PG  26.0    6-1   190.0  Kentucky  13500000.0
Devin Booker                      Phoenix Suns     1.0       SG  19.0    6-6   206.0  Kentucky   2127840.0
Archie Goodwin                    Phoenix Suns    20.0       SG  21.0    6-5   200.0  Kentucky   1160160.0
Brandon Knight                    Phoenix Suns     3.0       PG  24.0    6-3   189.0  Kentucky  13500000.0
Willie Cauley-Stein           Sacramento Kings     0.0        C  22.0    7-0   240.0  Kentucky   3398280.0
DeMarcus Cousins              Sacramento Kings    15.0        C  25.0   6-11   270.0  Kentucky  15851950.0
Rajon Rondo                   Sacramento Kings     9.0       PG  30.0    6-1   186.0  Kentucky   9500000.0
Jodie Meeks                    Detroit Pistons    20.0       SG  28.0    6-4   210.0  Kentucky   6270000.0
Terrence Jones                 Houston Rockets     6.0       PF  24.0    6-9   252.0  Kentucky   2489530.0
Anthony Davis             New Orleans Pelicans    23.0       PF  23.0   6-10   253.0  Kentucky   7070730.0
Aaron Harrison               Charlotte Hornets     9.0       SG  21.0    6-6   210.0  Kentucky    525093.0
Michael Kidd-Gilchrist       Charlotte Hornets    14.0       SF  22.0    6-7   232.0  Kentucky   6331404.0
John Wall                   Washington Wizards     2.0       PG  25.0    6-4   195.0  Kentucky  15851950.0
Tayshaun Prince         Minnesota Timberwolves    12.0       SF  36.0    6-9   212.0  Kentucky    947276.0
Karl-Anthony Towns      Minnesota Timberwolves    32.0        C  20.0    7-0   244.0  Kentucky   5703600.0
Enes Kanter              Oklahoma City Thunder    11.0        C  24.0   6-11   245.0  Kentucky  16407500.0
Nazr Mohammed            Oklahoma City Thunder    13.0        C  38.0   6-10   250.0  Kentucky    222888.0
Trey Lyles                           Utah Jazz    41.0       PF  20.0   6-10   234.0  Kentucky   2239800.0

'''

# 2. What is the average salary of all players?

print(df["Salary"].mean())

#RESULT: 4842684.105381166

#3. List top 10 players with the biggest salary

x = df.nlargest(10, "Salary",keep='first')
print(x)

#RESULT:

'''                                  Team  Number Position   Age Height  Weight       College      Salary
Name
Kobe Bryant         Los Angeles Lakers    24.0       SF  37.0    6-6   212.0           NaN  25000000.0
LeBron James       Cleveland Cavaliers    23.0       SF  31.0    6-8   250.0           NaN  22970500.0
Carmelo Anthony        New York Knicks     7.0       SF  32.0    6-8   240.0      Syracuse  22875000.0
Dwight Howard          Houston Rockets    12.0        C  30.0   6-11   265.0           NaN  22359364.0
Chris Bosh                  Miami Heat     1.0       PF  32.0   6-11   235.0  Georgia Tech  22192730.0
Chris Paul        Los Angeles Clippers     3.0       PG  31.0    6-0   175.0   Wake Forest  21468695.0
Kevin Durant     Oklahoma City Thunder    35.0       SF  27.0    6-9   240.0         Texas  20158622.0
Derrick Rose             Chicago Bulls     1.0       PG  27.0    6-3   190.0       Memphis  20093064.0
Dwyane Wade                 Miami Heat     3.0       SG  34.0    6-4   220.0     Marquette  20000000.0
Brook Lopez              Brooklyn Nets    11.0        C  28.0    7-0   275.0      Stanford  19689000.0
'''

# 4. Who is the oldest player in NBA?

print(df.nlargest(1,"Age", keep='first'))

#RESULT:

'''                         Team  Number Position   Age Height  Weight      College     Salary
Name
Tim Duncan  San Antonio Spurs    21.0        C  40.0   6-11   250.0  Wake Forest  5250000.0
'''

# 5. Find the 200th name in the list 

print(df.iloc[199])

#RESULT:

'''Name           Paul George
Team        Indiana Pacers
Number                13.0
Position                SF
Age                   26.0
Height                 6-9
Weight               220.0
College       Fresno State
Salary          17120106.0
Name: 199, dtype: object
'''
