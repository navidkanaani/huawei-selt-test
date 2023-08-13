import re


class Utils:
    @staticmethod
    def huawei_5300_retrieve_line_length(telnet_result):
        line_length_pattern = r"line length.*feet"
        line_length_meters_value_pattern = r"\d.+ m"
        if line_length := re.findall(line_length_pattern, telnet_result):
            line_length_meters = re.findall(line_length_meters_value_pattern, line_length[0])
            return line_length_meters[0]
        else:
            raise Exception("Test is failed, try again!")
    
    def huawei_5300_login_check(socket, telnet_result):
        login_success_pattern = r"Terminal users login"
        login_failed_pattern = r"Error User's Name or Password!"
        if re.findall(login_success_pattern, telnet_result):
            return True
        elif re.findall(login_failed_pattern, telnet_result):
            socket.close()
            raise Exception("Wronge username or password!")
        
    
    @staticmethod
    def huawei_5600_deactivate_confirmation(terminal_result: str) -> bool:
        deactivated_status = False
        already_deactivated_message_pattern = r"(Failure:).*(deactivated)"
        deactivate_successfull_message_pattern = r"(Deactivate).*(successfully)"
        if len(re.findall(already_deactivated_message_pattern, terminal_result)) or len(re.findall(deactivate_successfull_message_pattern, terminal_result)):
           deactivated_status = True 
        return deactivated_status
    
    @staticmethod
    def huawei_5600_retrieve_line_length(result: str):
        line_length_pattern = r"Line length.*\(\d*.feet\)"
        line_length_meters_pattern = r"\d.+ m"
        line_length = re.findall(line_length_pattern, result)
        line_length_meters = re.findall(line_length_meters_pattern, line_length[0])
        return line_length_meters[0]
