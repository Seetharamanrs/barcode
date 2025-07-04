## Barcode Generator using Streamlit 
This is simple and clean streamlit web app for generating **code39 barcodes**. Users can view barcode and download barcode

### Features 
- Support **code39** barcode format
- Input validation for allowed characters (A–Z, 0–9, and `- . $ / + %` and space)
- Displays barcode as image
- One-click **Download** button
- Clean separation of UI and logic for maintainability

## Why code39?
**code39** is the one of most commonly used barcode format in logistics, inventory management and industrial applications. Additional 
- It support upper case letters and digits
- It's widely supported by barcode scanners and libraries 
- It' prefectly for simple labels, IDs and Product ones 

While Code39 barcodes can be longer than some other formats (like Code128), they are extremely readable and simple to implement — ideal for educational, demo, and general-purpose use cases.

##  Requirements

Install the required packages using `pip`:

```bash
pip install streamlit python-barcode Pillo
```
## Future Improvement
Here are some potential enhancements planned for future versions of this app:

-  **QR Code support** using libraries like `qrcode` or `segno`
-  Support for other barcode formats (e.g., Code128, EAN13, UPC-A)
-  Customization options:
  - Adjustable barcode size and resolution
-  Export formats: download as PDF, SVG, or base64
-  Deploy to **Streamlit Cloud** or Docker for easy sharing

