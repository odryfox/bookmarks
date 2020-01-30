from marshmallow import Schema, fields


class BoardSchema(Schema):
    id = fields.Int()
    name = fields.Str()
