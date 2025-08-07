from django.apps import AppConfig


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'

    def ready(self) -> None:
        from langgraph_resources import store,checkpointer
        store.setup()
        checkpointer.setup()