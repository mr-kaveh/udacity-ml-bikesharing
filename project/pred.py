from ray import tune
from datetime import datetime
from autogluon.multimodal import MultiModalPredictor


predictor_hpo = MultiModalPredictor(label="count")

hyperparameters = {
            "optimization.learning_rate": tune.uniform(0.00005, 0.001),
            "model.timm_image.checkpoint_name": tune.choice(["ghostnet_100",
                                                             "mobilenetv3_large_100"])
}
hyperparameter_tune_kwargs = {
    "searcher": "bayes", # random
    "scheduler": "ASHA",
    "num_trials": 2,
}
start_time_hpo = datetime.now()
predictor_hpo.fit(
        train_data='dataSets/train.csv',
        hyperparameters=hyperparameters,
        hyperparameter_tune_kwargs=hyperparameter_tune_kwargs,
    )
end_time_hpo = datetime.now()
elapsed_seconds_hpo = (end_time_hpo - start_time_hpo).total_seconds()
elapsed_min_hpo = divmod(elapsed_seconds_hpo, 600)
print("Total fitting time: ", f"{int(elapsed_min_hpo[0])}m{int(elapsed_min_hpo[1])}s")