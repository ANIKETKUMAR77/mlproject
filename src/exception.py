import sys 

der error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  # it will give the exception details like file name,line number etc 
    file_name =  exc_tb.tb_frame.f_code.co_filename # it will give the file name where exception has occurred       
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format()(
      file_name,exc_tb.tb_lineno,str(error) # it will give the line number where exception has occurred
      )
   
    return error_message


# custom exception class

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # this will call the constructor of the parent class Exception
        self.error_message=error_message_detail(error_message,error_detail=error_detail) # this will give the detailed error message
     
    def __str__(self):
        return self.error_message
    
