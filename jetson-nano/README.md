# MNIST Detection

**Requirements**
- *ONNX* Trained Model (MNIST)

**Instructions**

1. Clone *Jetson-inference* `git clone https://github.com/dusty-nv/jetson-inference`
2. Create a folder  `~/project` and paste the `.onnx` model file
3. Go to `jetson-inference/`
4. Mount Docker container with `docker/run.sh --volume ~/project:/project` 
5. Run `python3 /project/app.py`