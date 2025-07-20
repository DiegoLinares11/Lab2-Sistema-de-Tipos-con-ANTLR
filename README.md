## Video de demostracion
https://youtu.be/S8u6LBGDFI8 

Para compilar 
### Para el listener 
```python
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -listener program/SimpleLang.g4 -o program
```
### Para el visitor
```python
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor program/SimpleLang.g4 -o program
```
Comandos para correr estos archivos 
### Para el visitor
```python
python program/Driver.py program/program_test_pass.txt
```
```python
python program/Driver.py program/program_test_no_pass.txt
```
Aca como no pasa deberia de decirte algo como:
<img width="1238" height="74" alt="imagen" src="https://github.com/user-attachments/assets/617e74b6-66de-4bb4-8e82-a2ade75ad4c1" />



### Para el listener
```python
python program/DriverListener.py program/program_test_pass.txt
```
```python
python program/DriverListener.py program/program_test_no_pass.txt
```
ACa para este algo como: <img width="1272" height="130" alt="imagen" src="https://github.com/user-attachments/assets/92b23154-a649-441c-8fb9-ba3e4bec4674" />


## Paso de extender la gramática de ANTLR para incluir otras dos operaciones
Asi se ve antes de agregarlas probando el archivo `program/program_test_extra`
<img width="1216" height="173" alt="imagen" src="https://github.com/user-attachments/assets/ade90b46-7fee-44a3-b571-b49542de1cb6" />

Y aca pues ya esta reconociendo las nuevas operaciones
<img width="1199" height="74" alt="imagen" src="https://github.com/user-attachments/assets/479b94b0-b7f5-4339-9bfa-a6f3a2d019bd" />

Lo que se hizo fue modificar el .g4 asi: <img width="575" height="152" alt="imagen" src="https://github.com/user-attachments/assets/d8843fb9-66cc-4002-94fc-ea45042a0b05" />

Por ultimo las validaciones nuevas que cree en el listener y en el visitor
<img width="1281" height="144" alt="imagen" src="https://github.com/user-attachments/assets/908662cd-0c1e-4723-99c9-f690911c5bef" />


