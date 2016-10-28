
# coding: utf-8

# In[96]:

import io
import sys
default_stdout = sys.stdout
default_stderr = sys.stderr
reload(sys)
sys.stdout = default_stdout
sys.stderr = default_stderr
sys.setdefaultencoding('utf-8')
import csv
import mysql.connector
from mysql.connector import MySQLConnection, Error
def query():
    """
    1027ETL改正版，原先的query太多筆，所以現在將要查詢的table整個寫成一個list
    
    """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='1025try',
                                       user='root',
                                       password='apple')
        cursor = conn.cursor()
        # 將要查詢的table以及所屬道路寫成list，方便印出也可以用在query上。
        Tablename=['EVQEUU60,民權','EVQKWL60,民權','EVQKWL61,民權','WVQEUU60,民權','WVQKWL60,民權','WVQKWL61,民權'                    ,'NVTXQL00,堤頂','NVT5QV00,堤頂','NVSPRA40,堤頂','NVRPSV70,堤頂','NVPMSV40,堤頂','NVRPSV00,堤頂'                    ,'SVTXQL00,堤頂','SVT5QV00,堤頂','SVSPRA40,堤頂','SVPMSV40,堤頂','SVRPSV00,堤頂'                ,'NVQRTE00,舊宗','SVQRTE00,舊宗']
        # 開一個csv檔寫入
        with io.open('1028堤頂舊宗民權.csv','w',encoding='utf-8')as RDBque:
            # 寫欄位名稱
            RDBque.write("VD編號,道路,位置,道路數,方向,日期,時間,當量,平均速度,平均佔有率,平均車間距,星期"+u'\n')
            i=0
            for ele in Tablename:
                table=[]
                table.append(ele.split(',')[0])
                # 這裡query的寫法參照format的特殊用法，https://pyformat.info/
                select_join=("""select {r[0]}.location,{r[0]}.lanenumber,{r[0]}.direct,{r[0]}.YMD,{r[0]}.hour,
                {r[0]}.15Total  ,{r[0]}.avgspeed ,{r[0]}.avgpercent , {r[0]}.avgCarSpace ,rain.WD from {r[0]} 
                join rain on {r[0]}.YMD=rain.YMD;""".format(r=table))
                cursor.execute(select_join)
                # Using the cursor as iterator
                i+=1
                # 不喜歡用fetchone，fetchmany，fetchall直接取cursor
                for rows in cursor:
                    RDBque.write(VDname[i-1]+u',')
                    for element in range(len(rows)):
                        #  如果element是最後一個元素，就寫入換行
                        if element == len(rows)-1:
                            RDBque.write(format(rows[element]).decode('utf-8')+u'\n')
                        else:
                            RDBque.write(format(rows[element]).decode('utf-8')+u',')
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# In[97]:

query()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



