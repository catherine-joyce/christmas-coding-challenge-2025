class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        total_prefix = ""
        prefixes_list = []
        for item in words:
            total_prefix += item
            prefixes_list.append(total_prefix)
        for prefix in prefixes_list:
            if prefix == s:
                return True
        return False
