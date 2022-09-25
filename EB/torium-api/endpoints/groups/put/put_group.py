from endpoints.groups.db_manager import DBManager
from endpoints.groups.content import ContentConverter
from endpoints.groups.exceptions import AccessDenied


class PutGroup:
    def __init__(self, kwargs: dict, db_manager: DBManager):
        self._db_manager = db_manager
        self._admin_id = kwargs["admin_id"]
        self.content = ContentConverter.convert(kwargs)

    def process_request(self):
        self._valid_permission()
        self._update_group()

    def _valid_permission(self):
        data = {
            "admin_id": self._admin_id,
            "group_id": self.content.group_id
        }
        if not self._db_manager.valid_permission(data):
            raise AccessDenied("Access Denied!")

    def _update_group(self):
        data = {
            "id": self.content.group_id,
            "name": self.content.name,
            "admin_id": self.content.admin_id
        }
        self._db_manager.update_group(data)