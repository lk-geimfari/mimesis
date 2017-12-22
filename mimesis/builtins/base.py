from mimesis.providers import BaseProvider


class BaseSpecProvider(BaseProvider):
    # TODO: Docs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
