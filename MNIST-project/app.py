import jetson.inference
import jetson.utils

# load model 
net = jetson.inference.imageNet(argv=['--model=simple_mnist_model.onnx'])
# net = jetson.inference.detectNet(argv=[‘--model=models/coin/ssd-mobilenet.onnx’, ‘--labels=models/coin/labels.txt’, ‘--input-blob=input_0’, ‘--output-cvg=scores’, ‘--output-bbox=boxes’], threshold=0.5)
camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file
font = jetson.utils.cudaFont()

while display.IsStreaming():
    img = camera.Capture()
    
    # classify the image
    class_idx, confidence = net.Classify(img)
    font.OverlayText(img, img.width, img.height, "{:05.2f}% {:s}".format(confidence * 100, class_desc), 5, 5, font.White, font.Gray40)
    display.Render(img)
    display.SetStatus("Classification | Network {:.0f} FPS".format(net.GetNetworkFPS()))

    # find the object description
    class_desc = net.GetClassDesc(class_idx)

    # print out the result
    print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))