from backend.src.common.exceptions import BeException
from backend.src.db.models.users import User

def require_self(target_user_id: int, current_user: User):
    if current_user.id != target_user_id:
        raise BeException("Forbidden", status_code=403)