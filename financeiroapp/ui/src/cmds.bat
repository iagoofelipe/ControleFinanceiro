REM Geral
pyside6-uic financeiroapp\ui\src\MainWindow.ui -o financeiroapp\ui\auto\ui_MainWindow.py
pyside6-rcc financeiroapp\ui\src\resource.qrc -o financeiroapp\ui\auto\resource_rc.py

REM Components
pyside6-uic financeiroapp\ui\src\table.ui -o financeiroapp\ui\auto\ui_table.py

REM Pages
pyside6-uic financeiroapp\ui\src\RegistryPage.ui -o financeiroapp\ui\auto\ui_RegistryPage.py
pyside6-uic financeiroapp\ui\src\LoginPage.ui -o financeiroapp\ui\auto\ui_LoginPage.py