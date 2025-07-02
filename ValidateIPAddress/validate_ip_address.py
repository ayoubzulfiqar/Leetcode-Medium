class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4_segment(segment: str) -> bool:
            if not segment or (len(segment) > 1 and segment[0] == '0'):
                return False
            if not segment.isdigit():
                return False
            num = int(segment)
            return 0 <= num <= 255

        def is_valid_ipv6_segment(segment: str) -> bool:
            if not segment or not (1 <= len(segment) <= 4):
                return False
            valid_chars = "0123456789abcdefABCDEF"
            for char in segment:
                if char not in valid_chars:
                    return False
            return True

        if '.' in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                if not is_valid_ipv4_segment(part):
                    return "Neither"
            return "IPv4"
        elif ':' in queryIP:
            parts = queryIP.split(':')
            if len(parts) != 8:
                return "Neither"
            for part in parts:
                if not is_valid_ipv6_segment(part):
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"