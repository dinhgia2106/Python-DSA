from ProgessionBaseClass import Progression


class ArithmeticProgression(Progression):
    """Iterator tạo ra một cấp số cộng."""

    def __init__(self, increment=1, start=0):
        """Tạo một cấp số cộng mới.

        increment   hằng số cộng vào mỗi số hạng (mặc định là 1)
        start      số hạng đầu tiên của cấp số cộng (mặc định là 0)
        """
        super().__init__(start)              # khởi tạo lớp cơ sở
        self._increment = increment

    def _advance(self):                      # ghi đè phương thức kế thừa
        """Cập nhật giá trị hiện tại bằng cách cộng thêm hằng số."""
        self._current += self._increment
