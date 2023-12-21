
# 11. Container With Most Water

def maxArea(height):

    if len(height) <= 1:
        return 0

    left = 0
    right = 1
    max_area = 0
    min_height = float('inf')

    while right < len(height)-1:

        base = right - left
        if height[right] < min_height:
            min_height = height[right]

        area = base * min_height
        if area > max_area:
            max_area = area

        right += 1

    while left < len(height)-1:
        base = right - left
        if height[right] < min_height:
            min_height = height[right]

        area = base * min_height
        if area > max_area:
            max_area = area

        left += 1

    return max_area

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]

    print(maxArea(height))