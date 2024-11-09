class _DoublyLinkedBase:
    """Lớp cơ sở cung cấp cấu trúc danh sách liên kết đôi."""

    class _Node:
        """Lớp nhẹ, không công khai để lưu trữ một nút liên kết đơn."""
        __slots__ = '_element', '_next'     # tối ưu hóa bộ nhớ

        def __init__(self, element, next):   # khởi tạo các trường của nút
            self._element = element          # tham chiếu đến phần tử của người dùng
            self._next = next                # tham chiếu đến nút tiếp theo

    def __init__(self):
        """Tạo một danh sách rỗng."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer        # trailer nằm sau header
        self._trailer._prev = self._header        # header nằm trước trailer
        self._size = 0                           # số lượng phần tử

    def __len__(self):
        """Trả về số lượng phần tử trong danh sách."""
        return self._size

    def is_empty(self):
        """Trả về True nếu danh sách rỗng."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Thêm phần tử e giữa hai nút hiện có và trả về nút mới."""
        newest = self._Node(
            e, predecessor, successor)  # liên kết với các nút lân cận
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Xóa nút không phải sentinel khỏi danh sách và trả về phần tử của nó."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                        # ghi nhận phần tử bị xóa
        node._prev = node._next = node._element = None  # vô hiệu hóa nút
        return element                                 # trả về phần tử đã xóa
