from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from config.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    image_path = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)  # ✅ Tambahan kategori langsung string
    is_best_seller = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "imagePath": self.image_path,
            "price": self.price,
            "category": self.category,
            "isBestSeller": self.is_best_seller,
        }
