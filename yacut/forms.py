from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class YacutForm(FlaskForm):
    original_link = StringField(
        "Длинная ссылка",
        validators=[DataRequired(message="Обязательное поле"), Length(1, 256)],
    )

    custom_id = StringField(
        "Ваш вариант короткой ссылки", validators=[Length(1, 16), Optional()]
    )

    submit = SubmitField("Создать")
