import logging
logging.basicConfig(filename="..//Logger//capestome.log",level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
from SearchFileinDrives.Searchfile import SearchFilesDrives
from SearchinDB.SearchFilePath import SearchFile
from SearchinDB.InsertData import InsertFileinDB
from CasptoneExceptions.MysqlException import MYSqlErrror
import mysql.connector
import time
import openpyxl as xl
def userdata():
    dir=input("Enter the drive like c://d://\n")
    filename=input("Enter the filename with extension like demo.txt\n")
    logging.info(f"Drive name {dir} file name {filename}")
    dbobj=SearchFile()
    logging.info(f'class used {SearchFile.__name__}')
    dbobj=SearchFile()
    wb=xl.load_workbook("C://testdata//testfiles.xlsx")
    ws=wb.active

    try:
        dbobj.Connect("localhost",'root',"Neelima@2001",'myhcl',3306)
        logging.info('myhcl database is connected')
        result=dbobj.SearchFile(filename)

    except mysql.connector.Error as err:
        logging.exception(err, exc_info=True)
        raise MYSqlErrror(f'{err.msg}',err.errno)

    finally:
        dbobj.connect.close()


    if len(result)==0:
        print("Not found in Database")
        print("Now Searching in Drives...")
        logging.info("Not found in Database")
        logging.info("Now searching in Drives")
        start_time=time.time()
        obj=SearchFilesDrives()
        logging.info(f'for searching in drive {SearchFilesDrives.__name__} is used')
        files=obj.searchfiles(dir,filename)
        ws.cell(row=1,column=1).value=str(files)
        wb.save("C://testdata//testfiles.xlsx")
        wb.close()
        inserobj=InsertFileinDB()
        inserobj.insert(files)
        logging.info(f'files found {files}')
        print(files)
        obj.start()
        end_time=time.time()
        logging.info(f'time taken{end_time-start_time}')
        logging.info("Ending")
        print(end_time-start_time)
    else:
        print("Found in database")
        print(result)
userdata()