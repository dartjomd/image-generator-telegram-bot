from app.database.DB import db
import time


class UsersController:
    @staticmethod
    def user_exists(id: int) -> list[any]:
        sql_str = """SELECT * FROM users WHERE user_id = ? """
        return db.read(sql_str, (id,))

    @staticmethod
    def create_user(id: int) -> bool:
        timestamp: int = int(time.time())
        data: tuple[any, ...] = (id, timestamp)
        sql_str: str = """
        INSERT INTO users (user_id, join_date) 
        VALUES (?, ?)
        """
        return db.create(sql_str, data)

    @staticmethod
    def get_all_users() -> list[any]:
        sql_str = """SELECT * FROM users"""
        return db.read(sql_str)

    @staticmethod
    def get_all_extended_users() -> list[any]:
        sql_str = """SELECT
            u.user_id,
            u.is_generating,
            COUNT(g.user_id) AS total,
            -- Используем SUM(CASE ...) для подсчета всех ЗАБЛОКИРОВАННЫХ генераций (is_resolved = 0)
            -- Если сумма равна 0, значит, нет заблокированных генераций.
            CASE 
                WHEN SUM(CASE WHEN g.is_resolved = 0 THEN 1 ELSE 0 END) = 0 THEN 1
                ELSE 0
            END AS all_generations_resolved
            FROM
                users u
            LEFT JOIN
                generations g ON u.user_id = g.user_id
            GROUP BY
                u.user_id
            ORDER BY
                total DESC;"""
        return db.read(sql_str)

    @staticmethod
    def is_user_generating(user_id: int) -> bool:
        sql_str = "SELECT is_generating FROM users WHERE user_id = ?"
        res = db.read(sql_str, (user_id,))
        if res:
            return res[0][0]
        return 0

    @staticmethod
    def change_user_generating(user_id: int, is_generating: bool) -> bool:
        sql_str = "UPDATE users SET is_generating = ? WHERE user_id = ?"
        return db.update(
            sql_str,
            (
                is_generating,
                user_id,
            ),
        )
