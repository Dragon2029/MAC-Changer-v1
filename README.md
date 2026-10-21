# MAC Changer 🔄

أداة بسيطة بلغة Python لتغيير عنوان MAC (Media Access Control) على أنظمة لينكس — متوافقة مع Kali Linux ومعظم التوزيعات.

---

## 📋 الوصف

**MAC Changer** أداة سطر أوامر تعتمد على `ifconfig` لتغيير عنوان MAC الخاص بأي واجهة شبكة. مفيدة في اختبارات الاختراق الأخلاقي واختبارات الشبكات وإخفاء الهوية.

---

## ✨ المميزات

- 🔧 تغيير عنوان MAC لأي واجهة شبكة (wlan0, eth0, ...)
- 📊 عرض عنوان MAC الحالي قبل وبعد التغيير
- ✅ التحقق من نجاح العملية تلقائياً
- ⚠️ معالجة الأخطاء (واجهة غير موجودة / عنوان غير صالح)
- 🐧 متوافق مع Kali Linux, Ubuntu, Debian, Arch, Fedora, Parrot OS

---

## 📦 المتطلبات

- Python 3.6+
- أداة `ifconfig` (من حزمة `net-tools`)
- صلاحيات **root**

### تثبيت المتطلبات

**Debian / Ubuntu / Kali:**
```bash
sudo apt update
sudo apt install python3 net-tools