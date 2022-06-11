# MNIST Detection

**Requirements**
- *ONNX* Trained Model (MNIST)

**Instructions**

1. Clone *Jetson-inference* `git clone https://github.com/dusty-nv/jetson-inference`
2. Create a folder  `~/project` and paste de `.onnx` model file
3. Go to `jetson-inference/`
4. Mount Docker container with `docker/run.sh --volume ~/project:/project` 