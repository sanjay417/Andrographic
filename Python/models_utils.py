import itertools
from data_utils.data_loaders import *
from models.AnnModels import *
from models.CnnModels import *
from models.RnnModels import *
from models.TransferLearnModels import *
from models.model_trainers_testers import *


def get_deep_rnn_expr_list(print_grid=True, simple_list=True):
    """
    sample template:
            {
            'experiment_name': 'rnn_experiment_1',
            'model_name': 'RNNMalware_Model1',
            'batch_size': 512,
            'embedding_dim': 256,
            'hidden_dim': 128,
            'epochs': 50,
            'lr': 0.0001,
            'num_layers': 1,
            'bidirectional': False,
            'dropout': 0,
            'LG': False
        }
    supported models so far :
    (1) RNNMalware_Model1 :
    (2) LSTMMalware_Model1 :
    (3) GRUMalware_Model1 :
    (4) StackedMalware_Model1 : Stack of LSTM and GRU layers.
            if LG=True => LSTM at bottom and GRU on top, e.g.
                    +---------+
                    |  GRUs   |
                    ----------|
                    |  LSTMs  |
                    +---------+
            else:
                    +---------+
                    |  LSTMs  |
                    ----------|
                    |  GRUs   |
                    +---------+
    ###########################################################
    Grid Template for RNNMalware_Model1, LSTMMalware_Model1, GRUMalware_Model1
        {    'model_name': ['LSTMMalware_Model1', 'GRUMalware_Model1', 'RNNMalware_Model1'],
            'batch_size': [128],
            'embedding_dim': [256],
            'hidden_dim': [256],
            'epochs': [2],
            'lr': [0.001],
            'num_layers': [1, 3],
            'bidirectional': [True, False],
            'dropout': [0.3],
            'opcode_len': [10]
        }
    ###########################################################
    Simple Template for StackedMalware_Model1
        {
            'model_name': 'StackedMalware_Model1',
            'experiment_name': 'rnn_experiment_1',
            'batch_size': 128,
            'embedding_dim': 8,
            'hidden_dim': 8,
            'epochs': 2,
            'lr': 0.001,
            'num_layers': 3,
            'bidirectional': True,
            'dropout': 0.3,
            'LG': True,
            'opcode_len': 500
        }
    ###########################################################
    """

    get_deep_rnn_expr_grid = {
        'model_name': ['StackedMalware_Model1'],
        'batch_size': [128],
        'embedding_dim': [256, 1024],
        'hidden_dim': [256, 1024],
        'epochs': [20],
        'lr': [0.001],
        'num_layers': [1, 3],
        'bidirectional': [True, False],
        'dropout': [0.3],
        'opcode_len': [500],
        'LG': [False]
    }

    simple_list = False
    if not simple_list and print_grid:
        print_line()
        print(f'Experiments Grid')
        print(get_deep_rnn_expr_grid)
        print_line()

    if simple_list:
        get_deep_rnn_expr_list = [
            {
                'model_name': 'StackedMalware_Model1',
                'experiment_name': 'rnn_experiment_1',
                'batch_size': 128,
                'embedding_dim': 8,
                'hidden_dim': 8,
                'epochs': 2,
                'lr': 0.001,
                'num_layers': 3,
                'bidirectional': True,
                'dropout': 0.3,
                'LG': True,
                'opcode_len': 10
            }
        ]
        return get_deep_rnn_expr_list
    else:
        keys, values = zip(*get_deep_rnn_expr_grid.items())
        permutations_dicts = []
        count = 1
        for v in itertools.product(*values):
            temp_dict = dict(zip(keys, v))
            temp_exp = 'rnn_experiment_' + str(count)
            temp_dict['experiment_name'] = temp_exp
            permutations_dicts.append(temp_dict)
            count += 1

        return permutations_dicts


