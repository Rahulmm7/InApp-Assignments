import sqlite3

def connection():
    conn = sqlite3.connect('database.sqlite')
    return conn

def question1b():
    con = connection()
    cursor = con.cursor()
    print("\nHome Team \t\t\tAway Team")
    cursor.execute("Select HomeTeam,AwayTeam From Matches Where Season=2015 and FTHG=5")
    result = cursor.fetchall()
    for row in result:
        print(f'{row[0]}\t\t\t{row[1]}\n')

def question1c():
    con=connection()
    cursor=con.cursor()
    cursor.execute("Select * From Matches Where HomeTeam='Arsenal' and FTR='A' ")
    result=cursor.fetchall()
    print("\nMatch ID\tDiv\t \tSeason\tDate\t\tHome Team\tAway Team\tFTHG\tFTAG\tFTR \n--------\t----\t-------\t---------\t"
          "---------\t---------\t----\t----\t----")
    for row in result:
        print(f'{row[0]}\t\t{row[1]} \t{row[2]}\t{row[3]}\t{row[4]}\t\t{row[5]}\t\t{row[6]}\t{row[7]}\t{row[8]}\n')

def question1d():
    con = connection()
    cursor = con.cursor()
    cursor.execute(
        "Select * From Matches Where (Season>=2012 and Season < 2015) and AwayTeam='Bayern Munich' and FTHG>2")
    result = cursor.fetchall()
    print("\nMatch ID\tDiv \tSeason\tDate\t\tHome Team\tAway Team\tFTHG\tFTAG\tFTR")
    for row in result:
        print(f'{row[0]}\t\t{row[1]} \t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}\n')

def question1e():
    con = connection()
    cursor = con.cursor()
    cursor.execute("Select * FROM Matches where hometeam like 'A%' AND AwayTeam like 'm%'")
    result = cursor.fetchall()
    print(
        "\n\Match ID\tDiv\t \tSeason\tDate\t\tHome Team\tAway Team\tFTHG\tFTAG\tFTR \n--------\t----\t-------\t-------\t"
        "---------\t---------\t----\t----\t----")
    for row in result:
        print(f"\t{row[0]}\t  \t{row[1]} \t{row[2]}\t{row[3]}\t{row[4]}\t\t{row[5]}\t\t{row[6]}\t{row[7]}\t{row[8]}\n")


question1b()
question1c()
question1d()
question1e()
