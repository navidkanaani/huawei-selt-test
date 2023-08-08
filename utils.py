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
    def huawei_5600_deactivate_confirm(terminal_result: str) -> bool:
        deactivated_status = False
        already_deactivated_message_pattern = r"(Failure:).*(deactivated)"
        deactivate_successfull_message_pattern = r"(Deactivate).*(successfully)"
        breakpoint()
        if re.match(already_deactivated_message_pattern, terminal_result) or re.match(deactivate_successfull_message_pattern, terminal_result):
           deactivated_status = True 
        return deactivated_status 

result = """esf-esf-ghandi1(config-if-adsl-0/3)#deactivate 1
  Failure: Port 1 has been deactivated"""
    
    
# match_test_result = Utils.huawei_5600_deactivate_confirm(result)
# print(match_test_result)