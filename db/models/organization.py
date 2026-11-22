from sqlalchemy import (String,Integer,DateTime,Boolean,
                        UniqueConstraint,CheckConstraint,Index,ForeignKey,
                        )
from sqlalchemy.orm import Mapped,mapped_column,relationship
from db.base import Base
from db.models.mixins import UUIDMixins,TimestampMixins
from sqlalchemy.types import Uuid
import uuid

class Organization(Base,UUIDMixins,TimestampMixins):
    __tablename__ = "organizations"

    name : Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=False
    )
    slug : Mapped[str] = mapped_column(
        String(),
        nullable=True,
        unique=False
    )
    is_active : Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    users : Mapped[list["User"]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan",
    )


class User(Base,UUIDMixins,TimestampMixins):
    __tablename__="users"

    __table_args__ = (
        CheckConstraint(
            "role IN ('owner', 'admin', 'member')",
            name="valid_role",
        ),
        UniqueConstraint(
            "organization_id",
            "email",
            name="uq_users_organization_email",
        ),
        Index("ix_users_organization_id", "organization_id"),
    )

    organization_id : Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey(
            "organizations.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    email : Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )
    password_hash : Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    full_name : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    role : Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    is_active : Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )
    organization : Mapped["Organization"] = relationship(
        back_populates="users"
    )
