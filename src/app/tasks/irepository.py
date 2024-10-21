from typing import Protocol


class AbstractRepository(Protocol):
    async def add_one(self):
        ...

    async def get_one(self):
        ...

    async def update_one(self):
        ...

    async def delete_one(self):
        ...

    async def get_all(self):
        ...
