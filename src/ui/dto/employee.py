from pydantic import (
    BaseModel,
    UUID4,
    field_validator,
    ValidationInfo,
)


class PersonalInfoDTO(BaseModel):
    name: str
    surname: str

    @field_validator("name", "surname")
    def validate_and_normalize_name(cls, value: str, info: ValidationInfo) -> str:
        _ = value.strip().title()

        field_name = info.field_name.capitalize() if info.field_name else None

        if len(value) < 1:
            raise ValueError(f"{field_name} cannot be empty")

        if len(value) > 50:
            raise ValueError(f"{field_name} cannot exceed 50 characters")

        if not all(char.isalpha() or char.isspace() for char in value):
            raise ValueError(f"{field_name} must contain only letters and spaces")

        return value


class EmploymentDetailsDTO(BaseModel):
    fte: float
    utilization_rate: float

    @field_validator("fte", "utilization_rate")
    def validate_employment_details(cls, value: float, info: ValidationInfo) -> float:
        field_name = info.field_name.capitalize() if info.field_name else None

        if value < 0 or value > 1:
            raise ValueError(f"{field_name} must be between 0.0 and 1.0")

        return value


class CompanyCredentialsDTO(BaseModel):
    username: str
    acronym: str

    @field_validator("username")
    def validate_and_normalize_username(cls, value: str, info: ValidationInfo) -> str:
        _ = value.strip().lower()

        field_name = info.field_name.capitalize() if info.field_name else None

        min_length = 3
        max_length = 20

        if len(value) < 1:
            raise ValueError(f"{field_name} cannot be empty")

        if len(value) < min_length:
            raise ValueError(f"{field_name} must be atleast {min_length} characters")

        if len(value) > max_length:
            raise ValueError(f"{field_name} cannot exceed {max_length} characters")

        if not all(char.isalpha() for char in value):
            raise ValueError(f"{field_name} must contain only letters")

        return value

    # Normalize acronym to upper case
    @field_validator("acronym")
    def validate_and_normalize_acronym(cls, value: str, info: ValidationInfo) -> str:
        _ = value.strip().upper()

        field_name = info.field_name.capitalize() if info.field_name else None

        acronym_length = 3

        if len(value) != acronym_length:
            raise ValueError(f"{field_name} must be {acronym_length} characters")

        if not all(char.isalpha() for char in value):
            raise ValueError(f"{field_name} must contain only letters")

        return value


class EmployeeDTO(BaseModel):
    id: UUID4
    personal: PersonalInfoDTO
    employment: EmploymentDetailsDTO
    credentials: CompanyCredentialsDTO
