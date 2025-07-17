from dotenv import load_dotenv
import os

load_dotenv()

DRIVER_ = os.getenv("DRIVER")
SERVER_ = os.getenv("SERVER")
DATABASE_ = os.getenv("DATABASE")
UID_ = os.getenv("UID")
PWD_ = os.getenv("PWD")