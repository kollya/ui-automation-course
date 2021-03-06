from ctypes import POINTER
from ctypes import c_long
from ctypes import c_uint32
from ctypes import c_void_p

CFIndex = c_long
CFStringEncoding = c_uint32
CFString = c_void_p
CFArray = c_void_p
CFDictionary = c_void_p
CFError = c_void_p
CFType = c_void_p

CFAllocatorRef = c_void_p
CFStringRef = POINTER(CFString)
CFArrayRef = POINTER(CFArray)
CFDictionaryRef = POINTER(CFDictionary)
CFErrorRef = POINTER(CFError)
CFTypeRef = POINTER(CFType)

kCFStringEncodingUTF8 = CFStringEncoding(0x08000100)

kCGWindowListOptionAll = 0
kCGWindowListOptionOnScreenOnly = (1 << 0)

kCGNullWindowID = 0
