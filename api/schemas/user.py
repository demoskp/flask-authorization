from marshmallow import validate, validates_schema, ValidationError
from marshmallow.fields import String

from extensions import ma
from models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True, validate=[validate.Length(min=3)], error_messages={
        "required": "The name is required",
        "invalid": "The name is invalid and needs to be a string",
    })
    email = String(required=True, validate=[validate.Email()])

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get("email")

        if User.query.filter_by(email=email).count():
            raise ValidationError(f"Email {email} already exists.")

    class Meta:
        model = User
        load_instance = True
        exclude = ["id", "_password"]


class UserCreateSchema(UserSchema):
    password = String(
        required=True,
        validate=[
            validate.Regexp(r"^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$",
                            error="The password needs to be at least 8 characters long and include a lowercase, uppercase, number and special character.")
        ]
    )