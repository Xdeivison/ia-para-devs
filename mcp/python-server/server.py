"""Servidor MCP didático.

A API do SDK pode evoluir. O exemplo acompanha a linha 2.x descrita no livro;
confira a documentação oficial do SDK antes de usar em produção.
"""
from pathlib import Path
from mcp.server import MCPServer

mcp = MCPServer("ia-para-devs-toolbox")
PROJECT_ROOT = Path.cwd().resolve()


def _safe_path(relative: str) -> Path:
    target = (PROJECT_ROOT / relative).resolve()
    if PROJECT_ROOT not in target.parents and target != PROJECT_ROOT:
        raise ValueError("caminho fora do projeto")
    return target


@mcp.tool()
def read_text_file(path: str) -> str:
    """Lê um arquivo UTF-8 dentro do diretório do projeto."""
    target = _safe_path(path)
    return target.read_text(encoding="utf-8")


@mcp.tool()
def list_project_files(limit: int = 100) -> list[str]:
    """Lista arquivos do projeto sem atravessar diretórios externos."""
    files = [str(p.relative_to(PROJECT_ROOT)) for p in PROJECT_ROOT.rglob("*") if p.is_file()]
    return files[: max(1, min(limit, 500))]


@mcp.resource("project://standards")
def standards() -> str:
    return "Mudanças pequenas; testes antes da entrega; nunca exponha segredos."


@mcp.prompt()
def review_prompt() -> str:
    return "Revise o diff priorizando correção, segurança, regressões e testes ausentes."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
