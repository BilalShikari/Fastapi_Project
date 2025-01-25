from sqlalchemy.orm import Session
from models import User, Watchlist
from schemas import UserCreate, WatchlistCreate, WatchlistUpdate


# User CRUD Operations
def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user by their email.
    """
    return db.query(User).filter(User.email == email).first()


def get_user_by_google_id(db: Session, google_id: str):
    """
    Retrieve a user by their Google OAuth ID.
    """
    return db.query(User).filter(User.google_id == google_id).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.
    """
    db_user = User(email=user.email, name=user.name, google_id=user.google_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Watchlist CRUD Operations
def create_watchlist_entry(db: Session, watchlist: WatchlistCreate, user_id: int):
    """
    Create a new watchlist entry for a specific user.
    """
    db_watchlist = Watchlist(
        user_id=user_id, symbol=watchlist.symbol, list_name=watchlist.list_name
    )
    db.add(db_watchlist)
    db.commit()
    db.refresh(db_watchlist)
    return db_watchlist


def get_watchlist_by_id(db: Session, watchlist_id: int, user_id: int):
    """
    Retrieve a specific watchlist entry by ID for a specific user.
    """
    return db.query(Watchlist).filter(Watchlist.id == watchlist_id, Watchlist.user_id == user_id).first()


def get_watchlists_for_user(db: Session, user_id: int):
    """
    Retrieve all watchlist entries for a specific user.
    """
    return db.query(Watchlist).filter(Watchlist.user_id == user_id).all()


def update_watchlist_entry(db: Session, watchlist_id: int, user_id: int, watchlist: WatchlistUpdate):
    """
    Update a specific watchlist entry for a user.
    """
    db_watchlist = get_watchlist_by_id(db, watchlist_id, user_id)
    if not db_watchlist:
        return None

    if watchlist.symbol:
        db_watchlist.symbol = watchlist.symbol
    if watchlist.list_name:
        db_watchlist.list_name = watchlist.list_name

    db.commit()
    db.refresh(db_watchlist)
    return db_watchlist


def delete_watchlist_entry(db: Session, watchlist_id: int, user_id: int):
    """
    Delete a specific watchlist entry for a user.
    """
    db_watchlist = get_watchlist_by_id(db, watchlist_id, user_id)
    if not db_watchlist:
        return None

    db.delete(db_watchlist)
    db.commit()
    return db_watchlist
