#-*- coding: utf-8 -*-
import msvcrt

def pwd_input():    
    chars = []   
    while True:  
        try:  
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:  
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")  
        if newChar in '\r\n': 
             break   
        elif newChar == '\b': 
             if chars:    
                 del chars[-1]   
                 msvcrt.putch('\b'.encode(encoding='utf-8')) 
                 msvcrt.putch( ' '.encode(encoding='utf-8'))
                 msvcrt.putch('\b'.encode(encoding='utf-8'))             
        else:  
            chars.append(newChar)  
            msvcrt.putch('*'.encode(encoding='utf-8'))
    return (''.join(chars) )  
