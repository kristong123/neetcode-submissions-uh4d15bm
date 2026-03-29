class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lMax = l
        rMax = r
        water = 0

        while l < rMax or r > lMax:
            lMaxh = height[lMax]
            rMaxh = height[rMax]

            if lMaxh <= rMaxh:
                lh = height[l]
                print(lMaxh, lh)
                if lh < lMaxh:
                    print('added', lMaxh - lh, 'at', l)
                    water += lMaxh - lh
                else:
                    lMax = l
                l += 1
            else:
                rh = height[r]
                if rh < rMaxh:
                    print('added', rMaxh - rh, 'at', r)
                    water += rMaxh - rh
                else:
                    rMax = r
                r -= 1

        return water

            