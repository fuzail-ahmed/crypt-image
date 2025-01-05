
# 🔒 **CryptImage**  

A lightweight, self-hosted Python Flask application for secure image uploads with advanced protection against AI exploitation, deepfakes, and metadata leaks.

---

## 🚀 **Features**  

- ✅ **Metadata Stripping:** Removes all sensitive image metadata (EXIF).  
- ✅ **Watermarking:** Adds an invisible watermark (e.g., unique hash or timestamp).  
- ✅ **Encryption:** AES encryption for enhanced image security.  
- ✅ **One-time Download:** Images are auto-deleted after download.  
- ✅ **No Authentication Required:** Open for all users without login.  
- ✅ **Self-Hosted:** Run it locally with ease.  

---

## 🛠️ **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/fuzail-ahmed/crypt-image.git
cd crypt-image
```

### **2. Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Server**
```bash
python backend/app.py
```

### **5. Access the Application**
Open your browser and navigate to:  
[http://localhost:5000](http://localhost:5000)

---

## 📖 **Usage Guide**

1. **Upload:** Drag and drop or select your image file.  
2. **Secure Processing:** The image will undergo metadata stripping, watermarking, and encryption.  
3. **Download:** Securely download your image.  
4. **Auto Clean-up:** Image is deleted after download.

---

## 🛡️ **Security Measures**

- Images are processed entirely in memory (no long-term storage).  
- Auto-deletion after download.  
- AES encryption for sensitive image data.  
- Metadata and EXIF data removal.

---

## 🧪 **Run Tests**
To ensure everything is working as expected:
```bash
pytest tests/
```

---

## 🤝 **Contributing**
Pull requests are welcome! For significant changes, please open an issue first to discuss what you'd like to change.

---

## 📜 **License**
This project is licensed under the **MIT License**. See the LICENSE file for more details.

---

## 📬 **Support**
For support or inquiries, please contact:  
📧 **fuzail1280@gmail.com**