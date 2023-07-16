def rotate_array(arr, rotation_count):
    # Check if rotation count is valid
    if rotation_count <= 0:
        return arr
    
    # Calculate the effective rotation count
    rotation_count = rotation_count % len(arr)
    
    # Rotate the array
    rotated_arr = arr[-rotation_count:] + arr[:-rotation_count]
    
    return rotated_arr