def get_deep_feedforward_expr_list(print_grid=True, simple_list=True):
    """
    ###########################################################
    Template for CNNMalware_1
            {
                'model_name': 'CNNMalware_Model3',
                'experiment_name': 'cnn_experiment_1',
                'batch_size': 512,
                'image_dim': 0,
                'epochs': 1,
                'lr': 0.001,
                'conv1d_image_dim_w': 1024 * 4,
                'feature_type': FEATURE_TYPE_IMAGE
            }
    ###########################################################
    Template for CNNMalware_2
        {
            'model_name': 'CNNMalware_Model4',
            'experiment_name': 'cnn_experiment_1',
            'batch_size': 512,
            'image_dim': 0,
            'epochs': 15,
            'lr': 0.001,
            'conv1d_image_dim_w': 1024 * 4,
            'c1_out': 64,
            'c1_kernel': 32,
            'c1_padding': 2,
            'c1_stride': 2,
            'c2_out': 32,
            'c2_kernel': 8,
            'c2_padding': 2,
            'c2_stride': 2,
            'feature_type': FEATURE_TYPE_IMAGE
        }
    ###########################################################
    Template for CNNMalware_3
        {
            'model_name': 'CNNMalware_Model5',
            'experiment_name': 'cnn_experiment_1',
            'batch_size': 512,
            'image_dim': 256,
            'epochs': 15,
            'lr': 0.001,
            'opcode_len': 500,
            'embedding_dim': 128,
            'hidden_dim': 128,
            'n_filters': 3,
            'filter_sizes': [3, 6],
            'dropout': 0,
            'feature_type': FEATURE_TYPE_OPCODE
        }
    ###########################################################
    """
    simple_list = False
    get_deep_feedforward_expr_grid = {
        'model_name': ['CNNMalware_Model5'],
        'batch_size': [256],
        'epochs': [20],
        'lr': [0.001],
        'opcode_len': [5000],
        'embedding_dim': [512],
        'n_filters': [16, 32],
        'filter_sizes': [[16, 24, 32], [32, 64, 128]],
        'dropout': [0.3],
        'feature_type': [FEATURE_TYPE_OPCODE]
    }

    if not simple_list and print_grid:
        print_line()
        print(f'Experiments Grid')
        print(get_deep_feedforward_expr_grid)
        print_line()

    if simple_list:
        get_deep_feedforward_expr_list = [
            {'model_name': 'CNNMalware_Model2', 'batch_size': 256, 'image_dim': 256, 'epochs': 50, 'lr': 0.001,
             'experiment_name': 'experiment_35', 'feature_type': FEATURE_TYPE_IMAGE},
            {'model_name': 'CNNMalware_Model2', 'batch_size': 256, 'image_dim': 256, 'epochs': 50, 'lr': 0.0001,
             'experiment_name': 'experiment_36', 'feature_type': FEATURE_TYPE_IMAGE},
            {'model_name': 'CNNMalware_Model2', 'batch_size': 256, 'image_dim': 512, 'epochs': 50, 'lr': 0.001,
             'experiment_name': 'experiment_37', 'feature_type': FEATURE_TYPE_IMAGE},
            {'model_name': 'CNNMalware_Model2', 'batch_size': 256, 'image_dim': 512, 'epochs': 50, 'lr': 0.0001,
             'experiment_name': 'experiment_38', 'feature_type': FEATURE_TYPE_IMAGE},
            {'model_name': 'CNNMalware_Model2', 'batch_size': 64, 'image_dim': 1024, 'epochs': 20, 'lr': 0.001,
             'experiment_name': 'experiment_39', 'feature_type': FEATURE_TYPE_IMAGE},
            {'model_name': 'CNNMalware_Model2', 'batch_size': 64, 'image_dim': 1024, 'epochs': 20, 'lr': 0.0001,
             'experiment_name': 'experiment_40', 'feature_type': FEATURE_TYPE_IMAGE}
        ]
        return get_deep_feedforward_expr_list
    else:
        keys, values = zip(*get_deep_feedforward_expr_grid.items())
        permutations_dicts = []
        count = 1
        for v in itertools.product(*values):
            temp_dict = dict(zip(keys, v))
            temp_exp = 'experiment_' + str(count)
            temp_dict['experiment_name'] = temp_exp
            permutations_dicts.append(temp_dict)
            count += 1

        return permutations_dicts


