import os
import sys

def run_logic():
    print("[+] System Logic Running...")
    try:
        # yuta.so (starlink.so) ကို ခေါ်သုံးခြင်း
        import yuta
        
        # အကယ်၍ yuta.so ထဲမှာ သီးသန့် function တစ်ခုခု ခေါ်ရမယ်ဆိုရင် 
        # ဒီအောက်မှာ ထည့်ပေးရပါမယ်။ 
        # ဥပမာ - yuta.menu() သို့မဟုတ် yuta.start()
        
    except ImportError:
        print("[!] Error: yuta.so (starlink.so) ကို ရှာမတွေ့ပါ!")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    run_logic()
