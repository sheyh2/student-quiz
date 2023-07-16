from src.database.__init__ import db


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=False)
    is_active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.String(255), nullable=False)

    @classmethod
    def get_instance(cls):
        return cls()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def isActive(self):
        return self.is_active

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

