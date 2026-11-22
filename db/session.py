from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker,create_async_engine
from core import get_config

config = get_config()

db_url = config.database_url

engine = create_async_engine(url=db_url,
                             pool_pre_ping=True,
                             echo=False)

sessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False
)

async def get_db():
    async with sessionLocal() as session:
            yield session

async def check_connection():
    from sqlalchemy import text

    async with engine.connect() as conn:
        await conn.execute(
            text("SELECT 1")
        )

    return True

async def close_db():
     await engine.dispose()