class LinkedStack:
    """Ngăn xếp LIFO được triển khai bằng danh sách liên kết đơn."""

    # ------------------------ lớp _Node lồng nhau ------------------------
    class _Node:
        """Lớp nhẹ, không công khai để lưu trữ một nút liên kết đơn."""
        __slots__ = '_element', '_next'     # tối ưu hóa bộ nhớ

        def __init__(self, element, next):   # khởi tạo các trường của nút
            self._element = element          # tham chiếu đến phần tử của người dùng
            self._next = next                # tham chiếu đến nút tiếp theo

    # ------------------------ các phương thức ngăn xếp ------------------------
    def __init__(self):
        """Tạo một ngăn xếp rỗng."""
        self._head = None                    # tham chiếu đến nút đầu
        self._size = 0                       # số lượng phần tử trong ngăn xếp

    def __len__(self):
        """Trả về số lượng phần tử trong ngăn xếp."""
        return self._size

    def is_empty(self):
        """Trả về True nếu ngăn xếp rỗng."""
        return self._size == 0

    def push(self, e):
        """Thêm phần tử e vào đỉnh của ngăn xếp."""
        self._head = self._Node(e, self._head)    # tạo và liên kết nút mới
        self._size += 1

    def top(self):
        """Trả về (nhưng không xóa) phần tử ở đỉnh của ngăn xếp.

        Raise Empty exception nếu ngăn xếp rỗng.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element           # đỉnh ngăn xếp ở đầu danh sách

    def pop(self):
        """Xóa và trả về phần tử từ đỉnh của ngăn xếp (theo LIFO).

        Raise Empty exception nếu ngăn xếp rỗng.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next        # bỏ qua nút đỉnh cũ
        self._size -= 1
        return answer
