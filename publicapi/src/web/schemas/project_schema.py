from marshmallow import EXCLUDE, Schema, fields

class ProjectCreateSchema(Schema):
    title = fields.Str(required=True)

    class Meta:
        unknown = EXCLUDE
