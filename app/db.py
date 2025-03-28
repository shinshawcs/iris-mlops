from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# 你可以用 PostgreSQL，例如：
#DATABASE_URL = "postgresql://postgres:1027@localhost:5432/iris_db"
# 原来可能是这样
# DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"

# 改成这样
#DATABASE_URL = "postgresql://user:password@host.docker.internal:5432/iris_db"
#DATABASE_URL = "sqlite:///./test.db"  # 本地测试用 SQLite 更简单，稍后可以换成 PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()