def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.5
        if 2 <= speed <= 3:
            reward += 0.2
        elif 1.5 <= speed < 2:
            reward += 0.1
            
    elif distance_from_center <= marker_2:
        reward = 0.8
        
    elif distance_from_center <= marker_3:
        reward = 0.2
        
        if 15<= abs(steering_angle) <= 25:
            if 0.5 <= speed <= 1:
                reward += 0.1
            reward += 0.1
            
    else:
        reward = 0.001
        
        if 20<= abs(steering_angle) <= 25:
            reward += 0.01  # likely crashed/ close to off track
    
    
    return float(reward)
