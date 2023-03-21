class MYSqlErrror(Exception):
    def __init__(self,message,err_no):
        super().__init__(message)
        self.err_number=err_no
