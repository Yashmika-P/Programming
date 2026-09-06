class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("L")==moves.count("R") and moves.count("U")==moves.count("D"):
            return True
        return False
        

# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         vcount = 0
#         hcount = 0
#         for move in moves:
#             if move == 'L':
#                 hcount += 1
#             elif move == 'U':
#                 vcount +=1
#             elif move == 'R':
#                 hcount -= 1 
#             else:
#                 vcount -= 1
#         return hcount == 0 and vcount == 0        