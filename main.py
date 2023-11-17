from controller.controller import Controller
from model.model import Model
from view.view import View

persistence = Controller(View(), Model())
persistence.start()
