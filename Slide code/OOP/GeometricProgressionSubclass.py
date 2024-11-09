from ProgessionBaseClass import Progression


class GeometricProgression(Progression):
    """Iterator tạo ra một cấp số nhân."""

    def __init__(self, base=2, start=1):
        """Tạo một cấp số nhân mới.

        base    hằng số nhân vào mỗi số hạng (mặc định là 2)
        start   số hạng đầu tiên của cấp số nhân (mặc định là 1)
        """
        super().__init__(start)              # khởi tạo lớp cơ sở
        self._base = base

    def _advance(self):                      # ghi đè phương thức kế thừa
        """Cập nhật giá trị hiện tại bằng cách nhân với hằng số."""
        self._current *= self._base
