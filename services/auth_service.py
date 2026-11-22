from sqlalchemy import select,text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.concurrency import run_in_threadpool

from core import (get_config,Config,
                  hash_password,verify_password,
                  create_access_token)
from db import Organization,User


class AuthenticationError(Exception):
    pass

class RegistrationConflictError(Exception):
    pass

