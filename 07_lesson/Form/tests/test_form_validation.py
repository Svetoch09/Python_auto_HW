import pytest
from Form.form_pages.FormPage import FormPage

INPUT_DATA = [
    "Иван", "Петров", "Ленина, 55-3", "", "Москва",
    "Россия", "test@skypro.com", "+7985899998787", "QA", "SkyPro"
]
danger_index = 3


class TestFormValidation:

    @pytest.mark.negative
    def test_data_validation_after_submit(self, driver, base_url):
        """
        Тест проверяет валидацию формы, в которой поле
        Zip Code оставлено пустым.
        Ожидается: поле Zip Code (индекс 3)
        будет красным (DANGER_CLASS),
        остальные — зелеными (SUCCESS_CLASS).
        """
        page = FormPage(driver, base_url)
        page.open()
        page.fill_all_fields(INPUT_DATA)
        page.submit_form()
        page.assert_validation_colors(danger_index)
