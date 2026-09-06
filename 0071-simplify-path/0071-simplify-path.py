class Solution:
    def simplifyPath(self, path: str) -> str:
        final = []
        path = path.split('/')
        for i in path:
            if i == '' or i == ' ' or i == '.':
                continue
            # elif i.isalpha() or :
            #     final.append(i)
            elif i == "..":
                if len(final) != 0:
                    final.pop()
                else:
                    continue
            else:
                final.append(i)
            print(final)
        url = "/" + "/".join(final)
        return url


        