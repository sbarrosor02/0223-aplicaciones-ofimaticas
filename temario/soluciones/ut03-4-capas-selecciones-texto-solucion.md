# Criterios de corrección · UT3.4 Capas, selecciones y texto

No se publica en la web del alumnado. Las prácticas de este subtema no tienen
una única solución: aquí está lo que hay que comprobar al abrir el `.xcf`.

## P3.4.1 · Recortar un objeto

- Diálogo Capas: el objeto tiene **máscara de capa** (miniatura blanca y negra
  junto a la de la capa). Si lo recortaron con la goma, no hay máscara: no cumple.
- Sin restos de la sombra original ni halo del fondo (ampliar al 200 % en el
  borde). En la guitarra, el fallo típico es la sombra inferior derecha; en el
  mando, el borde entre las empuñaduras.
- Borde suave (difuminado de 1–2 px), no dentado.
- Fondo: la textura en su propia capa. Sombra nueva con Sombra arrojada (capa o
  efecto aparte), coherente con la luz.
- Explicación: nombra al menos dos herramientas y para qué usó cada una.

## P3.4.2 · Modos de fusión

- Tres capturas con modos distintos y una explicación correcta: Multiplicar
  oscurece y el blanco desaparece; Pantalla aclara y el negro desaparece;
  Superponer da contraste y tiñe.
- Capas con nombre; el paisaje no está modificado (la textura y el degradado
  van en capas separadas).

## P3.4.3 · Fundido con máscara

- La transición está en la **máscara** (degradado), no en la opacidad global
  ni borrando. Al desactivar la máscara (Ctrl+clic en su miniatura en GIMP 2.10
  o desde el menú contextual) la capa aparece entera.

## P3.4.4 · Miniatura con texto

- Imagen de 1280 × 720.
- Capas de texto editables (o una copia editable si aplicó efectos).
- Como mucho dos tipografías; título legible en la captura al 25 %; nada
  importante en la esquina inferior derecha.

## Errores frecuentes

| Síntoma | Causa |
|---|---|
| «No me deja pintar» o «no hace nada» | Selección olvidada (Seleccionar > Ninguno) o capa sin canal alfa |
| Se mueve la capa que no es | Herramienta Mover sin «Mover la capa activa» |
| Aparece «Selección flotante» y todo se bloquea | Pegó con Ctrl+V; Capa > A capa nueva |
| Pinta negro en la foto | Estaba activa la capa y no la máscara |
| El texto ya no se puede editar | Le aplicó un filtro o pintó encima |
