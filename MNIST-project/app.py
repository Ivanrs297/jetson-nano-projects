import jetson.inference
import jetson.utils

# load model 
net = jetson.inference.imageNet(model = "simple_mnist_model.onnx")
camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
    img = camera.Capture()
    
    # classify the image
    class_idx, confidence = net.Classify(img)
    display.Render(img)
    display.SetStatus("Classification | Network {:.0f} FPS".format(net.GetNetworkFPS()))

    # find the object description
    class_desc = net.GetClassDesc(class_idx)

    # print out the result
    print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))