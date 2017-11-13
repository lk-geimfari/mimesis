from mimesis.schema import Field

_ = Field('en')

app_schema = (
    lambda: {
        "id": _('uuid'),
        "name": _('word'),
        "version": _('version'),
        "owner": {
            "email": _('email'),
            "token": _('token'),
            "creator": _('full_name', gender='female')
        }
    }
)

result = _.fill(schema=app_schema, iterations=10)

print(result)
