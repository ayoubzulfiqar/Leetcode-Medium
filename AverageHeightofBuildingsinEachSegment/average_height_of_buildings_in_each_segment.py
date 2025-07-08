def average_height_in_segments(heights, segment_size):
    """
    Calculates the average height of buildings in each segment.

    Segments are defined as contiguous blocks of buildings of a specified size.
    If the last segment is incomplete, its average is still calculated.

    Args:
        heights (list of int or float): A list of building heights.
        segment_size (int): The number of buildings in each segment.
                            Must be a positive integer.

    Returns:
        list of float: A list of average heights for each segment.
                       Returns an empty list if heights is empty or segment_size is invalid.
    """
    if not heights:
        return []
    if not isinstance(segment_size, int) or segment_size <= 0:
        return []

    averages = []
    num_buildings = len(heights)
    
    for i in range(0, num_buildings, segment_size):
        segment = heights[i : i + segment_size]
        if segment: 
            segment_sum = sum(segment)
            segment_count = len(segment)
            averages.append(segment_sum / segment_count)
            
    return averages

if __name__ == "__main__":
    # Test Case 1: Standard case
    heights1 = [10, 20, 30, 40, 50, 60]
    segment_size1 = 2
    result1 = average_height_in_segments(heights1, segment_size1)
    print(f"Heights: {heights1}, Segment Size: {segment_size1} -> Averages: {result1}")

    # Test Case 2: Incomplete last segment
    heights2 = [10, 20, 30, 40, 50]
    segment_size2 = 3
    result2 = average_height_in_segments(heights2, segment_size2)
    print(f"Heights: {heights2}, Segment Size: {segment_size2} -> Averages: {result2}")

    # Test Case 3: Empty heights list
    heights3 = []
    segment_size3 = 5
    result3 = average_height_in_segments(heights3, segment_size3)
    print(f"Heights: {heights3}, Segment Size: {segment_size3} -> Averages: {result3}")

    # Test Case 4: segment_size = 1
    heights4 = [100, 200, 300]
    segment_size4 = 1
    result4 = average_height_in_segments(heights4, segment_size4)
    print(f"Heights: {heights4}, Segment Size: {segment_size4} -> Averages: {result4}")

    # Test Case 5: segment_size > len(heights)
    heights5 = [5, 10, 15]
    segment_size5 = 10
    result5 = average_height_in_segments(heights5, segment_size5)
    print(f"Heights: {heights5}, Segment Size: {segment_size5} -> Averages: {result5}")

    # Test Case 6: Invalid segment_size (0)
    heights6 = [1, 2, 3]
    segment_size6 = 0
    result6 = average_height_in_segments(heights6, segment_size6)
    print(f"Heights: {heights6}, Segment Size: {segment_size6} -> Averages: {result6}")

    # Test Case 7: Invalid segment_size (negative)
    heights7 = [1, 2, 3]
    segment_size7 = -2
    result7 = average_height_in_segments(heights7, segment_size7)
    print(f"Heights: {heights7}, Segment Size: {segment_size7} -> Averages: {result7}")

    # Test Case 8: Heights with floats
    heights8 = [10.5, 20.0, 30.5, 40.0]
    segment_size8 = 2
    result8 = average_height_in_segments(heights8, segment_size8)
    print(f"Heights: {heights8}, Segment Size: {segment_size8} -> Averages: {result8}")