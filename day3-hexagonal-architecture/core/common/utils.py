from typing import Type, TypeVar
import dataclasses

class ObjectMapperUtil:
    T = TypeVar("T")

    @staticmethod
    def map(source_model_object, destination_domain_class: Type[T]) -> T:
        domain_fields = [
            field.name for field in dataclasses.fields(destination_domain_class)
        ]
        if issubclass(type(source_model_object), dict):
            attributes = {
                field: source_model_object.get(field) for field in domain_fields
            }
        else:
            attributes = {
                field: getattr(source_model_object, field, None)
                for field in domain_fields
            }
        return destination_domain_class(**attributes)