# 🏦 Proyecto Sistema Bancario en Consola

## 👨‍💻 Autor
- **Nombre:** Samuel Mantilla Pallares  

---

## 📝 Descripción
Este proyecto es un **sistema bancario en consola**, desarrollado en Python, que permite la gestión de cuentas bancarias y créditos.  
Entre sus funcionalidades principales están:  
- Crear cuentas bancarias con información completa del cliente.  
- Eliminar cuentas existentes.  
- Realizar depósitos y retiros.  
- Solicitar y pagar créditos.  
- Guardar y cargar la información en un archivo JSON para persistencia de datos.  
- Limpieza automática de la consola para mejorar la experiencia de usuario.  

---

## ⚙️ Stack Tecnológico
- **Lenguaje:** Python 3.10+  
- **Persistencia:** JSON (para almacenar datos de cuentas y créditos).  
- **Sistema Operativo:** Compatible con Linux, Windows y macOS (ejecución en terminal).  

---

## 📌 Requerimientos
- Python 3.10 o superior  
- Acceso a terminal (cmd, PowerShell, bash, zsh, etc.)  
- Permisos de escritura en el directorio `data/`  

---

## 🚀 Ejecución del Proyecto

### 🔹 En Linux / macOS
```bash
cd Ejercicios
python3 main.py
```

### 🔹 En Windows
```powershell
cd Ejercicios
python main.py
```

---

## 📂 Estructura de Archivos

```
Ejercicios/
│── main.py               # Punto de entrada del programa
│
├── modules/              # Módulos principales
│   ├── menu.py           # Controla la interfaz del menú
│   ├── logic.py          # Lógica de operaciones (cuentas, créditos, etc.)
│   ├── corefiles.py      # Manejo de archivos JSON (guardar/cargar)
│   └── utilities.py      # Utilidades (limpieza de consola, helpers)
│
├── data/                 # Carpeta de persistencia
│   └── data.json         # Archivo donde se almacenan las cuentas
│
└── README.md             # Documentación del proyecto
```

---

## 📚 Librerías Externas
El proyecto **no requiere librerías externas**.  
Solo usa librerías estándar de Python:  
- `os` → manejo del sistema (limpieza de consola).  
- `json` → guardar y cargar datos.  
- `random` → generación de números de cuenta únicos.  

---

## 📤 Archivo
- Los datos de cuentas y créditos se almacenan en:  
  ```
  data/data.json
  ```

---

## 🤝 Colaboración
Para agregar o invitar al **trainer** al repositorio, usar la opción:  
👉 **Settings > Collaborators > Add people**  
y buscar el usuario:  
```
trainingLeader
```
