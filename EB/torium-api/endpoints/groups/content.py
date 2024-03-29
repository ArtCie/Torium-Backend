from datetime import datetime
from typing import Optional


class Content:
    def __init__(self, group_id: Optional[int], name: Optional[str], admin_id: int, description: Optional[str], status: Optional[str]):
        self._group_id = group_id
        self._name = name
        self._admin_id = admin_id
        self._status = status
        self._description = description
        self._timestamp = datetime.now()

    @property
    def group_id(self) -> int:
        return self._group_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def admin_id(self) -> int:
        return self._admin_id

    @property
    def status(self) -> str:
        return self._status

    @property
    def description(self) -> str:
        return self._description

    @property
    def timestamp(self) -> datetime:
        return self._timestamp


class ContentConverter:
    @staticmethod
    def convert_post(content: dict) -> Content:
        return Content(None, content["name"], content["admin_id"], content["description"], None)

    @staticmethod
    def convert_delete(content: dict) -> Content:
        return Content(content["id"], None, content["admin_id"], None, None)

    @staticmethod
    def convert(content: dict) -> Content:
        return Content(content["id"], content["name"], content["admin_id"], content["description"],
                       status="admin" if not content.get("status") else content["status"])
