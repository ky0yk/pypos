import psycopg2

connector =  psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'.format( 
                user="postgres",        #ユーザ
                password="postgresql",  #パスワード
                host="localhost",       #ホスト名
                port="5432",            #ポート
                dbname="postgres"))    #データベース名

cursor = connector.cursor()
    
# cursor.execute("SELECT version();")
# result = cursor.fetchone() 
    
# print(result[0]+"に接続しています。")


cursor.execute('SELECT * FROM books')   
rows = cursor.fetchall()

for row in rows:
    print(row)