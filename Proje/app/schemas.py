from marshmallow import Schema,fields

class PlainEgitimSchema(Schema):
    id = fields.Str(dump_only=True)
    egitim = fields.Str(required=True)
    sure = fields.Int(required=True)

class EgitimSchema(PlainEgitimSchema):
    birim_id = fields.Int(required=True,load_only=True)
    egitim = fields.Nested(PlainEgitimSchema(),dump_only=True)

    
class EgitimUpdateSchema(Schema):
    egitim = fields.Str()
    sure = fields.Int()

class PlainBirimSchema(Schema):
    id = fields.Str(dump_only=True)
    birim = fields.Str(required=True)


class BirimSchema(PlainBirimSchema):
    egitimler = fields.List(fields.Nested(PlainEgitimSchema()),dump_only=True)
    