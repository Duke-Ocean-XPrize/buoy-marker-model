import zmq
#import control.movement

yolo_filter = "1"
fiducial_filter = "2"
yolo_port = 5555
fiducial_port = 5556
 
#  Socket to talk to server
context = zmq.Context()

# yolo globals
viewport_x_size = 640
viewport_y_size = 480

x_center_threshold = viewport_x_size/2
y_center_threshold = viewport_y_size/2
drop_thresh = 30

socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:{}".format(yolo_port))
socket.connect("tcp://localhost:{}".format(fiducial_port))
socket.setsockopt_string(zmq.SUBSCRIBE, yolo_filter)
socket.setsockopt_string(zmq.SUBSCRIBE, fiducial_filter)

incoming_data = []
k_window = 30
input_min = 1
input_max = 30
output_min = 100
output_max = 1000

def average_errors(incoming_data):
     """
     TODO: get the error for x y z coords
     average error over k_window
     return results
     """
def remove_null(data):
    output = [x for x in data if x !='null']
    return output

def get_range(value, inputMin, inputMax, outputMin, outputMax):
    intputSpan = inputMax - inputMin
    outputSpan = outputMax - outputMin
    valueScaled = float(value - inputMin) / float(intputSpan)
    return outputMin + (valueScaled * outputSpan)

def get_window(data, n):
    tranformed_data = get_range(data, 1, 30, 100, 1000)
    input_arr.append(tranformed_data)
    if len(input_arr) > n:
        del input_arr[0]
    return input_arr

def weighted_sum(data):
    window = get_window(data, 4)
    sorted_window = sorted(window, reverse = True)
    return sorted_window


def connect_vision():
     vision_data = socket.recv_string()
     vision_id, midpointX, midpointY, raw_distance = vision_data.split(",")
     midpointX = float(midpointX)
     midpointY = float(midpointY)
     raw_distance = float(raw_distance)

     incoming_data.append([midpointX, midpointY, raw_distance])
     #print("{},{},{},{}".format(vision_id,midpointX, midpointY, raw_distance))
     #print(incoming_data)
     new_generator = get_window(incoming_data)
     for each in new_generator:
          print(each)
     #print(get_window(incoming_data))

     x_dist = abs(midpointX - viewport_x_size)
     y_dist = abs(midpointY - viewport_y_size)

     """
     if midpointX > x_center_threshold:
          print("move RIGHT")
     else:
          print("move LEFT")

     if midpointY < x_center_threshold:
          print("move DOWN")
     else:
          print("move UP")

     if x_dist > drop_thresh and y_dist < drop_thresh:
          print("I'M LANDING")
     
     
     return raw_distance
     """
     

if __name__ == "__main__":
     while True:
          connect_vision()