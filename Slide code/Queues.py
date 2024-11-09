from Empty import Empty

class ArrayQueue:
    """Hàng đợi FIFO được triển khai bằng list Python làm bộ nhớ."""
    DEFAULT_CAPACITY = 10      # dung lượng vừa phải cho tất cả hàng đợi mới

    def __init__(self):
        """Tạo một hàng đợi rỗng."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Trả về số lượng phần tử trong hàng đợi."""
        return self._size

    def is_empty(self):
        """Trả về True nếu hàng đợi rỗng."""
        return self._size == 0

    def first(self):
        """Trả về (nhưng không xóa) phần tử ở đầu hàng đợi.

        Raise Empty exception nếu hàng đợi rỗng.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Xóa và trả về phần tử đầu tiên của hàng đợi (theo FIFO).

        Raise Empty exception nếu hàng đợi rỗng.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None    # hỗ trợ thu gom rác
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Thêm một phần tử vào cuối hàng đợi."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))    # gấp đôi kích thước mảng
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):                  # giả định cap >= len(self)
        """Thay đổi kích thước thành list mới có dung lượng >= len(self)."""
        old = self._data                     # giữ lại list cũ
        self._data = [None] * cap            # cấp phát list với dung lượng mới
        walk = self._front
        for k in range(self._size):          # chỉ xét các phần tử hiện có
            self._data[k] = old[walk]        # di chuyển các chỉ số có chủ đích
            walk = (1 + walk) % len(old)     # sử dụng kích thước cũ làm modulo
        self._front = 0                      # front đã được căn chỉnh lại
