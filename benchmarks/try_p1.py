from locust import HttpUser, task
import random
import string

LETTERS = string.ascii_letters
PASTES_SO_FAR = 0

class PasteBin(HttpUser):
    def paste(self):
        global PASTES_SO_FAR
        PASTES_SO_FAR += 1
        len_title = random.randint(1, 100)
        len_content = random.randint(1, 400)
        title = ''.join(random.choice(LETTERS) for i in range(len_title))
        content = ''.join(random.choice(LETTERS) for i in range(len_content))
        return self.client.post(url="/api/paste", json={"title": title, "content": content})
    
    def get(self):
        global PASTES_SO_FAR
        paste_id = random.randint(1, PASTES_SO_FAR)
        return self.client.get(url=f"/api/{paste_id}")

    def recents(self):
        return self.client.post(url=f"/api/recents")

    @task
    def test_requests(self):
        api_type = random.randint(0, 2)
        if api_type == 0:
            _ = self.paste()
        elif api_type == 1 and PASTES_SO_FAR > 0:
            _ = self.get()
        else:
            _ = self.recents()