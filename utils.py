import re


class Utils:
    def retrieve_line_length(telnet_log):
        line_length_pattern = r"line length.*feet"
        line_length_meters_value_pattern = r"\d.+ m"
        line_length = re.findall(line_length_pattern, telnet_log)
        line_length_meters = re.findall(line_length_meters_value_pattern, line_length[0])
        return line_length_meters[0]
    