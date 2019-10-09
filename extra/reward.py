X_MAX = -0.5

def normalize_dist(track_width, distance_from_center, is_left_of_center):
    if is_left_of_center:
        distance_from_center = -1 * distance_from_center
        
    return 2 * distance_from_center / track_width

def calc_b(x):
    return (x*x*x - x - 1) / (x*x - 1)

def dist_reward(x, b):
    return float((x+1) * (x-1) * (x-b))

def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']
    
    b = calc_b(X_MAX)
    x = normalize_dist(track_width, distance_from_center, is_left_of_center)
    if abs(x) > 1.2:
        return 0
    return dist_reward(x, b)

# https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html
# https://github.com/sasasavic82/deepracer-reward/blob/master/model/reward_v1.py