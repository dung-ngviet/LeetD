import re
# class Solution:
#     def validIPAddress(self, IP: str) -> str:
#         if ":" in IP:
#             parts = IP.split(":")
#             if len(parts) != 8: return "Neither"
#             for part in parts:
#                 if not re.fullmatch("[0-9a-fA-F]{1,4}", part): return "Neither"
#             return "IPv6"
#         elif "." in IP:
#             parts = IP.split(".")
#             if len(parts) != 4: return "Neither"
#             for part in parts:
#                 if part != "0" and part.startswith("0"): return "Neither"
#                 if not re.fullmatch("[0-9]+", part): return "Neither"
#                 if int(part) > 255: return "Neither"
#             return "IPv4"
#         else: return "Neither"

class Solution:
    def isIPv4(self, s):
        try: return str(int(s)) == s and 0 <= int(s) <= 255
        except: return False

    def isIPv6(self, s):
        try: return 1 <= len(s) <= 4 and int(s, 16) >= 0
        except: return False

    def validIPAddress(self, IP: str) -> str:
        if IP.count(":") == 7 and all(self.isIPv6(i) for i in IP.split(":")):
            return "IPv6"
        if IP.count(".") == 3 and all(self.isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        return "Neither"

print(Solution().validIPAddress(IP = "172.16.254.1")) # 4
print(Solution().validIPAddress(IP = "2001:0db8:85a3:0:0:8A2E:0370:7334")) # 6
print(Solution().validIPAddress(IP = "256.256.256.256")) # Neither
print(Solution().validIPAddress(IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:")) # Neither
print(Solution().validIPAddress(IP = "1e1.4.5.6")) # Neither