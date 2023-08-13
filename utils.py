import re


class Utils:
    @staticmethod
    def retrieve_line_length(telnet_log):
        line_length_pattern = r"line length.*feet"
        line_length_meters_value_pattern = r"\d.+ m"
        line_length = re.findall(line_length_pattern, telnet_log)
        line_length_meters = re.findall(line_length_meters_value_pattern, line_length[0])
        return line_length_meters[0]
    
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
