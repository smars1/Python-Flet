# Class StateButton()

## Flet no detecta cambios, self.update() no está reconstruyendo el UserControl.
## Causas del problema
Esto ocurre si Flet no detecta un cambio en un atributo que lo obligue a volver a llamar a build().
self.bgcolor cambia, pero Flet puede no estarlo registrando correctamente.

### El botón no está almacenado dentro del UserControl.

Flet solo reconstruye el widget si detecta cambios en un componente dentro de build().
Para asegurarnos de que Flet reconstruya el botón, debemos:

Guardar self.button en self.controls dentro de build().
Modificar self.controls dentro de on_click_handler().
Forzar la actualización de self.controls usando self.update()

```py
 def on_click_handler(self, e):
        """
        Evento que cambia de color al botón al hacer clic.
        """
        self.clicked = not self.clicked  # Alternamos entre True y False
        print(f"Presionando botón. Estado actual: {self.clicked}")  # ✅ Confirmamos que el evento se ejecuta

        # ✅ Cambiamos la variable del estado
        self.bgcolor = ft.colors.GREEN_500 if self.clicked else ft.colors.BLUE_500
        print(f"Cambiando color a: {self.bgcolor}")  # 🔍 Debugging

        # ✅ Actualizamos el botón dentro de `self.controls`
        self.controls.clear()  # Eliminamos el botón antiguo
        self.controls.append(self.build())  # Agregamos el botón actualizado
        self.update()  # ✅ Esto forzará que `build()` se ejecute nuevamente y actualice el botón
```

# 📌 Explicación de las correcciones
✅ 1. Se usa ``self.controls.clear()`` y ``self.controls.append(self.build())``
```py
self.controls.clear()  
self.controls.append(self.build())  
```

- Razón: Flet solo detecta cambios si modificamos la lista self.controls.
- Ahora el botón anterior se borra y se reemplaza con uno nuevo con el color actualizado.
- por ultimo se llama a ``self.update()`` para actualizar la UI, lo que obliga a Flet a redibujar el UserControl y mostrar el cambio de color.


## ¿Por qué esta solución funciona y las anteriores no?
Antes: self.update() no estaba forzando la reconstrucción del botón.
Ahora: self.controls.clear() y self.controls.append(self.build()) hacen que Flet detecte el cambio y lo redibuje.
🔹 Con esta solución, el botón se reconstruye correctamente y el color cambia en tiempo real. 🚀🔥

# 🔹 ¿Cómo funciona Flet?
Flet usa un sistema de "reactividad", lo que significa que cuando un control cambia, se tiene que reconstruir para reflejar el cambio en la interfaz.
UserControl en Flet tiene un método llamado update(), que obliga a Flet a redibujar el control con sus nuevos valores.
- 🔹 El problema:
Cuando cambiábamos self.bgcolor, Flet no redibujaba el botón porque la interfaz no sabía que algo había cambiado dentro del UserControl.

🔹-  La solución:
Para que Flet detecte el cambio, necesitamos borrar el botón anterior y reemplazarlo con uno nuevo dentro de self.controls.