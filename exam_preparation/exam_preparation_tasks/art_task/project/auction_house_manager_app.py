from project.artifacts.base_artifact import BaseArtifact
from project.collectors.base_collector import BaseCollector
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.private_collector import PrivateCollector
from project.collectors.museum import Museum


class AuctionHouseManagerApp:
    artifacts: list[BaseArtifact]
    collectors: list[BaseCollector]
    VALID_COLLECTORS = ["Museum", "PrivateCollector"]
    VALID_ARTIFACTS = ["ContemporaryArtifact", "RenaissanceArtifact"]

    def __init__(self):
        self.artifacts = []
        self.collectors = []
        self.__sold_artifacts: list[BaseArtifact] = []

    @staticmethod
    def subject_existence(request_name: str, target_collection: list):
        return next((target for target in target_collection if target.name == request_name), None)

    def find_subject_in_collection(self, requested_type, request_name, subject, target_collection):

        target_class = globals().get(requested_type)
        if target_class:
            if self.subject_existence(request_name, target_collection):
                raise ValueError(f"{request_name} has been already registered!")
            return target_class
        else:
            raise ValueError(f"Unknown {subject} type!")

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.VALID_ARTIFACTS:
            raise ValueError("Unknown artifact type!")

        target_class = self.find_subject_in_collection(artifact_type, artifact_name, 'artifact', self.artifacts)
        if target_class:
            artifact = target_class(artifact_name, artifact_price, artifact_space)
            self.artifacts.append(artifact)
            return f"{artifact_name} is successfully added to the auction as {artifact_type}."
        return None

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.VALID_COLLECTORS:
            raise ValueError("Unknown collector type!")

        target_class = self.find_subject_in_collection(collector_type, collector_name, 'collector', self.collectors)
        if target_class:
            collector = target_class(collector_name)
            self.collectors.append(collector)
            return f"{collector_name} is successfully registered as a {collector_type}."
        return None

    def remove_artifact(self, artifact_name: str):
        artifact = self.subject_existence(artifact_name, self.artifacts)
        if artifact:
            self.artifacts.remove(artifact)
            return f"Removed {artifact.artifact_information()}"
        return "No such artifact."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector: BaseCollector = self.subject_existence(collector_name, self.collectors)
        if collector:
            artifact: BaseArtifact = self.subject_existence(artifact_name, self.artifacts)
            if artifact:
                if collector.can_purchase(artifact.price, artifact.space_required):
                    collector.purchased_artifacts.append(artifact)
                    self.remove_artifact(artifact_name)
                    self.__sold_artifacts.append(artifact)
                    collector.available_money -= artifact.price
                    collector.available_space -= artifact.space_required
                    return f"{collector.name} purchased {artifact.name} for a price of {artifact.price:.2f}."

                return f"Purchase is impossible."

            else:
                raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        raise ValueError(f"Collector {collector_name} is not registered to the auction!")

    def fundraising_campaigns(self, max_money: float):
        count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count += 1
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        result_string = f"**Auction statistics**\nTotal number of sold artifacts: {len(self.__sold_artifacts)}\nAvailable artifacts for sale: {len(self.artifacts)}\n***"
        for collector in sorted(self.collectors, key=lambda x: (-len(x.purchased_artifacts), x.name)):
            result_string += "\n" + str(collector)
        return result_string.strip()
