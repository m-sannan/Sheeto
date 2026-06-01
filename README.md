# Sheeto

Sheeto (formerly Local-to-Sheets) is a Python utility to authenticate and sync files to Google Drive.

## 🚀 Download Ready-to-Use Software
Don't want to deal with the hassle of installing Python, managing dependencies, and setting up environments? 
You can download the pre-packaged executable software for Mac and Windows directly from Gumroad:
👉 **[Download Sheeto on Gumroad](https://6014760986164.gumroad.com/l/sheeto)**

## Features
- Google Drive OAuth2 authentication flow.
- Ensures the application only has access to the files it creates (`drive.file` scope).

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/m-sannan/Sheeto.git
   cd Sheeto
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup Google Credentials:
   - Go to Google Cloud Console.
   - Create a project and enable the **Google Drive API**.
   - Create OAuth 2.0 Client IDs and download the JSON file.
   - Save it as `credentials.json` in the root of the project.

4. Run the application:
   ```bash
   python main.py
   ```
   The first time you run this, a browser window will open asking you to authenticate. After authenticating, a `token.json` file will be created automatically.

## Building Executables
You can use PyInstaller to build the app for Windows or Mac:
```bash
pyinstaller --onefile main.py
```
*(You may use the included `.spec` files depending on your needs).*

## Author & Support
**Mohammed Sannan**

If you have any questions, want to suggest improvements, or just want to connect, feel free to reach out to me on LinkedIn!
👉 [Connect with me on LinkedIn](https://www.linkedin.com/in/mohammedsannan/)
