from sqlalchemy import select,text
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (create_async_engine,
                                    AsyncSession,
                                    async_sessionmaker
)

from core import get_config

config = get_config()

load_dotenv()

db_url = config.database_url
engine = create_async_engine(db_url,pool_pre_ping=True,echo=False)

sessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def ping_connection() -> bool:
    """Check database connectivity."""
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            value = result.scalar_one()

            assert value == 1

    except Exception:
        return False
        

