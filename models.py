from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    progress = db.relationship("RoadmapProgress", backref="user", lazy=True,
                                cascade="all, delete-orphan")
    results  = db.relationship("QuizResult", backref="user", lazy=True,
                                cascade="all, delete-orphan")

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)


class QuizResult(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    results_json = db.Column(db.Text)   # JSON: [{career_id, pct, title}, ...]
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    def get_results(self):
        return json.loads(self.results_json) if self.results_json else []


class RoadmapProgress(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    career_id  = db.Column(db.String(60), nullable=False)
    node_id    = db.Column(db.String(120), nullable=False)
    status     = db.Column(db.String(20), default="not_started")
    # status values: not_started | in_progress | done
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("user_id", "career_id", "node_id",
                            name="uq_user_career_node"),
    )
