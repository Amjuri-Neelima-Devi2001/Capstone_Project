from SearchinDB.DBConnection import DatabaseConnection
class InsertFileinDB(DatabaseConnection):
    def __init__(self):
        self.conn =self.Connect('localhost','root','Neelima@2001','myhcl',3306)
    def insert(self,files):
        self.files=files
        self.insertcur = self.connect.cursor()
        for f in self.files:
            sql="insert into fileinfo(filename) values(%s);"
            self.insertcur.execute(sql,(f,))
            self.connect.commit()
        print("Files added successfully")
