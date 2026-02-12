class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        used = 0

        while mainTank > 0:
            mainTank -= 1
            used += 1
            distance += 10

            if used == 5 and additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
                used = 0

        return distance

    # return 10*(mainTank+min((mainTank-1)//4, additionalTank))