def get_shallow_expr_list():
    """list_shallow_expr = [
        {
            'experiment_name': 'XGB_experiment_1',
            'model_name': 'XGB',
            'param_grid': {
                'max_depth': [5, 15, 20, 50, 100],
                'learning_rate': [0.1, 0.01, 0.001],
                'n_estimators': list(range(10, 500, 50)),
            }
        },
        {
            'experiment_name': 'RandomForest_experiment_1',
            'model_name': 'RandomForest',
            'param_grid': {
                'criterion': ['gini', 'entropy'],
                'n_estimators': [10, 40, 100, 500],
            }
        },
        {
            'experiment_name': 'Knn_experiment_1',
            'model_name': 'Knn',
            'param_grid': {
                'n_neighbors': list(range(130, 190, 10)),
                'p': [1, 2],
            }
        },
        {
            'experiment_name': 'Knn_experiment_2',
            'model_name': 'Knn',
            'param_grid': {
                'n_neighbors': list(range(130, 190, 10)),
                'p': [2],
            }
        }
        {
            'experiment_name': 'Knn_experiment_1',
            'model_name': 'Knn',
            'param_grid': {
                'n_neighbors': list(range(50, 160, 30)),
                'p': [1, 2, 3],
                'weights': ['uniform', 'distance'],
                'algorithm': ['ball_tree', 'kd_tree', 'brute']
            }
        }
    ]"""

    list_shallow_expr = [
        {
            'experiment_name': 'XGB_experiment_1',
            'model_name': 'XGB',
            'param_grid': {
                'max_depth': [5, 15, 20, 50, 100],
                'learning_rate': [0.1, 0.01, 0.001],
                'n_estimators': list(range(10, 500, 50)),
            }
        },
        {
            'experiment_name': 'RandomForest_experiment_1',
            'model_name': 'RandomForest',
            'param_grid': {
                'criterion': ['gini', 'entropy'],
                'n_estimators': [10, 20, 30, 40, 100, 500],
                'max_features': ['sqrt', 'log2'],
            }
        },
        {
            'experiment_name': 'Knn_experiment_1',
            'model_name': 'Knn',
            'param_grid': {
                'n_neighbors': list(range(1, 170, 10)),
                'p': [1, 2, 3],
                'weights': ['uniform', 'distance'],
                'algorithm': ['ball_tree', 'kd_tree', 'brute']
            }
        }
    ]

    return list_shallow_expr


def get_conv_transfer_learning_expr_list():

    # choose model of your choice !!
    list_tl_expr = [
        {
            'experiment_name': 'tl_experiment_1',
            'model_name': 'vgg19',
            'batch_size': 256,
            'image_dim': 256,
            'epochs': 20,
            'lr': 0.0001
        }
    ]

    return list_tl_expr


def get_malware_experiments_list(expr_type):

    expr_list = None
    if expr_type == DEEP_FF:
        expr_list = get_deep_feedforward_expr_list()
    if expr_type == DEEP_RNN:
        expr_list = get_deep_rnn_expr_list()

    if expr_list is None:
        raise Exception('Unknown experiment type')
    else:
        return expr_list


