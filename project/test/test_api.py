import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_interaction_fail(test_app, interaction_payload):
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        response = await ac.post("/interactions/", json=interaction_payload)
        assert response.status_code == 404

@pytest.mark.asyncio
async def test_create_interaction_success(test_app, interaction_payload, init_data):
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        response = await ac.post("/interactions/", json=interaction_payload)
        
        interaction = response.json()
        type(response)
        assert response.status_code == 200
        assert interaction["diagnosis"] == interaction_payload["diagnosis"]
        assert interaction["treatment"] == interaction_payload["treatment"]
        assert interaction["outcome"]  == interaction_payload["outcome"]
        assert interaction["id"] == 1