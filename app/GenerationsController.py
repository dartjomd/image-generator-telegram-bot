from app.database.DB import db


class GenerationsController:
    @staticmethod
    def get_generations() -> list[any]:
        sql_str = """SELECT * FROM generations"""
        return db.read(sql_str)

    @staticmethod
    def get_generation_by_user_id(user_id: int) -> list[any]:
        sql_str = """SELECT * FROM generations WHERE user_id = ? AND is_resolved = 0"""
        res = db.read(sql_str, (user_id,))
        if res:
            return res[0]
        return False

    # @staticmethod
    # def get_generation_by_id(id: int) -> list[any]:
    #     sql_str = """SELECT * FROM generations WHERE id = ?"""
    #     res = db.read(sql_str, (id,))
    #     if res:
    #         return res[0]
    #     return False

    @staticmethod
    def create_generation(user_id: int, image_url: str, prompt: str) -> bool:
        data: tuple[any, ...] = (user_id, image_url, prompt, 0)
        sql_str: str = """
        INSERT INTO generations (user_id, image_url, prompt, is_resolved) 
        VALUES (?, ?, ?, ?)
        """
        return db.create(sql_str, data)

    @staticmethod
    def resolve_generation(u_id: int) -> list[any]:
        sql_str = """UPDATE generations SET is_resolved = 1 WHERE user_id = ?"""
        return db.update(sql_str, (u_id,))

    @staticmethod
    def is_user_allowed_to_generate(u_id: int) -> bool:
        sql_str = (
            """SELECT user_id FROM generations WHERE user_id = ? AND is_resolved = 0"""
        )
        res = db.read(sql_str, (u_id,))
        return 0 if len(res) else 1

    @staticmethod
    def get_user_total_generations(u_id: int) -> int | bool:
        sql_str = """SELECT COUNT(*) FROM generations WHERE user_id = ?"""
        res = db.read(sql_str, (u_id,))
        if res:
            return res[0][0]
        return False
