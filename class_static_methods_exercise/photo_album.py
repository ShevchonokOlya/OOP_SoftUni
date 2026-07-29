from math import ceil

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list[str]] = [[] for i in range(0, self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(0, self.pages):
            photos_on_the_page = self.photos[page]
            if len(photos_on_the_page) < self.PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        photo = "[] "
        photo_album = []
        separator = "-" * 11
        photo_album.append(separator)
        for page in range(0, self.pages):
            page = str(photo * len(self.photos[page])).strip()
            photo_album.append(page)
            photo_album.append(separator)

        return "\n".join(photo_album)

#
# import unittest
#
#
# class TestsPhotoAlbum(unittest.TestCase):
#     def test_init_creates_all_attributes(self):
#         album = PhotoAlbum(2)
#         self.assertEqual(album.pages, 2)
#         self.assertEqual(album.photos, [[], []])
#
#     def test_from_photos_should_create_instace(self):
#         album = PhotoAlbum.from_photos_count(12)
#         self.assertEqual(album.pages, 3)
#         self.assertEqual(album.photos, [[], [], []])
#
#     def test_add_photo_with_no_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.add_photo("prom")
#         self.assertEqual(result, "No more free slots")
#
#     def test_add_photo_with_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])
#
#     def test_display_with_one_page(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------")
#
#     def test_display_with_three_pages(self):
#         album = PhotoAlbum(3)
#         for _ in range(8):
#             album.add_photo("asdf")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
#
#
# if __name__ == "__main__":
#     unittest.main()
