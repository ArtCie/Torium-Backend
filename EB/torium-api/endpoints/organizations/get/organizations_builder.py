from typing import List

from endpoints.organizations.content import Content
from aws.s3_manager import S3Manager


class OrganizationsBuilder:
    def __init__(self):
        self.s3_manager = S3Manager()

    def build_organizations_response(self, organizations: List[Content]):
        return [
            {
                "name": organization.name,
                "url": organization.url,
                "file_name": self.s3_manager.get_presigned_url(organization.file_name)
            }
            for organization in organizations
        ]
