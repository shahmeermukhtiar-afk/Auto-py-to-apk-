Installation Steps  

1.
    Clone this repository:     

                    git clone https://github.com/shahmeermukhtiar-afk/Auto-py-to-apk-.git

2. Run this command 
                       cd Auto-py-to-apk-    


3.  (Optional) Create a virtual environment and activate it:


                      python3 -m venv venv source venv/bin/activate

3.     Install dependencies (if any). If you have a requirements.txt file, run:             
           
       pip install -r requirements.txt

4.     Run the GUI tool:

                    python apk_builder_gui.py

5.     In the GUI, select your Python project directory, fill in app name, version, and click Convert to APK.

      After build, check the built APK inside the bin/ folder of the project workspace.


   🧩 Project Structure

   Auto-py-to-apk-/
│
├── apk_builder_gui.py
├── README.md
├── requirements.txt
└── (other source files)


  🛠️ Tips & Notes

 On first build, Buildozer may take a long time since it downloads SDK, NDK,

 
If Buildozer command is not found, install it via pip install buildozer and ensure it's in your PATH.

Always use a clean environment to avoid conflicts.

📜 License

MIT
 (or your chosen license)








