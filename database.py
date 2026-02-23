from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://USER:PASSWORD@HOST/DATABASE"

engine = create_engine(psql 'postgresql://neondb_owner:npg_T9g3eFcNDYsz@ep-ancient-grass-a9phk972-pooler.gwc.azure.neon.tech/neondb?sslmode=require&channel_binding=require')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
