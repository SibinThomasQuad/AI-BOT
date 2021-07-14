import sqlite3
conn = sqlite3.connect('brain')
cursor = conn.cursor()
def main():
    print("[+] Bot>>Ok.")
    question=input("[+] You>>")
    #print("You>>"+question+"")
    thinking(question)
def thinking(q):
    cursor.execute("SELECT * FROM memory where question like '%"+q+"%'")
    rows = cursor.fetchall()
    if(rows):
        #line
        for row in rows:
            print ("[+] Bot>>"+row[2])
            #print(row[2])
        main()
    else:
        print("[+] Bot>>What is that ,i dont know")
        print("[+] Bot>>if you say that i will remember")
        ans=input("[+] You>>")
        learn(q,ans)
def learn(qt,ans):
    cursor.execute('insert into memory (question,answer) values (?,?)',(str(qt),str(ans)))
    conn.commit()
    print("[+] Bot>>Ok i will remember that")
    main()
main()
#learn('who is sibin thomas?','sibin thomas is developed me')
