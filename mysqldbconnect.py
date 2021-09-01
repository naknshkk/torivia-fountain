import MySQLdb

#---------
# 接続
#---------
cnct = MySQLdb.connect(
    host = "localhost",
    user = "root",
    password = "root",
    db = "triviadata",
    charset = "utf8"
    )
TABLE = "tribia"

cur = cnct.cursor()

#データの取得・表示
cur.execute("SELECT tribia, hee_amount FROM " + TABLE + " ORDER BY rand() limit 1" + ";")
results = cur.fetchall()
print("全て表示")
print(results)
print("\n")

print("1行ずつ表示")
for r in results:
    print(r)

cur.close()
cnct.close()