from locust import HttpUser, task
import random

PASTES_SO_FAR = 0

class PasteBin(HttpUser):
    @task
    def paste(self):
        global PASTES_SO_FAR
        PASTES_SO_FAR += 1
        title = f"This is the title of paste number {PASTES_SO_FAR}"
        content = f"Generating random number, {random.randint(1, 400)}"
        self.client.post(url="/api/paste", json={"title": title, "content": content})
    
    @task(2)
    def get(self):
        paste_id = random.randint(1, PASTES_SO_FAR)
        self.client.get(url=f"/api/{paste_id}")

    @task(3)
    def recents(self):
        self.client.post(url=f"/api/recents")

    def on_start(self):
        self.paste()