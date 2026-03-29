class TimeMap:
    def __init__(self):
        # Store key -> list of (timestamp, value) tuples
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Pushes are strictly increasing, so list stays sorted by timestamp
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return empty string
        if key not in self.m:
            return ""

        vals = self.m[key]
        l, r = 0, len(vals) - 1
        res = ""

        while l <= r:
            mid = l + (r - l) // 2
            
            # If the current mid timestamp is less than or equal to target
            if vals[mid][0] <= timestamp:
                res = vals[mid][1] # This is a potential candidate
                l = mid + 1        # Try to find an even larger timestamp <= target
            else:
                r = mid - 1        # Too large, search the left side
                
        return res