
import sys

import torch

import matplotlib

print("Hallo vanaf een Snellius Compute Node!")

print(f"Python versie: {sys.version}")

print(f"PyTorch beschikbaar: {torch.__version__}")

print(f"CUDA beschikbaar op deze node: {torch.cuda.is_available()}")

