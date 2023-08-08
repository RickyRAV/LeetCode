class TimeMap:

    def __init__(self):
        #use faultdict to automatically create lists for new keys.
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #append the new timestamp and value to the key's list
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #get the list of (timestamp, value) pairs for the given key.
        pairs = self.data.get(key, None)
        
        #if theres no data for the key, return empty string
        if not pairs:
            return ""
        
        #use binary search to find the index where the timestamp would be inserted
        idx = bisect.bisect(pairs, (timestamp, chr(127))) #127 is the highest ASCII value
        
        #if idx is 0, it means all timestamps we have are larger than the given timestamp
        if idx == 0:
            return ""
        
        #otherwise, return the value at idx - 1, which is the largest timestamp less than or equal to the given timestamp.
        return pairs[idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)