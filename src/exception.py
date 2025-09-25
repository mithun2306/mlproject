# import sys
# import logging

# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name [{0}] line number [{1}] error msg [{2}]".format(
#         file_name,exc_tb.tb_lineno,str(error)    
#     )

#     return error_message


# class CustomException(Exception):
#     def __init__(self,error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)

#     def __str__(self):
#         return self.error_message

# if __name__=="__main__":
#     try:
#         0/1
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e,sys)
    


import sys
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error msg [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     try:
#         1 / 0  # Intentional error
#     except Exception as e:
#         logging.info("Divide by zero error")
#         ce = CustomException(e, sys)
#         print(ce)
