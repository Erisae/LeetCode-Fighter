class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def allDigits(seq): #
            if not seq:
                return False
            for s in seq:
                if not s.isdigit():
                    return False
            return True

        def validHex(seq):
            for s in seq:
                if not s.isdigit() and not re.match(r'[a-fA-F]', s): # should be a to z
                    return False
            return True

        def validIPv4(q):
            xs = q.split(".")
            if len(xs) != 4:
                return False
            for x in xs:
                # check non digit
                if not allDigits(x):
                    return False
                # check leading Zero and value range
                val = int(x)
                if x[0] == '0' and len(x) > 1:
                    return False
                elif not 0 <= val <= 255:
                    return False
            return True

        def validIPv6(q):
            xs = q.split(":")
            if len(xs) != 8:
                return False
            for x in xs:
                if not (1 <= len(x) <= 4):
                    return False
                if not validHex(x):
                    return False
            return True

        if validIPv4(queryIP):
            return "IPv4"
        elif validIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
