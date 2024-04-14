import sqlite3
import aiosqlite


class Database():
    def __init__(self, path):
        self.path = path
        
    async def tabll(self):
        async with aiosqlite.connect(self.path) as conn:
            cur = await conn.cursor()
            await cur.execute("""CREATE TABLE IF NOT EXISTS users_info(
                        id INTEGER PRIMARY KEY,
                        ID_TG INTEGER,
                        NAME TEXT,
                        USERNAME TEXT,
                        NICKNAME TEXT,
                        PASSWORD TEXT,
                        STATE_PASS INTEGER,
                        DATE_REG TEXT
            )""")
            await conn.commit()

    async def getCursor(self):
        conn = await aiosqlite.connect(self.path)
        cur = await conn.cursor()
        return conn, cur

    async def checkIdUser(self, id_tg):
        conn, cur = await self.getCursor()
        rows = await cur.execute("SELECT * FROM users_info WHERE ID_TG=?", (id_tg,))
        rows = await rows.fetchall()
        await cur.close()
        await conn.close()
        if len(rows) > 0:
            return True
        else:
            return False
    
    async def createNewUser(self, id_tg, name, username, nickname, password, state_pass = 0, date_reg = None):
        conn, cur = await self.getCursor()
        await cur.execute("""INSERT INTO users_info
                          (ID_TG, NAME, USERNAME, NICKNAME, PASSWORD, STATE_PASS, DATE_REG) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)""",
                           (id_tg, name, username, nickname, password, state_pass, date_reg))
        await conn.commit()
        await cur.close()
        await conn.close()

    async def ifNewUser(self, nickname):
        conn, cur = await self.getCursor()
        rows = await cur.execute("SELECT * FROM users_info WHERE NICKNAME=?", (nickname,))
        rows = await rows.fetchall()
        await cur.close()
        await conn.close()
        return len(rows) > 0