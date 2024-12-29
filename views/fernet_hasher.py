import string
import secrets
import hashlib
import base64
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_letters + string.digits
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'keys'

    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode('utf-8')
        self.fernet = Fernet(key)

    @classmethod
    def _get_random_string(cls, length=25):
        return ''.join(secrets.choice(cls.RANDOM_STRING_CHARS) for _ in range(length))

    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string()
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        key = base64.urlsafe_b64encode(hasher[:32])
        if archive:
            return key, cls.archive_key(key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        cls.KEY_DIR.mkdir(parents=True, exist_ok=True)
        file = 'key.key'
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(length=5)}.key'
        with open(cls.KEY_DIR / file, 'wb') as f:
            f.write(key)
        return cls.KEY_DIR / file

    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        return self.fernet.encrypt(value).decode('utf-8')

    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken:
            return 'Token inválido'
