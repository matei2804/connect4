from UI.ui import ui
from Service.service import service
from Repository.repo import repo

repository = repo()
service = service(repository)
ui = ui(service)

ui.start_game()
