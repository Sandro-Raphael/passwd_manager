from fastapi import APIRouter, HTTPException
from core.config import AES_KEY
from db.db import Senha, SenhaManager, SenhaOut
from core.security import Security


router = APIRouter()

security = Security(AES_KEY)
senha_manager = SenhaManager()


@router.post("/register", response_model=SenhaOut)
def registrar_senha(senha: Senha):
    return senha_manager.create(senha, security)


@router.get("/register", response_model=list[SenhaOut])
def listar_senhas():
    return senha_manager.get_all()


@router.get("/register/{senha_id}", response_model=SenhaOut)
def buscar_senha(senha_id: int):
    senha = senha_manager.get_by_id(senha_id)

    if senha is None:
        raise HTTPException(
            status_code=404,
            detail="Senha não encontrada"
        )

    return senha


@router.put("/register/{senha_id}", response_model=SenhaOut)
def atualizar_senha(senha_id: int, senha: Senha):
    senha_atualizada = senha_manager.update(
        senha_id,
        senha,
        security
    )

    if senha_atualizada is None:
        raise HTTPException(
            status_code=404,
            detail="Senha não encontrada"
        )

    return senha_atualizada


@router.delete("/register/{senha_id}")
def deletar_senha(senha_id: int):
    sucesso = senha_manager.delete(senha_id)

    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Senha não encontrada"
        )

    return {
        "message": "Senha deletada com sucesso!"
    }