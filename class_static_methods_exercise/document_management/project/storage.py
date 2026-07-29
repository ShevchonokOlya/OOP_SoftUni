from project import Category
from project import Document
from project import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    @staticmethod
    def _add_item(item, target_list: list):
        if item not in target_list:
            target_list.append(item)

    def add_category(self, category: Category):
        self._add_item(category, self.categories)

    def add_topic(self, topic: Topic):
        self._add_item(topic, self.topics)


    def add_document(self, document: Document):
        self._add_item(document, self.documents)

    @staticmethod
    def _edit_item(item_id: int, target_list: list, *args):
        taget_object = next((item for item in target_list if item.id == item_id), None)
        if taget_object:
            taget_object.edit(*args)

    def edit_category(self, category_id: int, new_name: str):
        self._edit_item(category_id, self.categories, new_name)


    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self._edit_item(topic_id, self.topics, new_topic, new_storage_folder)


    def edit_document(self, document_id: int, new_file_name: str):
        self._edit_item(document_id, self.documents, new_file_name)

    @staticmethod
    def _delete_item(item_id: int, target_list: list):
        taget_item = next((item  for item in target_list if item.id == item_id), None)
        if taget_item:
            target_list.remove(taget_item)

    def delete_category(self, category_id):
        self._delete_item(category_id , self.categories)

    def delete_topic(self, topic_id):
        self._delete_item(topic_id , self.topics)

    def delete_document(self, document_id):
        self._delete_item(document_id , self.documents)

    def get_document(self, document_id):
        return next((doc for doc in self.documents if doc.id == document_id), None)

    def __repr__(self):
        return '\n'.join(str(doc) for doc in self.documents)