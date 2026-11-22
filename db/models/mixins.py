from sqlalchemy import DateTime,func
from sqlalchemy.orm import Mapped,mapped_column
from db.base import Base
from sqlalchemy.types import Uuid
import uuid
from datetime import datetime

class UUIDMixins:
    id : Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )

class TimestampMixins:
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

