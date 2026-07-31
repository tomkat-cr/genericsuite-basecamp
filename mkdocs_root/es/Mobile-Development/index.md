# GenericSuite Móvil (Flutter)

[GenericSuite Móvil](https://github.com/tomkat-cr/genericsuite-mobile) trae
el patrón CRUD impulsado por JSON de GenericSuite a las apps Flutter: define tus
entidades en archivos de configuración JSON y monta el widget `CrudEditor` — no
se necesita código Dart por entidad para CRUD estándar.

Layout del repositorio:

- `genericsuite_flutter/` — la biblioteca Flutter reutilizable (consumida como una dependencia Git).

## Instalación

Agrega la biblioteca al `pubspec.yaml` de tu aplicación:

```yaml
dependencies:
  genericsuite:
    git:
      url: https://github.com/tomkat-cr/genericsuite-mobile.git
      path: genericsuite_flutter
      ref: main
```

## Arranque de la aplicación

Crea una subclase de `AppCallablesSuper` para inyectar el comportamiento de tu aplicación, luego inicia la app con `CreateGsApp`:

```dart
void main() {
  runApp(CreateGsApp(appCallables: AppCallables()));
}
```

`CreateGsApp` construye la raíz del árbol de widgets con `ShadApp`
([shadcn_ui](https://pub.dev/packages/shadcn_ui), la versión Flutter de ShadCN) y deriva el tema de `MaterialApp` a partir de los tokens de tema de GenericSuite (ver [Theming](#theming)).

## CRUD impulsado por JSON

Los archivos de configuración viven bajo `assets/`:

- `assets/config/stage.json` — selecciona el entorno (`dev`, `qa`,
  `staging`, `prod`).
- `assets/config/config-{stage}.json` — URL base de la API y otros valores.
- `assets/config_dbdef/backend/*.json` — endpoints REST y definiciones de esquemas.
- `assets/config_dbdef/frontend/*.json` — tipos de campos, etiquetas, distribución de formularios.

Monta un editor:

```dart
CrudEditor(
  jsonFileName: 'users.json',
  callbacks: callbacks,
  props: props,
)
```

## Componentes hijos (relaciones 1-N)

El Editor CRUD de Flutter maneja `childComponents` de la misma manera que el editor CRUD de genericsuite-fe (React): la configuración JSON del frontend de una entidad padre lista los nombres de los componentes hijos, y cada uno se renderiza dentro del formulario de edición del padre.

Configuración del padre (`assets/config_dbdef/frontend/users.json`):

```json
{
    "childComponents": [
        "UsersFoodTimes"
    ]
}
```

En móvil, cada hijo aparece como una sección pulsable en la parte inferior del formulario de edición del padre (nunca durante la creación). Al pulsar, se abre el editor del hijo a pantalla completa pasando la fila padre como `parentData`.

Registra un builder para cada nombre en el mapa `callbacks['childComponents']`:

```dart
Map<String, dynamic> callbacks = {
  "childComponents": {
    "UsersFoodTimes": ({
      required Map<String, dynamic> parentData,
      Map<String, dynamic>? props,
    }) =>
        CrudEditor(
          jsonFileName: 'users_food_times.json',
          callbacks: AppCallables().getUserCallbacks(context),
          props: {...?props, 'parentData': parentData},
        ),
  },
};
```

La configuración JSON del hijo declara la relación:

```json
{
    "type": "child_listing",
    "subType": "array",
    "array_name": "food_times",
    "endpointKeyNames": [
        {"parameterName": "user_id", "parentElementName": "_id"}
    ]
}
```

- `subType: "array"` — las filas hijo viven dentro de un atributo de tipo arreglo de la fila padre (`array_name` obligatorio). Las escrituras envían `{parentKey, <array_name>: newValues, <array_name>_old: initialValues}`.
- `subType: "table"` — las filas hijo viven en su propia tabla; la clave del padre se fusiona en cada fila hijo.

## Theming

El lenguaje de diseño es limpio al estilo Apple: superficies blancas/neutras, texto casi negro, un color de acento (predeterminado `Colors.green`), radio de esquinas de 12 px y colores semánticos del sistema iOS.

Sobre escribe `getThemeParams()` en tu `AppCallables` para personalizarlo — devuelve solo las claves que quieras cambiar; se fusionan sobre los valores predeterminados de la biblioteca (`defaultThemeParams` en `theme_config_defaults.dart`):

| Token | Predeterminado | Propósito |
| --- | --- | --- |
| `accentColor` | `Colors.green` | El único color de acento |
| `borderRadius` | `12.0` | Radio de esquinas (px) para entradas, botones, tarjetas |
| `fontFamily` | `'Inter'` | Tipografía; `'Inter'` se carga vía google_fonts (similar a SF-Pro) |
| `textTheme` | `null` | Sobrescritura opcional completa de `TextTheme` |
| `textColor` | `#111111` | Text principal casi negro |
| `secondaryTextColor` | `#6E6E73` | Etiqueta secundaria de iOS |
| `separatorColor` | `#D1D1D6` | Separador de iOS (bordes, divisores) |
| `neutralSurfaceColor` | `#F2F2F7` | Superficie neutral del sistema iOS (systemGray6) |
| `scaffoldBackgroundColor` | `Colors.white` | Fondo de la pantalla |
| `appBarBackgroundColor` / `appBarForegroundColor` | blanco / casi negro | Superficies de la barra de la aplicación |
| `errorBackgroundColor` | `#FF3B30` (systemRed) | Mensajes de error |
| `infoBackgroundColor` | `#007AFF` (systemBlue) | Mensajes informativos |
| `warningBackgroundColor` | `#FF9500` (systemOrange) | Advertencias |
| `successBackgroundColor` | `#34C759` (systemGreen) | Mensajes de éxito |

Ejemplo:

```dart
class AppCallables extends AppCallablesSuper {
  @override
  Map<String, dynamic> getThemeParams() {
    return {
      'accentColor': Colors.indigo,
      'fontFamily': 'Inter',
    };
  }
}
```

## Más información

- README de la biblioteca:
  [genericsuite_flutter](https://github.com/tomkat-cr/genericsuite-mobile/tree/main/genericsuite_flutter)
- Plantilla de inicio:
  [flutter_project_template](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp)