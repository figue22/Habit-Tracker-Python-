# 🧠 Habit Tracker - Aplicación de Consola en Python

Aplicación interactiva en consola para gestionar y analizar hábitos semanales.

Permite crear hábitos, registrar días completados, calcular progreso y generar estadísticas generales de cumplimiento.

---

## 🚀 Características

- ✅ Crear nuevos hábitos con meta semanal
- 🔁 Marcar días como completados o no completados
- 📊 Calcular progreso en días y porcentaje
- 🏆 Mostrar hábito con mayor cumplimiento
- 📈 Calcular promedio general de cumplimiento
- ❌ Eliminar hábitos
- 🛡 Validación de entradas del usuario

---

## 🛠 Tecnologías y conceptos utilizados

Este proyecto fue desarrollado utilizando:

- Python 3
- Diccionarios anidados
- Listas y valores booleanos
- Funciones y modularización
- Parámetros y valores de retorno
- Bucles `while` y `for`
- Validación centralizada
- Funciones auxiliares (`max` con `key`)
- Cálculo de estadísticas
- Control de flujo estructurado

---

## 🧠 Estructura del proyecto

El programa está organizado bajo un enfoque modular:

- `menu_principal()` → Controla la navegación del usuario
- `crear_habito()` → Permite agregar nuevos hábitos
- `marcar_dia()` → Alterna el estado de un día
- `calcular_progreso()` → Calcula días cumplidos y porcentaje
- `estadisticas()` → Muestra métricas generales
- `validar_campo()` → Centraliza validaciones
- Funciones auxiliares para cálculos específicos

Se utiliza el patrón:

```python
if __name__ == "__main__":
    menu_principal(habitos)

Para definir el punto de entrada del programa.

▶️ Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/tu-usuario/habit-tracker-python.git


Entrar al directorio:

cd habit-tracker-python


Ejecutar el archivo principal:

python main.py