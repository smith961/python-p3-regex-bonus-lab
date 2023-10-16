import re

class my_regex:
    @staticmethod
    def fullmatch(string):
        pattern = r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
        return re.fullmatch(pattern, string)

    @staticmethod
    def findall(string):
        pattern = r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
        return re.findall(pattern, string)