def create_deep_image_model(model_params):

    image_dim = model_params['image_dim']
    num_of_classes = model_params['num_of_classes']
    model_name = model_params['model_name']

    model = None
    if model_name == 'CNNMalware_Model1':
        if image_dim == 0:
            raise Exception("CNNMalware_Model1 needs image_dim != 0")
        model = CNNMalware_Model1(image_dim=image_dim, num_of_classes=num_of_classes).to(device)

    if model_name == 'CNNMalware_2':
        if image_dim != 0:
            raise Exception("CNNMalware_Model4 needs image_dim = 0")

        conv1d_image_dim_w = model_params['conv1d_image_dim_w']
        c1_out = model_params['c1_out']
        c1_kernel = model_params['c1_kernel']
        c1_padding = model_params['c1_padding']
        c1_stride = model_params['c1_stride']

        c2_out = model_params['c2_out']
        c2_kernel = model_params['c2_kernel']
        c2_padding = model_params['c2_padding']
        c2_stride = model_params['c2_stride']

        model = CNNMalware_Model2(image_dim_w=conv1d_image_dim_w, num_of_classes=num_of_classes,
                                  c1_out=c1_out, c1_kernel=c1_kernel, c1_padding=c1_padding, c1_stride=c1_stride,
                                  c2_out=c2_out, c2_kernel=c2_kernel, c2_padding=c2_padding, c2_stride=c2_stride,
                                  ).to(device)

    if model is None:
        raise Exception("Unknown Image-based model name given")

    return model


def get_pretrained_image_dim(model_name):

    if model_name == 'resnet152':
        return 224
    if model_name == 'vgg19':
        return 224
    raise Exception("Unknown model name given for tl")


def create_deep_opcode_model(model_params):

    input_dim = model_params['input_dim']
    output_dim = model_params['output_dim']
    embedding_dim = model_params['embedding_dim']
    batch_size = model_params['batch_size']
    num_of_classes = model_params['num_of_classes']
    model_name = model_params['model_name']

    hidden_dim = 0
    if 'hidden_dim' in model_params.keys():
        hidden_dim = model_params['hidden_dim']

    if 'bidirectional' in model_params.keys():
        bidirectional = model_params['bidirectional']

    if 'dropout' in model_params.keys():
        dropout = model_params['dropout']

    if 'num_layers' in model_params.keys():
        num_layers = model_params['num_layers']

    model = None
    if model_name == 'RNNMalware_Model1':
        model = RNNMalware_Model1(input_dim=input_dim, embedding_dim=embedding_dim, hidden_dim=hidden_dim,
                                  output_dim=output_dim, batch_size=batch_size,
                                  num_layers=num_layers, bidirectional=bidirectional, dropout=dropout)

    if model_name == 'LSTMMalware_Model1':
        model = LSTMMalware_Model1(input_dim=input_dim, embedding_dim=embedding_dim, hidden_dim=hidden_dim,
                                   output_dim=output_dim, batch_size=batch_size,
                                   num_layers=num_layers, bidirectional=bidirectional, dropout=dropout)

    if model_name == 'GRUMalware_Model1':
        model = GRUMalware_Model1(input_dim=input_dim, embedding_dim=embedding_dim, hidden_dim=hidden_dim,
                                  output_dim=output_dim, batch_size=batch_size,
                                  num_layers=num_layers, bidirectional=bidirectional, dropout=dropout)

    if model_name == 'CNNMalware_3':
        feature_type = model_params['feature_type']
        if feature_type != FEATURE_TYPE_OPCODE:
            raise Exception("CNNMalware_Model5 needs Opcode features")

        input_dim = model_params['input_dim']
        output_dim = model_params['output_dim']
        embedding_dim = model_params['embedding_dim']
        n_filters = model_params['n_filters']
        filter_sizes = model_params['filter_sizes']
        dropout = model_params['dropout']

        model = CNNMalware_Model3(input_dim=input_dim, embedding_dim=embedding_dim,
                                  n_filters=n_filters, filter_sizes=filter_sizes,
                                  output_dim=output_dim, dropout=dropout
                                  ).to(device)
    if model is None:
        raise Exception("Unknown Opcode-based model name given")

    return model



