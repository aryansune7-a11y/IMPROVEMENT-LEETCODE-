class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0

        from datetime import datetime
        start = datetime.strptime(start, "%m-%d")
        end = datetime.strptime(end, "%m-%d")

        return (end - start).days + 1
