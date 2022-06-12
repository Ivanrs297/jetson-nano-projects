# MNIST Detection

**Requirements**
- *ONNX* Trained Model (MNIST)

**Instructions**

1. Clone *Jetson-inference* 
   ```
   $ cd ~/
   $ git clone https://github.com/dusty-nv/jetson-inference
   ```
2. Clone this repo 
   ```
   $ cd ~/
   $ git clone ...
   ```
3. Go to `jetson-inference/`
   ```
   $ cd ~/
   $ cd jetson-inference/
   ```
4. Mount Docker container with 
   ```
   $ docker/run.sh --volume ~/jetson-nano-projects/MNIST-project:/MNIST-project
   ```
5. Run 
   ```
   python3 /MNIST-project/app.py
   ```