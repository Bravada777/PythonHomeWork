from project_page import BoardsPage

# Данные для авторизации
ID =
TOKEN =
BASE_URL =

BOARD_ID = "c939ac7c-70d0-400e-b834-d352262b0e10"  # ID реальной доски
NON_EXISTENT_BOARD_ID = "00000000-0000-0000-0000-000000000000"  # Несуществующий ID

boards_page = BoardsPage(BASE_URL, TOKEN)

# Позитивный тест для метода POST
def test_create_new_board():
    """Позитивный тест: создание новой доски с валидными данными"""
    response = boards_page.create_board("Новая Доска", ID)
    assert response.status_code == 201, f"Ожидался статус-код 201, получили {response.status_code}: {response.text}"

# Негативный тест для метода POST
def test_create_invalid_board():
    """Негативный тест: попытка создать доску с пустым названием"""
    response = boards_page.create_board("", ID)
    assert response.status_code == 400, f"Ожидался статус-код 400, получили {response.status_code}: {response.text}"

# Позитивный тест для метода GET
def test_get_existing_board():
    """Позитивный тест: получение информации о существующей доске"""
    response = boards_page.get_board(BOARD_ID)
    assert response.status_code == 200, f"Ожидался статус-код 200, получили {response.status_code}: {response.text}"

# Негативный тест для метода GET
def test_get_nonexistent_board():
    """Негативный тест: попытка получить информацию о несуществующей доске"""
    response = boards_page.get_board(NON_EXISTENT_BOARD_ID)
    assert response.status_code == 404, f"Ожидался статус-код 404, получили {response.status_code}: {response.text}"

# Позитивный тест для метода PUT
def test_update_existing_board():
    """Позитивный тест: обновление существующей доски с валидными данными"""
    response = boards_page.update_board(BOARD_ID, "Новая страна")
    assert response.status_code == 200, f"Ожидался статус-код 200, получили {response.status_code}: {response.text}"

# Негативный тест для метода PUT
def test_update_nonexistent_board():
    """Негативный тест: попытка обновить несуществующую доску"""
    response = boards_page.update_board(NON_EXISTENT_BOARD_ID, "New Title")
    assert response.status_code == 404, f"Ожидался статус-код 404, получили {response.status_code}: {response.text}"
