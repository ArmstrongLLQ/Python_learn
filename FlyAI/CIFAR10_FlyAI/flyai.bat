
@rem ----- ExeScript Options Begin -----
                                
                           
               
                                      
                                   
                         
@rem ----- ExeScript Options End -----

@echo off

if not exist C:\%HOMEPATH%\.flyai (
   md C:\%HOMEPATH%\.flyai
)

C:\%HOMEPATH%\.flyai\main.exe %*
