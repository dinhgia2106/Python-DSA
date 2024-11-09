class SortedPriorityQueue(PriorityQueueBase):  # lớp cơ sở định nghĩa _Item
    """Hàng đợi ưu tiên theo hướng min được triển khai với danh sách đã sắp xếp."""

    def __init__(self):
        """Tạo một Priority Queue rỗng mới."""
        self._data = PositionalList()

    def __len__(self):
        """Trả về số lượng phần tử trong hàng đợi ưu tiên."""
        return len(self._data)

    def add(self, key, value):
        """Thêm một cặp key-value."""
        newest = self._Item(key, value)           # tạo instance mới
        walk = self._data.last()                  # duyệt ngược tìm key nhỏ hơn
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)          # key mới là nhỏ nhất
        else:
            self._data.add_after(walk, newest)    # newest đi sau walk

    def min(self):
        """Trả về nhưng không xóa bộ (k,v) có key nhỏ nhất."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Xóa và trả về bộ (k,v) có key nhỏ nhất."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
