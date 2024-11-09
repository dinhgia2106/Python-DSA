from Empty import Empty


class HeapPriorityQueue(PriorityQueueBase):  # lớp cơ sở định nghĩa _Item
    """Hàng đợi ưu tiên theo hướng min được triển khai bằng heap nhị phân."""

    # --------------------- các hành vi không công khai ---------------------
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)    # chỉ số vượt quá cuối mảng?

    def _has_right(self, j):
        return self._right(j) < len(self._data)   # chỉ số vượt quá cuối mảng?

    def _swap(self, i, j):
        """Hoán đổi các phần tử tại chỉ số i và j của mảng."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)                  # đệ quy tại vị trí của cha

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):               # mặc dù bên phải có thể nhỏ hơn
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                # đệ quy tại vị trí của con nhỏ nhất
                self._downheap(small_child)

    # --------------------- các hành vi công khai ---------------------
    def __init__(self):
        """Tạo một Priority Queue rỗng mới."""
        self._data = []

    def __len__(self):
        """Trả về số lượng phần tử trong hàng đợi ưu tiên."""
        return len(self._data)

    def add(self, key, value):
        """Thêm một cặp key-value vào hàng đợi ưu tiên."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)        # upheap vị trí mới thêm vào

    def min(self):
        """Trả về nhưng không xóa bộ (k,v) có key nhỏ nhất.

        Raise Empty exception nếu rỗng.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Xóa và trả về bộ (k,v) có key nhỏ nhất.

        Raise Empty exception nếu rỗng.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        # đặt phần tử nhỏ nhất vào cuối
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()                   # và xóa nó khỏi list
        self._downheap(0)                         # sau đó sửa lại gốc
        return (item._key, item._value)
