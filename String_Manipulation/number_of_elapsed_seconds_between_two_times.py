    def get_secs(self, time):
        hours, minutes, seconds = [int(res) for res in time.split(":")]
        return hours * 3600 + minutes * 60 + seconds
    
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        time1 = self.get_secs(startTime)
        time2 = self.get_secs(endTime)

        return time2 - time1