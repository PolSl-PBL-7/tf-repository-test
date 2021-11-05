import wandb

if __name__ == "__main__":
    wandb.init(project="avenue-experiments", entity="polsl-pbl-7")
    run = wandb.init(job_type='test')


    artifact = run.use_artifact('avenue-dataset:latest')

    artifact_dir = artifact.download()