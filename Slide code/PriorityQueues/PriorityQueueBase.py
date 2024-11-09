class PriorityQueueBase:
    """Lớp cơ sở trừu tượng cho hàng đợi ưu tiên."""

    class _Item:
        """Lớp composite nhẹ để lưu trữ các phần tử hàng đợi ưu tiên."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key    # so sánh các phần tử dựa trên key

    def is_empty(self):                      # phương thức cụ thể giả định len trừu tượng
        """Trả về True nếu hàng đợi ưu tiên rỗng."""
        return len(self) == 0
