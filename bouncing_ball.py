def bouncing_ball(h, bounce, window):
    total_passes = 1
    current_height = h
    if h > 0 and 0 < bounce < 1 and window < h:
        while True:
            updated_height = current_height * bounce
            if updated_height <= window:
                break
            else:
                current_height = updated_height
                total_passes += 2
    else:
        total_passes = -1
    return total_passes

print(bouncing_ball(2, 0.5, 1))
# h = 3, bounce = 0.66, window = 1.5, result is 3

