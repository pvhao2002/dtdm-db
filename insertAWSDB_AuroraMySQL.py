import insertUtil as ut
import MySQLdb


# Tạo kết nối với RDS Aurora MySQL và thêm dữ liệu vào
conn = MySQLdb.connect(host='database-aurora.cluster-cujlork3fltg.us-east-1.rds.amazonaws.com',
                       user='admin', passwd='12345678', db='covid_19', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')
