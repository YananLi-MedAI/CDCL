import sys
import torch.nn as nn

# Import network architectures from submodules securely
from .networks_2d.xnet import XNet_sb
from .networks_2d.unet import unet, r2_unet, attention_unet, r2_attention_unet
from .networks_2d.unet_plusplus import unet_plusplus
from .networks_2d.resunet import res_unet
from .networks_2d.resunet_plusplus import res_unet_plusplus
from .networks_2d.swinunet import swinunet


def get_network(network, in_channels, num_classes, **kwargs):
    """
    Factory function to instantiate and return the requested 2D neural network architecture.

    Args:
        network (str): Name of the network architecture.
        in_channels (int): Number of input channels (e.g., 1 for grayscale, 3 for RGB).
        num_classes (int): Number of output segmentation classes.
        **kwargs: Additional keyword arguments.

    Returns:
        nn.Module: The initialized neural network model.
    """
    net = None

    if network == 'xnet_sb':
        net = XNet_sb(in_channels, num_classes)
    elif network == 'unet':
        net = unet(in_channels, num_classes)
    elif network == 'unet_plusplus' or network == 'unet++':
        net = unet_plusplus(in_channels, num_classes)
    elif network == 'resunet':
        net = res_unet(in_channels, num_classes)
    elif network == 'resunet++':
        net = res_unet_plusplus(in_channels, num_classes)
    elif network == 'swinunet':
        # Swin-Unet typically expects image size configuration, defaulting to 224 here
        net = swinunet(num_classes, img_size=kwargs.get('img_size', 224))
    else:
        raise ValueError(f"Error: Network architecture '{network}' is not supported or spelled incorrectly.")

    return net