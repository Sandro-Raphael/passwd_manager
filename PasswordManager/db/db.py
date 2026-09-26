from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base, sessionmaker
from pydantic import BaseModel
from core.config import DATABASE_URL


# Conexão com o PostgreSQL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


# Modelo da tabela no PostgreSQL
class SenhaDB(Base):
    __tablename__ = "senhas"

    id = Column(Integer, primary_key=True, index=True)
    nivel_entropia = Column(String, nullable=False)
    tempo_vida = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    encrypted_senha = Column(LargeBinary, nullable=False)


# Modelo recebido pela API
class Senha(BaseModel):
    id: int
    nivel_entropia: str
    tempo_vida: int
    status: str
    senha: str


# Modelo devolvido pela API
class SenhaOut(BaseModel):
    id: int
    nivel_entropia: str
    tempo_vida: int
    status: str


# Gerenciador do CRUD
class SenhaManager:

    def create(self, senha: Senha, security) -> SenhaOut:
        db = SessionLocal()

        try:
            encrypted_senha = security.encrypt(senha.senha)

            nova_senha = SenhaDB(
                id=senha.id,
                nivel_entropia=senha.nivel_entropia,
                tempo_vida=senha.tempo_vida,
                status=senha.status,
                encrypted_senha=encrypted_senha
            )

            db.add(nova_senha)
            db.commit()
            db.refresh(nova_senha)

            return SenhaOut(
                id=nova_senha.id,
                nivel_entropia=nova_senha.nivel_entropia,
                tempo_vida=nova_senha.tempo_vida,
                status=nova_senha.status
            )

        finally:
            db.close()

    def get_all(self) -> list[SenhaOut]:
        db = SessionLocal()

        try:
            senhas = db.query(SenhaDB).all()

            return [
                SenhaOut(
                    id=senha.id,
                    nivel_entropia=senha.nivel_entropia,
                    tempo_vida=senha.tempo_vida,
                    status=senha.status
                )
                for senha in senhas
            ]

        finally:
            db.close()

    def get_by_id(self, senha_id: int):
        db = SessionLocal()

        try:
            senha = db.query(SenhaDB).filter(
                SenhaDB.id == senha_id
            ).first()

            if senha is None:
                return None

            return SenhaOut(
                id=senha.id,
                nivel_entropia=senha.nivel_entropia,
                tempo_vida=senha.tempo_vida,
                status=senha.status
            )

        finally:
            db.close()

    def update(self, senha_id: int, senha: Senha, security):
        db = SessionLocal()

        try:
            senha_db = db.query(SenhaDB).filter(
                SenhaDB.id == senha_id
            ).first()

            if senha_db is None:
                return None

            senha_db.nivel_entropia = senha.nivel_entropia
            senha_db.tempo_vida = senha.tempo_vida
            senha_db.status = senha.status
            senha_db.encrypted_senha = security.encrypt(senha.senha)

            db.commit()
            db.refresh(senha_db)

            return SenhaOut(
                id=senha_db.id,
                nivel_entropia=senha_db.nivel_entropia,
                tempo_vida=senha_db.tempo_vida,
                status=senha_db.status
            )

        finally:
            db.close()

    def delete(self, senha_id: int) -> bool:
        db = SessionLocal()

        try:
            senha = db.query(SenhaDB).filter(
                SenhaDB.id == senha_id
            ).first()

            if senha is None:
                return False

            db.delete(senha)
            db.commit()

            return True

        finally:
            db.close()

# Base.metadata.create_all(bind=engine)