from Empty import Empty
from PriorityQueueBase import PriorityQueueBase


class UnsortedPriorityQueue(PriorityQueueBase):  # lớp cơ sở định nghĩa _Item
    """Hàng đợi ưu tiên theo hướng min được triển khai với danh sách không sắp xếp."""

    def _find_min(self):                         # tiện ích không công khai
        """Trả về Position của phần tử có key nhỏ nhất."""
        if self.is_empty():                      # is_empty được kế thừa từ lớp cơ sở
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Tạo một Priority Queue rỗng mới."""
        self._data = PositionalList()

    def __len__(self):
        """Trả về số lượng phần tử trong hàng đợi ưu tiên."""
        return len(self._data)

    def add(self, key, value):
        """Thêm một cặp key-value vào hàng đợi ưu tiên."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Trả về nhưng không xóa bộ (k,v) có key nhỏ nhất."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Xóa và trả về bộ (k,v) có key nhỏ nhất."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
