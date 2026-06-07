from django.db import models


class Certificate(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sertifikat nomi")
    issuer = models.CharField(max_length=200, verbose_name="Bergan tashkilot")
    year = models.CharField(max_length=10, verbose_name="Yil")
    image_url = models.URLField(blank=True, null=True, verbose_name="Rasm URL (imgbb.com dan)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.issuer}"


class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Xabar")
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name="O'qildi")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.name} ({self.email})"
