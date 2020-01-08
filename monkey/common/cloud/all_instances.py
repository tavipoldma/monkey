from typing import List

from common.cloud.aws.aws_instance import AwsInstance
from common.cloud.azure.azure_instance import AzureInstance
from common.cloud.instance import CloudInstance

all_cloud_instances = [AwsInstance(), AzureInstance()]


def get_all_cloud_instances() -> List[CloudInstance]:
    return all_cloud_instances
