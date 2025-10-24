class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1, n + 1))
        # listing all out players

        kSub = k - 1
        # considering we count the friend we start with offset it by -1
        i = 0

        while len(circle) > 1:
            i = (i + kSub) %  len(circle)
            # the modulus allows us to find the right location even  when we are at the  end
            # next time i will be next to the player we removed
            circle.pop(i)

        return circle[0]
        