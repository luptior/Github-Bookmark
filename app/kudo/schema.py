"""
As you may have noticed, the schemas are inheriting from Schema a package from the [marshmallow library]
(https://marshmallow.readthedocs.io/en/3.0/), marshmallow is an ORM/ODM/framework-agnostic library for
serializing/deserializing complex data types, such as objects, to and from native Python data types.
"""

from marshmallow import Schema, fields


class GithubRepoSchema(Schema):
    id = fields.Int(required=True)
    repo_name = fields.Str()
    full_name = fields.Str()
    language = fields.Str()
    description = fields.Str()
    repo_url = fields.URL()


class KudoSchema(GithubRepoSchema):
    user_id = fields.Email(required=True)
