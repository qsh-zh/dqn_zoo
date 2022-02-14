import os
import shutil
import socket

__all__ = ["Wandb", "WandbUrls"]


class WandbUrls:  # pylint: disable=too-few-public-methods
    def __init__(self, url):

        url_hash = url.split("/")[-1]
        project = url.split("/")[-3]
        entity = url.split("/")[-4]

        self.weight_url = url
        self.log_url = "https://app.wandb.ai/{}/{}/runs/{}/logs".format(
            entity, project, url_hash
        )
        self.chart_url = "https://app.wandb.ai/{}/{}/runs/{}".format(
            entity, project, url_hash
        )
        self.overview_url = "https://app.wandb.ai/{}/{}/runs/{}/overview".format(
            entity, project, url_hash
        )
        self.hydra_config_url = (
            "https://app.wandb.ai/{}/{}/runs/{}/files/hydra-config.yaml".format(
                entity, project, url_hash
            )
        )
        self.overrides_url = (
            "https://app.wandb.ai/{}/{}/runs/{}/files/overrides.yaml".format(
                entity, project, url_hash
            )
        )

    # pylint: disable=line-too-long
    def __repr__(self):
        msg = "=================================================== WANDB URLS ===================================================================\n"
        for k, v in self.__dict__.items():
            msg += "{}: {}\n".format(k.upper(), v)
        msg += "=================================================================================================================================\n"
        return msg

    def to_dict(self):
        return {k.upper(): v for k, v in self.__dict__.items()}


class Wandb:
    IS_ACTIVE = False
    cfg = None
    run = None

    @staticmethod
    def set_urls_to_model(model, url):
        wandb_urls = WandbUrls(url)
        model.wandb = wandb_urls

    @staticmethod
    def prep_args(name):
        wandb_args = {
            "project": "dqn_zoo",
            "resume": "allow",
            "name": name,
            # "tags": cfg.wandb.tags,
            "config": {
                "run_path": os.getcwd(),
                "host": socket.gethostname(),
            },
            "save_code": True,
        }

        return wandb_args

    @staticmethod
    def launch(cfg, launch: bool, name: str):
        if launch:
            import wandb

            Wandb.IS_ACTIVE = True
            wandb_args = Wandb.prep_args(name)
            Wandb.run = wandb.init(**wandb_args)
            Wandb.run.config.update(cfg)
        return Wandb.run

    @staticmethod
    def add_file(file_path: str):
        if not Wandb.IS_ACTIVE:
            return
        import wandb

        filename = os.path.basename(file_path)
        shutil.copyfile(file_path, os.path.join(wandb.run.dir, filename))

    @staticmethod
    def log(*args, **kargs):
        if not Wandb.IS_ACTIVE:
            return
        import wandb

        wandb.log(*args, **kargs)

    @staticmethod
    def finish():
        if not Wandb.IS_ACTIVE:
            return
        import wandb

        wandb.finish()
