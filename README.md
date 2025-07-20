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
### Para el listener
```python
python program/DriverListener.py program/program_test_pass.txt
```
```python
python program/DriverListener.py program/program_test_no_pass.txt
```
