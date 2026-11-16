# Conflict-aware Diversified Collaborative Learning for Semi-Supervised Histopathology Image Segmentation
<img width="2563" height="1560" alt="frame_diagram" src="https://github.com/user-attachments/assets/20cb18de-5386-4ce9-b1cf-c789e1642e46" />

## Overview

We present **Conflict-aware Diversified Collaborative Learning (CDCL)**, a novel semi-supervised framework for histopathology image segmentation. Traditional co-training methods often suffer from two intrinsic pathologies: **model coupling** (where sub-networks lose diversity) and **confirmation bias** (where erroneous pseudo-labels are reinforced).

## Datasets

**Download the datasets**:
- GlaS dataset: [Download GlaS dataset](https://datasets.activeloop.ai/docs/ml/datasets/glas-dataset/)
- CRAG dataset: [Download CRAG dataset](https://opendatalab.com/OpenDataLab/CRAG/tree/main)

## Training FDCL

1. **Install dependencies**:

Install the required Python libraries by running the following command:
```text
pip install -r requirements.txt
```

2. **Train the model**:

Once the dataset is organized and the dependencies are installed, you can start training by running:
```text
python main.py
```

## Citation
```text
@article{li2026cdcl,
  title={Conflict-aware Diversified Collaborative Learning for Semi-Supervised Histopathology Image Segmentation},
  author={Li, Yanan and Shi, Cao},
  journal={International Journal of Imaging Systems and Technology},
  year={2026}
}
```
   
      
