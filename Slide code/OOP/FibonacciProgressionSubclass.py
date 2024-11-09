from ProgessionBaseClass import Progression


class FibonacciProgression(Progression):
    """Iterator tạo ra một dãy Fibonacci tổng quát."""

    def __init__(self, first=0, second=1):
        """Tạo một dãy Fibonacci mới.

        first    số hạng đầu tiên của dãy (mặc định là 0)
        second   số hạng thứ hai của dãy (mặc định là 1)
        """
        super().__init__(first)              # khởi tạo lớp cơ sở
        self._prev = second - first          # giá trị giả đứng trước số đầu tiên

    def _advance(self):                      # ghi đè phương thức kế thừa
        """Cập nhật giá trị hiện tại bằng cách lấy tổng của hai số trước đó."""
        self._prev, self._current = self._current, self._current + self._prev
