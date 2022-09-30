from django.db import models
from .paystack import PayStack
import secrets

# Create your models here.

class Payment(models.Model):
    
    fullname = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        ordering = ('-date',)
        
    def __str__(self):
        return f"payment: {self.amount}"
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs) 
        
    def amount_value(self) -> int:
        return self.amount *100       
        
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False
                     