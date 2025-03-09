from fastapi import APIRouter, Depends, Query
from services.chroma import ChromaService

router = APIRouter()

@router.get("/search")
async def semantic_search(
    query: str = Query(..., min_length=3),
    limit: int = Query(10, ge=1, le=100)
):
    chroma = ChromaService()
    results = await chroma.search(query, n_results=limit)
    return {
        "results": results
    }