from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=500)
    address = models.TextField()

    def __str__(self):
        return str(self.hospital_name)

class DonateItem(models.Model):
    donate_item_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=50)
    show_item = models.BooleanField(default=True)

    def __str__(self):
        return str(self.donate_item_name)

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.job_name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.full_name

class Donate(models.Model):
    SHIPPING = 'Shipping'
    RECEIVED = 'Received'
    CANCEL = 'Cancel'
    DONATE_STATUS = [
        (RECEIVED,'Received'),
        (SHIPPING,'Shipping'),
        (CANCEL,'Cancel')
    ]

    donator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(DonateItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=100, choices=DONATE_STATUS, default=SHIPPING)
    shipping_id = models.CharField(max_length=30, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.donator)

class Receive(models.Model):
    WAITING_FOR_PRODUCTION = 'รอการผลิต'
    PACKING = 'กำลังบรรจุ'
    SHIPPING = 'กำลังจัดส่ง'
    CONFIRM_RECEIVED = 'ยืนยันการรับของ'
    RECEIVE_STATUS = [
        (WAITING_FOR_PRODUCTION,'Waiting for production'),
        (PACKING,'Packing'),
        (SHIPPING,'Shipping'),
        (CONFIRM_RECEIVED,'Confirm received')
    ]

    THAILAND_PROVINCES = (
        ('KBI', 'กระบี่'),
        ('BKK', 'กรุงเทพมหานคร'),
        ('KRI', 'กาญจนบุรี'),
        ('KSN', 'กาฬสินธุ์'),
        ('KPT', 'กำแพงเพชร'),
        ('KKN', 'ขอนแก่น'),
        ('CTI', 'จันทบุรี'),
        ('CCO', 'ฉะเชิงเทรา'),
        ('CBI', 'ขลบุรี'),
        ('CNT', 'ชัยนาท'),
        ('CPM', 'ชัยภูมิ'),
        ('CPN', 'ชุมพร'),
        ('CRI', 'เชียงราย'),
        ('CMI', 'เชียงใหม่'),
        ('TRG', 'ตรัง'),
        ('TRT', 'ตราด'),
        ('TAK', 'ตาก'),
        ('NYK', 'นครนายก'),
        ('NPT', 'นครปฐม'),
        ('NPM', 'นครพนม'),
        ('NMA', 'นครราชสีมา'),
        ('NST', 'นครศรีธรรมราช'),
        ('NSN', 'นครสวรรค์'),
        ('NBI', 'นนทบุรี'),
        ('NWT', 'นราธิวาส'),
        ('NAN', 'น่าน'),
        ('BKN', 'บึงกาฬ'),
        ('BRM', 'บุรีรัมย์'),
        ('PTE', 'ปทุมธานี'),
        ('PKN', 'ประจวบคีรีขันธ์'),
        ('PRI', 'ปราจีนบุรี'),
        ('PTN', 'ปัตตานี'),
        ('PYO', 'พะเยา'),
        ('AYA', 'พระนครศรีอยุธยา'),
        ('PNA', 'พังงา'),
        ('PLG', 'พัทลุง'),
        ('PCT', 'พิจิตร'),
        ('PLK', 'พิษณุโลก'),
        ('PBI', 'เพชรบุรี'),
        ('PNB', 'เพชรบูรณ์'),
        ('PRE', 'แพร่'),
        ('PKT', 'ภูเก็ต'),
        ('NKM', 'มหาสารคาม'),
        ('MDH', 'มุกดาหาร'),
        ('MSN', 'แม่ฮ่องสอน'),
        ('YST', 'ยโสธร'),
        ('YLA', 'ยะลา'),
        ('RET', 'ร้อยเอ็ด'),
        ('RNG', 'ระนอง'),
        ('RYG', 'ระยอง'),
        ('RBR', 'ราชบุรี'),
        ('LRI', 'ลพบุรี'),
        ('LPG', 'ลำปาง'),
        ('LPN', 'ลำพูน'),
        ('LEI', 'เลย'),
        ('SSK', 'ศรีสะเกษ'),
        ('SNK', 'สกลนคร'),
        ('SKA', 'สงขลา'),
        ('STN', 'สตูล'),
        ('SPK', 'สมุทรปราการ'),
        ('SKM', 'สมุทรสงคราม'),
        ('SKN', 'สมุทรสาคร'),
        ('SKW', 'สระแก้ว'),
        ('SRI', 'สระบุรี'),
        ('SBR', 'สิงห์บุรี'),
        ('STI', 'สุโขทัย'),
        ('SPB', 'สุพรรณบุรี'),
        ('SNI', 'สุราษฎร์ธานี'),
        ('SRN', 'สุรินทร์'),
        ('NKI', 'หนองคาย'),
        ('NBP', 'หนองบัวลำภู'),
        ('ATG', 'อ่างทอง'),
        ('ACR', 'อำนาจเจริญ'),
        ('UDN', 'อุดรธานี'),
        ('UTT', 'อุตรดิตถ์'),
        ('UTI', 'อุทัยธานี'),
        ('UBN', 'อุบลราชธานี')
    )

    GRADE = (
        ('A','A'),
        ('B','B'),
    )
    
    ref = models.CharField(max_length=255, null=True, blank=True)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    #use for add data
    full_name = models.CharField(max_length=255, null=True, blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    holding_medical_license_no = models.CharField(max_length=20, null=True, blank=True)
    shipping_id = models.CharField(max_length=30, null=True, blank=True)
    province = models.CharField(max_length=255, choices=THAILAND_PROVINCES, null=True, blank=True)
    grade = models.CharField(max_length=5, choices=GRADE, default='A')
    note = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=RECEIVE_STATUS, default=WAITING_FOR_PRODUCTION)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.receiver)

class Review(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    receive = models.OneToOneField(Receive, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.receive)

class Order(models.Model):
    order_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.order_name)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    receive = models.ForeignKey(Receive, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.order)