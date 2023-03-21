from SearchinDB.DBConnection import DatabaseConnection


class SearchFile(DatabaseConnection):
    def SearchFile(self,filename):
        print("searching in database")
        self.filename=filename
        sql="""Select *from fileinfo where filename like '%{0}'""".format(filename)
        self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
