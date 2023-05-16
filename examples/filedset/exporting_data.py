from mimesis.keys import maybe
from mimesis.locales import Locale
from mimesis.schema import Field, Schema

_ = Field(locale=Locale.EN)
schema = Schema(
    schema=lambda: {
        "pk": _("increment"),
        "name": _("text.word", key=maybe("N/A", probability=0.2)),
        "version": _("version"),
        "timestamp": _("timestamp", posix=False),
    },
    iterations=1000,
)
schema.to_csv(file_path="data.csv")
schema.to_json(file_path="data.json")
schema.to_pickle(file_path="data.obj")
