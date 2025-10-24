class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        win = 0

        #let's assume to add one person in the game at the time. At first there is only one, for that the winner is that player so no need to start from just one player but what if our friends start from 2 and keep going, we can track who the winner is from the begining
        
        for i in range(2, n + 1):
            win = (win + k) % i
        
        return win + 1