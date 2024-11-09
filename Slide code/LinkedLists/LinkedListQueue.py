class LinkedQueue:
    """Hàng đợi FIFO được triển khai bằng danh sách liên kết đơn."""

    class _Node:
        """Lớp nhẹ, không công khai để lưu trữ một nút liên kết đơn."""
        __slots__ = '_element', '_next'     # tối ưu hóa bộ nhớ

        def __init__(self, element, next):   # khởi tạo các trường của nút
            self._element = element          # tham chiếu đến phần tử của người dùng
            self._next = next                # tham chiếu đến nút tiếp theo

    def __init__(self):
        """Tạo một hàng đợi rỗng."""
        self._head = None
        self._tail = None
        self._size = 0                   # số lượng phần tử trong hàng đợi

    def __len__(self):
        """Trả về số lượng phần tử trong hàng đợi."""
        return self._size

    def is_empty(self):
        """Trả về True nếu hàng đợi rỗng."""
        return self._size == 0

    def first(self):
        """Trả về (nhưng không xóa) phần tử ở đầu hàng đợi."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element       # đầu được căn chỉnh với đầu danh sách

    def dequeue(self):
        """Xóa và trả về phần tử đầu tiên của hàng đợi (theo FIFO)."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():             # trường hợp đặc biệt khi hàng đợi rỗng
            self._tail = None           # nút đã xóa đã từng là đuôi
        return answer

    def enqueue(self, e):
        """Thêm một phần tử vào cuối hàng đợi."""
        newest = self._Node(e, None)     # nút sẽ là đuôi mới
        if self.is_empty():
            self._head = newest          # trường hợp đặc biệt: trước đó rỗng
        else:
            self._tail._next = newest
        self._tail = newest             # cập nhật tham chiếu đến nút đuôi
        self._size += 1
