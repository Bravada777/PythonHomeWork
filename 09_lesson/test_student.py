from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pytest

Base = declarative_base()


class Student(Base):
    __tablename__ = 'group_student'

    user_id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False)


engine = create_engine('postgresql://postgres:147@localhost:5432/QA')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db_session():
    session = SessionLocal()
    yield session
    session.close()


def test_add_student(db_session):
    new_student = Student(user_id=1, group_id=1)
    db_session.add(new_student)
    db_session.commit()

    retrieved_student = db_session.query(Student).filter_by(user_id=1).first()
    assert retrieved_student is not None
    assert retrieved_student.user_id == 1
    assert retrieved_student.group_id == 1


def test_update_student(db_session):
    new_student = Student(user_id=2, group_id=2)
    db_session.add(new_student)
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(user_id=2).first()
    updated_student.group_id = 3
    db_session.commit()

    retrieved_student = db_session.query(Student).filter_by(user_id=2).first()
    assert retrieved_student is not None
    assert retrieved_student.user_id == 2
    assert retrieved_student.group_id == 3


def test_delete_student(db_session):
    new_student = Student(user_id=3, group_id=3)
    db_session.add(new_student)
    db_session.commit()

    student_to_delete = db_session.query(Student).filter_by(user_id=3).first()
    db_session.delete(student_to_delete)
    db_session.commit()

    retrieved_student = db_session.query(Student).filter_by(user_id=3).first()
    assert retrieved_student is None
