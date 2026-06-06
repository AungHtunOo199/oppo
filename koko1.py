import os
import sys

def run_logic():
    print("[+] System Logic Running...")
    try:
        # မူလအတွင်းနာမည် starlink အတိုင်း ခေါ်သုံးရပါမယ်
        import starlink 
        
    except ImportError:
        print("[!] Error: starlink.so ကို ရှာမတွေ့ပါ!")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    run_logic()
