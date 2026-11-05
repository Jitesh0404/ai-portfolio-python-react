from ai_portfolio.services import user_services


def get_all_users():
    return user_services.get_all_user_db()
