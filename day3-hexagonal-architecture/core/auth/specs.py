from dataclasses import dataclass

@dataclass
class AuthRegistrationSpec:
    username: str
    password: str
    email: str

@dataclass
class AuthRegistrationResult:
    user_id: int
    username: str
    email: str