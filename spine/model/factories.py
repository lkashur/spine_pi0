import torch

def model_dict():
    """Returns dictionary of model classes using name keys (strings).

    Returns
    -------
    dict
        Dictionary of available models
    """

    from . import full_chain
    from . import uresnet
    from . import uresnet_ppn
    from . import singlep
    from . import spice
    from . import graph_spice
    from . import grappa
    from . import bayes_uresnet
    from . import vertex

    # Make some models available (not all of them, e.g. PPN is not standalone)
    models = {
        # Full reconstruction chain, including an option for deghosting
        "full_chain": (full_chain.FullChain, full_chain.FullChainLoss),
        # UresNet
        "uresnet": (uresnet.UResNetSegmentation, uresnet.SegmentationLoss),
        # UResNet + PPN
        'uresnet_ppn': (uresnet_ppn.UResNetPPN, uresnet_ppn.UResNetPPNLoss),
        # Single Particle Classifier
        "singlep": (singlep.ParticleImageClassifier, singlep.ParticleTypeLoss),
        # Multi Particle Classifier
        "multip": (singlep.MultiParticleImageClassifier,
                singlep.MultiParticleTypeLoss),
        # SPICE
        "spice": (spice.SPICE, spice.SPICELoss),
        # Graph SPICE
        "graph_spice": (graph_spice.GraphSPICE, graph_spice.GraphSPICELoss),
        # Graph neural network Particle Aggregation (GrapPA)
        "grappa": (grappa.GrapPA, grappa.GrapPALoss),
        # Bayesian Classifier
        "bayes_singlep": (singlep.BayesianParticleClassifier,
                singlep.ParticleTypeLoss),
        # Bayesian UResNet
        "bayesian_uresnet": (bayes_uresnet.BayesianUResNet,
                bayes_uresnet.SegmentationLoss),
        # DUQ UResNet
        "duq_uresnet": (bayes_uresnet.DUQUResNet,
                bayes_uresnet.DUQSegmentationLoss),
        # Evidential Classifier
        'evidential_singlep': (singlep.EvidentialParticleClassifier,
                singlep.EvidentialLearningLoss),
        # Evidential Classifier with Dropout
        'evidential_dropout_singlep': (singlep.BayesianParticleClassifier,
                singlep.EvidentialLearningLoss),
        # Deep Single Pass Uncertainty Quantification
        'duq_singlep': (singlep.DUQParticleClassifier,
                singlep.MultiLabelCrossEntropy),
        # Vertex PPN
        'vertex_ppn': (vertex.VertexPPNChain, vertex.UResNetVertexLoss),
        # Vertex Pointnet
        'vertex_pointnet': (vertex.VertexPointNet, vertex.VertexPointNetLoss),
    }
    return models


def model_factory(name):
    """
    Returns an instance of a model class based on its name key (string).

    Parameters
    ----------
    name: str
        Key for the model. See source code for list of available models.

    Returns
    -------
    object
    """
    models = model_dict()
    if name not in models:
        raise ValueError("Unknown model name provided: %s" % name)

    return models[name]
