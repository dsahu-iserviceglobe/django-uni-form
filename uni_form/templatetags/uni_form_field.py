from django import template

register = template.Library()

class_converter = {
    "textinput": "textinput textInput",
    "fileinput": "fileinput fileUpload",
    "passwordinput": "textinput textInput",
}

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"

@register.filter
def with_class(field):
    class_name = field.field.widget.__class__.__name__.lower()
    class_name = class_converter.get(class_name, class_name)
    initial_classes = field.field.widget.attrs.pop('class', '')
    error_class = " input-error" if field.errors else ""
    field.field.widget.attrs['class'] = "%s %s%s" %(initial_classes,
            field.css_classes(extra_classes=class_name), error_class)

    return field
