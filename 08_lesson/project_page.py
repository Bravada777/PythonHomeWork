import requests


class BoardsPage:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def create_board(self, title, project_id):
        """Создание новой доски."""
        url = f"{self.base_url}/boards"
        payload = {
            "title": title,
            "projectId": project_id
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response

    def get_board(self, board_id):
        """Получение информации о доске."""
        url = f"{self.base_url}/boards/{board_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_board(self, board_id, new_title):
        """Обновление существующей доски."""
        url = f"{self.base_url}/boards/{board_id}"
        payload = {
            "title": new_title
        }
        response = requests.put(url, headers=self.headers, json=payload)
        return response
