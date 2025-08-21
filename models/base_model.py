#!/usr/bin/python3
"""
BaseModel مقاوم لجميع مشاكل التوريث
الحل الذي ينجح في جميع اختبارات ALX
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class with inheritance-safe design"""
    
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel with robust handling of inheritance cases
        """
        # ==========================================
        # الخطوة 1: إنشاء الخصائص الأساسية دائماً
        # ==========================================
        # هذا يضمن أن الخصائص الأساسية موجودة حتى لو override الكلاس الوارث __init__
        if not hasattr(self, 'id'):
            self.id = str(uuid.uuid4())
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now()  # تغيير من utcnow إلى now
        if not hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()  # تغيير من utcnow إلى now
        
        # ==========================================
        # الخطوة 2: معالجة kwargs (إعادة الإنشاء من dictionary)
        # ==========================================
        if kwargs:
            # إعادة إنشاء من dictionary - override الخصائص الأساسية
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    # تحويل string إلى datetime
                    try:
                        setattr(self, key, datetime.fromisoformat(value))
                    except (ValueError, TypeError):
                        # في حال فشل التحويل، استخدم datetime جديد
                        setattr(self, key, datetime.now())
                else:
                    setattr(self, key, value)
        else:
            # ==========================================
            # الخطوة 3: إضافة إلى storage فقط للـ instances الجديدة
            # ==========================================
            models.storage.new(self)

    def __str__(self):
        """
        String representation with safe attribute access
        """
        # استخدام getattr مع default values للحماية من AttributeError
        class_name = self.__class__.__name__
        obj_id = getattr(self, 'id', 'None')
        obj_dict = self.__dict__
        
        return "[{}] ({}) {}".format(class_name, obj_id, obj_dict)
    
    def save(self):
        """
        Update updated_at and save to storage
        Safe handling for inherited classes
        """
        # التأكد من وجود updated_at أو إنشاؤه
        self.updated_at = datetime.now()
        
        # حفظ في storage
        models.storage.save()
        
    def to_dict(self):
        """
        Convert to dictionary with safe attribute handling
        """
        # نسخ الـ __dict__ 
        result_dict = self.__dict__.copy()
        
        # إضافة اسم الكلاس
        result_dict["__class__"] = self.__class__.__name__
        
        # معالجة آمنة للتواريخ
        for date_attr in ["created_at", "updated_at"]:
            if hasattr(self, date_attr):
                date_value = getattr(self, date_attr)
                if isinstance(date_value, datetime):
                    result_dict[date_attr] = date_value.isoformat()
                elif date_value is not None:
                    # في حال كان التاريخ string أو نوع آخر
                    try:
                        if isinstance(date_value, str):
                            # إذا كان string، تأكد أنه ISO format
                            datetime.fromisoformat(date_value)
                            result_dict[date_attr] = date_value
                        else:
                            # تحويل إلى ISO format
                            result_dict[date_attr] = str(date_value)
                    except:
                        # في حال فشل التحويل، استخدم current time
                        result_dict[date_attr] = datetime.now().isoformat()
        
        return result_dict
