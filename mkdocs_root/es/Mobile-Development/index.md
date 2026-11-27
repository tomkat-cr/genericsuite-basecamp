# GenericSuite Mobile (Flutter)

<img 
    align="right"
    width="100"
    height="100"
    src="https://genericsuite.carlosjramirez.com/images/gs_logo_circle.svg"
    title="Logotipo de GenericSuite, de Carlos J. Ramirez"
/>

[GenericSuite Mobile](https://github.com/tomkat-cr/genericsuite-mobile) lleva el patrón CRUD de GenericSuite basado en JSON a las aplicaciones Flutter: define tus entidades en archivos de configuración JSON y añade el widget `CrudEditor` —no se necesita código Dart por entidad para las operaciones CRUD estándar—. También puedes aprovechar la interfaz de inicio de sesión personalizable, el generador de menús y un conjunto de herramientas para agilizar el desarrollo de aplicaciones móviles con Flutter/Dart.

## Características

- **Editor CRUD personalizable:** código CRUD básico (*Create, Read, Update, Delete*) que se puede parametrizar y ampliar mediante archivos de configuración JSON. No es necesario reescribir el código para cada editor de tablas.
- **Menú personalizable:** el menú y los endpoints se pueden parametrizar y ampliar mediante archivos de configuración JSON en el Backend. La API proporciona la estructura del menú y realiza la comprobación de seguridad según el grupo de seguridad del usuario; GenericSuite dibuja el menú y las opciones disponibles.
- **Pantalla de inicio de sesión personalizable:** adapta fácilmente la pantalla de inicio de sesión a la identidad de tu marca con el logotipo de la aplicación.
- **Scripts de desarrollo y producción:** comandos rápidos para iniciar el desarrollo o compilar la aplicación para entornos de QA, staging o producción en los principales proveedores de nube.
- **Widgets personalizables:** un conjunto de widgets que se pueden parametrizar y ampliar mediante archivos de configuración JSON.
- **Flutter/Dart:** GenericSuite está desarrollado con Flutter/Dart, por lo que es compatible con Android y iOS.

El complemento perfecto para esta solución móvil es la [versión Backend de The GenericSuite](https://genericsuite.carlosjramirez.com/Backend-Development/GenericSuite-Core/).

## Primeros pasos

### Requisitos previos

- [Flutter SDK](https://docs.flutter.dev/install)
- [Android Studio](https://developer.android.com/studio) (para administrar Android SDK, emuladores, etc.)
- [Xcode](https://developer.apple.com/xcode/) (para administrar iOS SDK, emuladores, etc.)
- [Paquete móvil de GenericSuite](https://github.com/tomkat-cr/genericsuite-mobile)
- [Paquete Backend de GenericSuite](https://github.com/tomkat-cr/genericsuite-be)
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- [Make](https://formulae.brew.sh/formula/make) (Mac) | Linux incluye Make de forma predeterminada | [Make](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows) (Windows)

#### ¿No tienes un proyecto Flutter?

Crea un proyecto Flutter con el comando `flutter create`:

```bash
flutter create exampleapp
```

### Instalación

- Añade el paquete genericsuite:

```bash
flutter pub add genericsuite
```

O hazlo manualmente:

1. Abre el archivo `pubspec.yaml` y añade GenericSuite a la sección `dependencies:`:

```yaml
  genericsuite:
    git:
      url: https://github.com/tomkat-cr/genericsuite-mobile
      ref: main  # or develop
      path: genericsuite_flutter
```

2. Instala las dependencias.

```bash
flutter pub get
```

## Uso

### Ejemplos de uso

En los siguientes ejemplos crearemos una aplicación sencilla con una página de inicio, una página de perfil de usuario y otras funcionalidades.

### Configuración

- Consulta la [Guía de creación y configuración de aplicaciones](https://genericsuite.carlosjramirez.com/Configuration-Guide/) para obtener más información sobre cómo crear los archivos de configuración JSON.

- Consulta la [Guía del Backend](https://genericsuite.carlosjramirez.com/Backend-Development/GenericSuite-Core) para obtener más información sobre cómo crear la API.

### Estructura del directorio de la aplicación

La siguiente estructura de directorios sirve como referencia para tu aplicación. Encontrarás más información sobre la estructura de directorios en la [Guía de creación y configuración de aplicaciones](https://genericsuite.carlosjramirez.com/Configuration-Guide/).

```
.
├── android
├── assets
|   ├── config
|   │   ├── config-dev.json
|   │   ├── config-env.example.json
|   │   ├── config-prod.json
|   │   ├── config-qa.json
|   │   ├── stage-dev.json
|   │   ├── stage-prod.json
|   │   ├── stage-qa.json
|   │   └── stage.json
|   ├── config_dbdef
|   │   ├── backend
|   │   │   ├── app_main_menu.json
|   │   │   ├── endpoints.json
|   │   │   ├── general_config.json
|   │   │   ├── onboarding_admin.json
|   │   │   ├── onboarding_users.json
|   │   │   ├── users_api_keys.json
|   │   │   ├── users_config.json
|   │   │   ├── users_profile.json
|   │   │   ├── users.json
|   │   │   └── exampleapp_any_other_table.json
|   │   ├── CHANGELOG.md
|   │   ├── frontend
|   │   │   ├── app_constants.json
|   │   │   ├── general_config.json
|   │   │   ├── general_constants.json
|   │   │   ├── onboarding_admin.json
|   │   │   ├── onboarding_users.json
|   │   │   ├── users_api_keys.json
|   │   │   ├── users_config.json
|   │   │   ├── users_profile.json
|   │   │   ├── users.json
|   │   │   └── exampleapp_any_other_table.json
|   │   └── README.md
|   └── images
|       ├── app_logo_circle.png
|       ├── app_logo_emblem.png
|       └── app_logo_horizontal.png
├── build
├── ios
├── lib
|   ├── config
|   │   └── theme_config.dart
|   ├── domain
|   │   ├── app_menu_callables.dart
|   │   ├── exampleapp_crud_editor_sf_users.dart
|   │   └── exampleapp_utilities.dart
|   ├── main.dart
|   ├── views
|   │   ├── about.dart
|   │   ├── exampleapp_any_other_crud_editor_view.dart
|   │   └── user_profile.dart
|   └── widgets
|       ├── homepage_body.dart
|       └── exampleapp_any_other_widget.dart
├── test
├── web
└── windows
```

### Inicio de la aplicación

#### lib/main.dart

El archivo `main.dart` es el punto de entrada de la aplicación. En nuestros ejemplos, creamos el widget `ExampleApp`, una subclase de `StatelessWidget` que construye el árbol de widgets de la aplicación.

La clase `AppCallables` inyecta el comportamiento de la aplicación y la configuración del tema en el framework GenericSuite. `CreateGsApp` construye la raíz del árbol de widgets con `ShadApp` ([shadcn_ui](https://pub.dev/packages/shadcn_ui), la adaptación de ShadCN para Flutter) y deriva el tema de `MaterialApp` de los tokens del tema de GenericSuite (consulta [Tematización](#tematización)).

```dart
import 'package:flutter/material.dart';
import 'package:genericsuite/services/create_gs_app.dart';

import "domain/app_menu_callables.dart";

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(ExampleApp());
}

class ExampleApp extends StatelessWidget {
  const ExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    return CreateGsApp(appCallables: AppCallables());
  }
}
```

#### lib/domain/app_menu_callables.dart

Este archivo define las funciones del menú de la aplicación (funciones que se ejecutan al seleccionar un elemento del menú, widgets especificados en los archivos de configuración JSON, etc.), la información de la aplicación, los elementos de la pantalla principal y las funciones de retorno relacionadas con la gestión de usuarios.

```dart
import 'package:flutter/material.dart';
import 'package:genericsuite/services/app_callables_super.dart';
import 'package:genericsuite/services/logout_service.dart';
import 'package:genericsuite/services/utilities.dart';
import 'package:genericsuite/views/homepage.dart';

import '../config/theme_config.dart';
import '../domain/exampleapp_crud_editor_sf_users.dart';
import '../views/about.dart';
import '../views/user_profile.dart';

import '../domain/exampleapp_utilities.dart';

// "exampleapp_any_other_crud_editor_view.dart" contiene el widget ExampleappAnyOtherCrudEditorView,
// que también es una vista alternativa para el widget HomepageBody
import '../views/exampleapp_any_other_crud_editor_view.dart';

// "homepage_body.dart" contiene el widget HomepageBody, que es la vista principal de la aplicación
import '../widgets/homepage_body.dart';

import '../widgets/exampleapp_any_other_widget.dart';

const debug = false;

class AppCallables extends AppCallablesSuper {
  /*
   * Get the theme parameters
   */
  @override
  Map<String, dynamic> getThemeParams() {
    return {
      'accentColor': accentColor,
      'accentForegroundColor': accentForegroundColor,
      'borderRadius': borderRadius,
      'fieldVerticalSpacing': fieldVerticalSpacing,
      'fontFamily': gsFontFamily,
      'textTheme': null, // TextTheme? — app-provided full text theme
      'textColor': textColor,
      'secondaryTextColor': secondaryTextColor,
      'separatorColor': separatorColor,
      'neutralSurfaceColor': neutralSurfaceColor,
      'primarySwatch': primarySwatch,
      'scaffoldBackgroundColor': scaffoldBackgroundColor,
      'appBarBackgroundColor': appBarBackgroundColor,
      'appBarForegroundColor': appBarForegroundColor,
      'drawerBackgroundColor': drawerBackgroundColor,
      'drawerForegroundColor': drawerForegroundColor,
      'drawerBarBackgroundColor': drawerBarBackgroundColor,
      'drawerBarForegroundColor': drawerBarForegroundColor,
      'errorBackgroundColor': errorBackgroundColor,
      'errorForegroundColor': errorForegroundColor,
      'infoBackgroundColor': infoBackgroundColor,
      'infoForegroundColor': infoForegroundColor,
      'warningBackgroundColor': warningBackgroundColor,
      'warningForegroundColor': warningForegroundColor,
      'successBackgroundColor': successBackgroundColor,
      'successForegroundColor': successForegroundColor,
      'closeButtonPlacement': closeButtonPlacement,
      'shadColorSchemeName': shadColorSchemeName,
      'drawerHeaderLogoPath': drawerHeaderLogoPath,
      'drawerHeaderLogoHeight': drawerHeaderLogoHeight,
      'drawerHeaderLogoWidth': drawerHeaderLogoWidth,
      'drawerHeaderText': drawerHeaderText,
      'drawerHeaderTextFontSize': drawerHeaderTextFontSize,
      'drawerHeaderTextFontWeight': drawerHeaderTextFontWeight,
      'appBarLogoPath': appBarLogoPath,
      'appBarLogoHeight': appBarLogoHeight,
      'appBarLogoWidth': appBarLogoWidth,
      'appBarTitleText': appBarTitleText,
      'appBarTitleTextFontSize': appBarTitleTextFontSize,
      'appBarTitleTextFontWeight': appBarTitleTextFontWeight,
    };
  }

  /*
   * Get the menu callables and other options
   */
  @override
  Map<String, dynamic> getMenuCallables() {
    if (debug) {
      logDebug('AppCallables | getMenuCallables');
    }
    return {
      "HomePage": {
        "widget": () =>
            HomePage(homePageBodyBuilder: (userData) => HomePageBody(userData)),
        "icon": Icons.dashboard,
        "args": {}
      },
      "ExampleappAnyOtherCrudEditorView_EditorData": {
        "widget": () => ExampleappAnyOtherCrudEditorView(),
        "icon": Icons.restaurant_menu,
        "args": {}
      },
      "UserProfileEditor": {
        "widget": () => UserProfile(),
        "icon": Icons.person,
        "args": {}
      },
      "BillingEditor": {"widget": null, "icon": Icons.payment, "args": {}},
      "|about|": {"widget": () => About(), "icon": Icons.info, "args": {}},
      "logout": {
        "function": (context) => logOut(context),
        "icon": Icons.logout,
        "args": {}
      },
    };
  }

  /*
   * Get the app info
   */
  @override
  Map<String, dynamic> getAppInfo() {
    return {
      "version": "1.0.0",
      "name": appName,
      "description": "Nutrition in your pocket",
      "appEmail": "support@fynapp.com",
      "appPhone": "+57 316 320-1208",
      "appWebsite": "https://fynapp.com",
      "author": "Carlos J. Ramirez / Mediabros",
      "authorEmail": "contact@mediabros.com",
      "authorPhone": "+57 316 320-1208",
      "authorWebsite": "https://mediabros.com",
    };
  }

  /*
   * Get the main screen elements
   */
  @override
  Map<String, dynamic> getMainScreenElements() {
    return {
      "mainScreen": (userData) => HomePageBody(userData),
      "alternateScreen": () => Dishes(),
      "redirect": false, // or true to redirect to alternate screen
      "icon": Icons.dashboard,
      "args": {},
    };
  }

  /*
   * Get the user management related callbacks
   */
  @override
  Map<String, dynamic> getUserCallbacks(
      BuildContext context, dynamic userData) {
    bool isSuperUser = userData != null &&
        userData is Map &&
        userData.containsKey('isSuperUser') &&
        userData['isSuperUser'] == true;
    return {
      'specificFunctions': {
        'UsersDbPostWrite': (dynamic data,
                Map<String, dynamic> editorConfig,
                String action,
                Map<String, dynamic> params,
                BuildContext? context) async =>
            usersDbPostWrite(data, editorConfig, action, params, context),
      },
      "components": {
        'UserTotalQtyAndCondition': ({
          dynamic data,
          required Map<String, dynamic> config,
          required String value,
          required Function onChanged,
          required String action,
          Map<String, dynamic>? props,
        }) =>
            UserTotalQtyAndCondition(
              config: config,
              value: value,
              onChanged: onChanged,
              action: action,
              context: context,
              props: props,
            ),
        'UserMinimumDailyQty': ({
          dynamic data,
          required Map<String, dynamic> config,
          required String value,
          required Function onChanged,
          required String action,
          Map<String, dynamic>? props,
        }) =>
            userMinimumDailyQty(
              config: config,
              value: value,
              onChanged: onChanged,
              action: action,
              context: context,
              props: props,
            ),
      },
      "childComponents": {
        "UsersUserHistory": ({
          required Map<String, dynamic> parentData,
          Map<String, dynamic>? props,
        }) =>
            CrudEditor(
              jsonFileName: isSuperUser
                  ? 'users_user_history_admin.json'
                  : 'users_user_history.json',
              callbacks: {},
              props: {...?props, 'parentData': parentData},
            ),
        "UsersConfig": ({
          required Map<String, dynamic> parentData,
          Map<String, dynamic>? props,
        }) =>
            CrudEditor(
              jsonFileName:
                  isSuperUser ? 'users_config_admin.json' : 'users_config.json',
              callbacks: {},
              props: {...?props, 'parentData': parentData},
            ),
        "UsersApiKey": ({
          required Map<String, dynamic> parentData,
          Map<String, dynamic>? props,
        }) =>
            CrudEditor(
              jsonFileName: isSuperUser
                  ? 'users_api_keys_admin.json'
                  : 'users_api_keys.json',
              callbacks: {},
              props: {...?props, 'parentData': parentData},
            ),
      }
    };
  }
}
```

## Tematización

El lenguaje visual tiene una estética limpia al estilo Apple: superficies blancas o neutras, texto casi negro, un color de acento (por defecto `Colors.green`), un radio de esquina de 12 px y colores semánticos del sistema iOS.

Sobrescribe `getThemeParams()` en tu `AppCallables` para personalizar el tema. Devuelve solo las claves que quieras cambiar; se combinarán con los valores predeterminados de la biblioteca (`defaultThemeParams` en `theme_config_defaults.dart`):

| Token | Predeterminado | Propósito |
| --- | --- | --- |
| `accentColor` | `Colors.green` | El único color de acento |
| `borderRadius` | `12.0` | Radio de esquina (px) para campos de entrada, botones y tarjetas |
| `fontFamily` | `'Inter'` | Tipografía; `'Inter'` se carga mediante google_fonts (similar a SF-Pro) |
| `textTheme` | `null` | Anulación opcional de todo el `TextTheme` |
| `textColor` | `#111111` | Color principal del texto, casi negro |
| `secondaryTextColor` | `#6E6E73` | Etiqueta secundaria de iOS |
| `separatorColor` | `#D1D1D6` | Separador de iOS (bordes, divisores) |
| `neutralSurfaceColor` | `#F2F2F7` | Superficie neutra systemGray6 de iOS |
| `scaffoldBackgroundColor` | `Colors.white` | Fondo de pantalla |
| `appBarBackgroundColor` / `appBarForegroundColor` | blanco / casi negro | Superficies de la barra de la aplicación |
| `errorBackgroundColor` | `#FF3B30` (systemRed) | Mensajes de error |
| `infoBackgroundColor` | `#007AFF` (systemBlue) | Mensajes informativos |
| `warningBackgroundColor` | `#FF9500` (systemOrange) | Advertencias |
| `successBackgroundColor` | `#34C759` (systemGreen) | Mensajes de éxito |
| `listingRowEvenBackgroundColor` | `Color(0xFFE5E7EB)` (gray-200) | Fondo de las filas pares (índices 0, 2, 4, ...) |
| `listingRowOddBackgroundColor` | `Colors.transparent` | Fondo de las filas impares |
| `listingRowEvenTextColor` | `textColor` | Color del texto del título en las filas pares |
| `listingRowOddTextColor` | `textColor` | Color del texto del título en las filas impares |
| `listingRowSubtitleColor` | `secondaryTextColor` | Color del texto del subtítulo (línea 2) |
| `listingColumnSeparator` | `' · '` | Texto entre los valores de columna de una misma línea |

Las claves de la pantalla de listado se describen en [Pantalla de listado](#pantalla-de-listado).

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

#### lib/config/theme_config.dart

Este archivo define el tema de la aplicación (colores, estilos, etc.).

```dart
import 'package:flutter/material.dart';

const String appName = "ExampleApp";

const MaterialColor accentColor = Colors.green;
const Color accentForegroundColor = Colors.white;

const double borderRadius = 12.0;

// Defines the border line's weight of Material inputDecorationTheme
// border and enabledBorder, and dividerTheme thickness
const double separatorWidth = 0.50;

// Vertical gap between stacked form fields so outlined focus rings do not
// overlap the previous field's border / floating label.
const double fieldVerticalSpacing = 12.0;

// Named shadcn_ui base scheme for buildGsShadTheme(). Valid values match
// ShadColorScheme.fromName: blue, gray, green, neutral, orange, red, rose,
// slate, stone, violet, yellow, zinc. Apps override via getThemeParams().
const String shadColorSchemeName = 'green';

// Typography tokens. 'Inter' triggers GoogleFonts.interTextTheme() in
// CreateGsApp; any other family name is applied verbatim. An app can also
// provide a full TextTheme via the 'textTheme' theme param (null = derive
// from fontFamily).
const String gsFontFamily = 'Inter';

const Color textColor = Color(0xFF111111); // near-black
const Color secondaryTextColor = Color(0xFF6E6E73); // iOS secondary label

const Color separatorColor = Color(0xFFD1D1D6); // iOS separator
const Color neutralSurfaceColor = Color(0xFFF2F2F7); // iOS systemGray6

// Legacy token, superseded by accentColor. Kept because existing apps
// reference it in their getThemeParams() overrides.
const MaterialColor primarySwatch = accentColor;
const Color scaffoldBackgroundColor = Colors.white;

const Color appBarBackgroundColor = accentColor; // Colors.white;
const Color appBarForegroundColor = accentForegroundColor; // textColor;

const Color drawerBarBackgroundColor = appBarBackgroundColor;
const Color drawerBarForegroundColor = appBarForegroundColor;

const Color drawerBackgroundColor = scaffoldBackgroundColor; // Colors.white;
const Color drawerForegroundColor = textColor;

// iOS system semantic colors
const Color errorBackgroundColor = Color(0xFFFF3B30); // systemRed
const Color errorForegroundColor = Colors.white;

const Color infoBackgroundColor = Color(0xFF007AFF); // systemBlue
const Color infoForegroundColor = Colors.white;

const Color warningBackgroundColor = Color(0xFFFF9500); // systemOrange
const Color warningForegroundColor = Colors.white;

const Color successBackgroundColor = Color(0xFF34C759); // systemGreen
const Color successForegroundColor = Colors.white;

const String closeButtonPlacement = "bottom"; // "bottom" or "right"

const String appBarLogoPath = 
   'assets/images/app_logo_horizontal.png'; // If left empty, the appName
                                            // will be displayed in the app bar
const double appBarLogoHeight = 32.0;
const double appBarLogoWidth = 128.0;

const String appBarTitleText = appName;
const double appBarTitleTextFontSize = 20.0;
const FontWeight appBarTitleTextFontWeight = FontWeight.bold;

const String drawerHeaderLogoPath =
    'assets/images/app_logo_horizontal.png'; // 'assets/images/app_logo_circle.png';
const double drawerHeaderLogoHeight = 250.0;
const double drawerHeaderLogoWidth = 250.0;

const String drawerHeaderText = appName;
const double drawerHeaderTextFontSize = 20.0;
const FontWeight drawerHeaderTextFontWeight = FontWeight.bold;
```

### Código de compatibilidad con CRUD

#### lib/domain/exampleapp_crud_editor_sf_users.dart

Este archivo contiene las «funciones específicas» que se ejecutan cuando se crea o actualiza un usuario en la base de datos.

* *Las funciones específicas* son funciones invocables que amplían las capacidades del editor CRUD genérico (widget `CrudEditor`).

```dart
import 'package:flutter/material.dart';

import 'package:genericsuite/services/crud_editor_commons.dart';
import 'package:genericsuite/services/http_service.dart';
import 'package:genericsuite/services/utilities.dart';
import 'package:genericsuite/views/login.dart';

const debug = false;

Future<Map<String, dynamic>> usersDbPostWrite(
  dynamic data,
  Map<String, dynamic> editorConfig,
  String action,
  Map<String, dynamic> params,
  BuildContext? context,
) async {
  Map<String, dynamic> result = genericFuncArrayDefaultValue(data);
  if (context == null || context.mounted == false) return result;
  String parentId = data[editorConfig['primaryKeyName']];
  switch (action) {
    case actionCreate:
    case actionUpdate:
      final HttpUtilities api = HttpUtilities(storage);
      final Map<String, dynamic> itemToSave = {
        "user_id": parentId,
        "user_history": {
          "date": nowToTimestamp(),
          // Other data that can be change every time the user item is updated
          "goal_code": data['goal_code'],
          "minimun_daily_qty": data['minimun_daily_qty'],
        }
      };
      final apiResp =
          await api.httpsCall('post', 'users_user_history', {}, itemToSave, {});
      if (debug) {
        logDebug(
            "UsersDbPostWrite - itemToSave: $itemToSave | apiResp: $apiResp");
      }
      if (apiResp['error'] == false) {
        // To refresh parent component and show the new minimun_daily_qty value
        result['otherData']['refresh'] = true;
        if (debug) {
          logDebug("UsersDbPostWrite | result: $result");
        }
      } else {
        result['error'] = true;
        result['error_message'] = apiResp['error_message'];
        result['status_code'] = apiResp['status_code'];
        result['resultset'] = apiResp['resultset'];
      }
      break;
    default:
      break;
  }
  return result;
}

Future<Map<String, dynamic>> usersOnboardingDbPostWrite(
  dynamic data,
  Map<String, dynamic> editorConfig,
  String action,
  Map<String, dynamic> params,
  BuildContext? context,
) async {
  Map<String, dynamic> result = genericFuncArrayDefaultValue(data);
  if (context == null || context.mounted == false) return result;
  String userId = data[editorConfig['primaryKeyName']];
  switch (action) {
    case actionCreate:
    case actionUpdate:
      final HttpUtilities api = HttpUtilities(storage);
      final Map<String, dynamic> body = {
        "user_id": userId,
      };
      final apiResp =
          await api.httpsCall('post', 'onboarding_admin', {}, body, {});
      if (debug) {
        logDebug(
            "UsersOnboardingDbPostWrite - body: $body | apiResp: $apiResp");
      }
      if (apiResp['error'] == false) {
        result['onboardingMessage'] =
            "User registration completed successfully. Please check your Email for a confirmation email.";
      } else {
        result['errorMessage'] = apiResp['error_message'];
        result['errorCode'] = 'UOBPW-E010';
        result['apiStatusCode'] = apiResp['status_code'];
      }
      break;
    default:
      break;
  }

  Navigator.push(
    (context?.mounted == false ? null : context)!,
    MaterialPageRoute(builder: (context) => LoginPage(params: result)),
  );

  return result;
}
```

### lib/views/about.dart

Este archivo define un `StatelessWidget` que muestra una página sencilla «Acerca de» con un título y una descripción.

```dart
import 'package:flutter/material.dart';
import 'package:genericsuite/widgets/app_frame.dart';

class About extends StatefulWidget {
  const About({super.key});

  @override
  AboutState createState() => AboutState();
}

class AboutState extends State<About> {
  @override
  Widget build(BuildContext context) {
    return AppFrame(
      body: ListView(
        padding: const EdgeInsets.only(
          top: 10.0,
          left: 20.00,
          right: 20.00,
        ),
        children: const <Widget>[
          Text(
              'ExampleApp is a mobile app that uses GenericSuite to create a CRUD app.'),
          Text(""),
          Text(
              'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
        ],
      ),
    );
  }
}
```

### lib/views/exampleapp_any_other_crud_editor_view.dart

Este archivo contiene un editor CRUD (implementado con el widget `CrudEditor` de GenericSuite) que se usa para mostrar los datos de una tabla de la base de datos.

La tabla utilizada es [exampleapp_any_other](#assetsconfig_dbdeffrontendexampleapp_any_other_tablejson).

```dart
import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import 'package:genericsuite/services/crud_editor.dart';
import 'package:genericsuite/services/locator_service.dart';

import '../domain/app_menu_callables.dart';

class ExampleappAnyOtherCrudEditorView extends StatefulWidget {
  const ExampleappAnyOtherCrudEditorView({super.key});

  @override
  ExampleappAnyOtherCrudEditorViewState createState() => ExampleappAnyOtherCrudEditorViewState();
}

class ExampleappAnyOtherCrudEditorViewState extends State<ExampleappAnyOtherCrudEditorView> {
  @override
  Widget build(BuildContext context) {
    final storage = storageLocator<FlutterSecureStorage>();
    Map<String, dynamic> callbacks = {
      'specificFunctions': {
        'ExampleappAnyOtherValidations': (dynamic data,
                Map<String, dynamic> editorConfig,
                String action,
                Map<String, dynamic> params,
                BuildContext? context) async =>
            exampleappAnyOtherValidations(
                data, editorConfig, action, params, storage, context),
      },
      "childComponents": {
        "ExampleappAnyOtherChildComponent": ({
          required Map<String, dynamic> parentData,
          Map<String, dynamic>? props,
        }) =>
            CrudEditor(
              jsonFileName: 'exampleapp_any_other_child_table.json',
              callbacks: AppCallables().getUserCallbacks(context),
              props: {...?props, 'parentData': parentData},
            ),
      }
    };
    Map<String, dynamic> props = {};
    return CrudEditor(
      jsonFileName: 'exampleapp_any_other_table.json',
      callbacks: callbacks,
      props: props,
    );
  }
}
```

### lib/views/user_profile.dart

```dart
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import 'package:genericsuite/services/app_callables_super.dart';
import 'package:genericsuite/services/crud_editor.dart';
import 'package:genericsuite/services/http_service.dart';
import 'package:genericsuite/services/locator_service.dart';
import 'package:genericsuite/services/utilities.dart';

const debug = true;

class UserProfile extends StatefulWidget {
  const UserProfile({super.key});

  @override
  UserProfileState createState() => UserProfileState();
}

class UserProfileState extends State<UserProfile> {
  final FlutterSecureStorage storage = storageLocator<FlutterSecureStorage>();
  String itemId = '';
  Map<String, dynamic> userData = {};
  AppCallablesSuper appCallables = appCallablesLocator<AppCallablesSuper>();

  Future<Map<String, dynamic>> loadUserData() {
    return storage.read(key: 'user_data').then((userDataValue) {
      Map<String, dynamic> userDataResponse = {};
      if (userDataValue == null || userDataValue.isEmpty) {
        userDataResponse = {
          'errorMessage': "User data could not be loaded",
          'errorCode': "UP-E010",
        };
        return Future.value(userDataResponse);
      } else {
        userDataResponse = Map<String, dynamic>.from(
          json.decode(userDataValue),
        );
      }
      return Future.value(userDataResponse);
    });
  }

  @override
  void initState() {
    super.initState();
    loadConfig().then((configStr) {
      Map<String, dynamic> config =
          Map<String, dynamic>.from(json.decode(configStr));
      loadUserData().then((data) {
        userData = data;
      });
      if (debug) {
        logDebug('UserProfile | initState | itemId: $itemId');
        logDebug('UserProfile | initState | userData: $userData');
      }
      setState(() {
        itemId = config["userId"];
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    if (itemId.isEmpty) {
      return Container();
    }
    if (userData.containsKey('errorMessage') &&
        userData['errorMessage'] != null &&
        userData['errorMessage'].isNotEmpty) {
      logDebug(
          'UserProfile / build / errorMessage: ${userData['errorMessage']}');
      return Dialog(
        child: Column(
          children: [
            Text('${userData['errorMessage']} [${userData['errorCode']}]'),
            TextButton(
                onPressed: () => Navigator.pop(context), child: Text('OK')),
          ],
        ),
      );
    }
    Map<String, dynamic> callbacks =
        appCallables.getUserCallbacks(context, userData);
    Map<String, dynamic> props = {
      'isEditMode': true,
      'itemId': itemId,
    };
    if (debug) {
      logDebug('UserProfile | build | props: $props');
    }
    return CrudEditor(
      jsonFileName: 'users_profile.json',
      callbacks: callbacks,
      props: props,
      backButtonAction: () {
        if (debug) {
          logDebug('UserProfile | backButtonAction');
        }
        return appCallables.mainScreenWidget();
      },
    );
  }
}
```

### lib/widgets/homepage_body.dart

Este archivo contiene el widget HomePageBody, que se utiliza para mostrar la página de inicio de la aplicación.

```dart
import 'package:flutter/material.dart';
import 'package:genericsuite/services/message_service.dart';
import 'package:genericsuite/services/select_options_service.dart';
import 'package:genericsuite/services/utilities.dart';

const debug = false;

class HomePageBody extends StatefulWidget {
  final Map<String, dynamic> userData;

  const HomePageBody(this.userData, {super.key});

  @override
  State<HomePageBody> createState() => _HomePageBodyState();
}

class _HomePageBodyState extends State<HomePageBody> {
  String errorMessage = '';
  String errorCode = '';
  String infoMessage = '';
  Map<String, dynamic> constants = {};

  @override
  void initState() {
    super.initState();
  }

  Future<Map<String, dynamic>> loadHomeConfig() async {
    return getAllConstants().then((constantsMap) {
      return constantsMap;
    }).catchError((error) {
      throw error;
    });
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  void didUpdateWidget(covariant HomePageBody oldWidget) {
    super.didUpdateWidget(oldWidget);
    scheduleMessagesBindings(context, {
      'errorMessage': errorMessage,
      'errorCode': errorCode,
      'infoMessage': infoMessage,
    });
  }

  String setErrorMessage(dynamic error) {
    errorMessage = error.toString();
    return "";
  }

  Widget bodyBuilder(Map<String, dynamic> data) {
    constants = data['constants'];
    if (debug) {
      logDebug("HomePageBody - constants: ${constants.toString()}");
    }
    return ListView(
      padding: const EdgeInsets.only(
        top: 10.0,
        left: 20.00,
        right: 20.00,
      ),
      children: <Widget>[
        Text("Hi ${widget.userData['firstname']}\n"),
        Text("Birthdate: ${widget.userData['birthday']}"),
        const Divider(),
        debug ? Text(widget.userData.toString()) : Container()
      ],
    );
  }

  Widget buildHomePage(BuildContext context) {
    return Center(
      child: FutureBuilder(
          future: loadHomeConfig(),
          builder: (context, snapshot) => snapshot.hasData &&
                  errorMessage.isEmpty
              ? bodyBuilder({"constants": snapshot.data})
              : snapshot.hasError || errorMessage.isNotEmpty
                  ? snapshot.hasError
                      ? Text(setErrorMessage(snapshot.error.toString()))
                      : Text(setErrorMessage("Error loading Home config data"))
                  : const Center(child: CircularProgressIndicator())),
    );
  }

  @override
  Widget build(BuildContext context) {
    return buildHomePage(context);
  }
}
```

### lib/domain/exampleapp_utilities.dart

Este archivo contiene funciones de utilidad de ejemplo que utiliza ExampleApp.

```dart
import 'package:genericsuite/services/convertion_utilities.dart';
import 'package:genericsuite/services/timestamp_utilities.dart';
import 'package:genericsuite/services/utilities.dart';

const String anyConstant = "Condition:";

class DailyConditionResult {
  final bool deficitCondition;
  final String conditionMessage;

  DailyConditionResult({
    required this.deficitCondition,
    required this.conditionMessage,
  });
}

DailyConditionResult getDailyCondition(
    double? minimunDaily, double? totalToday) {

  final bool deficitCondition =
      (minimunDaily ?? 0) > (totalToday ?? 0);
  final String conditionDescription = (deficitCondition ? 'Deficit' : 'Surplus');
  final String conditionMessage =
      (totalToday == null ? '' : '$anyConstant $conditionDescription');

  final result = DailyConditionResult(
    deficitCondition: deficitCondition,
    conditionMessage: conditionMessage,
  );
  return result;
}

int getAge(DateTime today, DateTime dob) {
    final year = today.year - dob.year;
    final mth = today.month - dob.month;
    final days = today.day - dob.day;
    if(mth < 0){
      // negative month means it's still upcoming
      return year-1;
    }
    else {
      return year;
    }
  }

class MinimumDailyQuantityResult {
  final double value;

  MinimumDailyQuantityResult({
    required this.value,
  });
}

MinimumDailyQuantityResult getMinimumDailyQuantity(
  String dateOfBirth,
  String gender,
  String goalCode,
) {
  final age = getAge(DateTime.now(), DateTime.parse(dateOfBirth));
  final result = MinimumDailyQuantityResult(
    // This is a hypothetical calculation based on age, gender, and goal code
    value: (goalCode == 'goal_code_1' ? 100 : 200) * (gender == 'male' ? 1 : 0.5) * age,
  );
  return result;
}

```

### lib/widgets/exampleapp_any_other_widget.dart

```dart
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:genericsuite/services/locator_service.dart';
import 'package:genericsuite/services/utilities.dart';

import '../domain/exampleapp_utilities.dart';

const bool debug = false;

class DailyCondition extends StatelessWidget {
  final double minimumDailyQty;
  final double totalQty;
  final String className;
  final String showAsField;

  const DailyCondition({
    Key? key,
    required this.minimumDailyQty,
    required this.totalQty,
    this.className = '',
    this.showAsField = '0',
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final dailyCondition =
        getDailyCondition(minimumDailyQty, totalQty);
    final output = Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          dailyCondition.conditionMessage,
          style: TextStyle(
            color: dailyCondition.deficitCondition ? Colors.green : Colors.red,
            fontWeight: FontWeight.bold,
          ),
        ),
        const SizedBox(width: 8),
        Text(totalQty.toStringAsFixed(2)),
      ],
    );

    if (showAsField == '1') {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 8.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Daily Condition',
                style: TextStyle(fontSize: 12, color: Colors.grey)),
            output,
          ],
        ),
      );
    }
    return output;
  }
}

class MinimumDailyQty extends StatelessWidget {
  final Map<String, dynamic> data;
  final String className;
  final String name;
  final String id;
  final String type;
  final bool required;
  final bool readOnly;
  final bool disabled;
  final String showAsField;
  final Function(String, String)? onChanged;

  const MinimumDailyQty({
    Key? key,
    required this.data,
    this.className = '',
    this.name = '',
    this.id = '',
    this.type = 'text',
    this.required = false,
    this.readOnly = true,
    this.disabled = false,
    this.showAsField = '1',
    this.onChanged,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final weight = (data['weight'] as num?)?.toDouble() ?? 0.0;
    final height = (data['height'] as num?)?.toDouble() ?? 0.0;
    final dateOfBirth = data['dateOfBirth']?.toString() ?? '';
    final gender = data['gender']?.toString() ?? '';
    final exerciseDays = (data['exerciseDays'] as num?)?.toInt() ?? 0;
    final goalCode = data['goal_code']?.toString();

    final minimumDailyQty = getMinimumDailyQuantity(
      dateOfBirth,
      gender,
      goalCode,
    );

    final newValue = minimumDailyQty.value.toStringAsFixed(2);

    if (showAsField == '1') {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 8.0),
        child: TextFormField(
          initialValue: newValue,
          decoration: InputDecoration(
            labelText: name.isNotEmpty ? name : 'Minimum Daily Qty',
            border: const OutlineInputBorder(),
          ),
          readOnly: true,
          enabled: false,
        ),
      );
    }
    return Text(newValue);
  }
}

class UserTotalQtyAndCondition extends StatefulWidget {
  final Map<String, dynamic> config;
  final String value;
  final Function onChanged;
  final String action;
  final Map<String, dynamic>? props;

  const UserTotalQtyAndCondition({
    Key? key,
    required this.config,
    required this.value,
    required this.onChanged,
    required this.action,
    this.props = const {},
  }) : super(key: key);

  @override
  UserTotalQtyAndConditionState createState() =>
      UserTotalQtyAndConditionState();
}

class UserTotalQtyAndConditionState
    extends State<UserTotalQtyAndCondition> {
  final FlutterSecureStorage storage = storageLocator<FlutterSecureStorage>();
  Map<String, dynamic>? userData;
  String? errorMessage;
  bool ignoreUserData = false;

  @override
  void initState() {
    super.initState();
    _loadUserData();
  }

  Future<void> _loadUserData() async {
    try {
      ignoreUserData = false;
      if (widget.props!.containsKey('ignoreUserData')) {
        ignoreUserData = widget.props!['ignoreUserData'];
      }
      final userDataValue = await storage.read(key: 'user_data');
      if (userDataValue == null) {
        setState(() {
          errorMessage = "User data not found [2]";
        });
        return;
      }

      final currentUserData =
          Map<String, dynamic>.from(json.decode(userDataValue));
      final preparedData = prepareUserDataForMDC(currentUserData);

      setState(() {
        userData = preparedData;
        if (debug) {
          logDebug(
              'UserTotalQtyAndCondition | _loadUserData | userData: $userData');
        }
      });
    } catch (e) {
      setState(() {
        errorMessage = "Error loading user data: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    if (errorMessage != null) {
      return Text(errorMessage!, style: const TextStyle(color: Colors.red));
    }

    if (userData == null) {
      return const SizedBox.shrink();
    }

    final totalQty = double.tryParse(widget.value) ?? 0.0;
    final minimumDailyQty = getMinimumDailyQuantity(
      userData!['dateOfBirth'].toString(),
      userData!['gender'].toString(),
      userData!['goal_code']?.toString(),
    );

    return DailyCondition(
      minimumDailyQty: minimumDailyQty.value,
      totalQty: totalQty,
      showAsField: '0',
    );
  }
}

class UserMinimumDailyQty extends StatefulWidget {
  final Map<String, dynamic> config;
  final String value;
  final Function onChanged;
  final String action;
  final Map<String, dynamic>? props;

  const UserMinimumDailyQty({
    Key? key,
    required this.config,
    required this.value,
    required this.onChanged,
    required this.action,
    this.props = const {},
  }) : super(key: key);

  @override
  UserMinimumDailyQtyState createState() =>
      UserMinimumDailyQtyState();
}

class UserMinimumDailyQtyState extends State<UserMinimumDailyQty> {
  final FlutterSecureStorage storage = storageLocator<FlutterSecureStorage>();
  Map<String, dynamic>? userData;
  String? errorMessage;
  bool ignoreUserData = false;

  @override
  void initState() {
    super.initState();
    _loadUserData();
  }

  Future<void> _loadUserData() async {
    try {
      ignoreUserData = false;
      if (widget.props!.containsKey('ignoreUserData')) {
        ignoreUserData = widget.props!['ignoreUserData'];
      }

      final userDataValue = await storage.read(key: 'user_data');
      if (userDataValue == null) {
        if (!ignoreUserData) {
          setState(() {
            errorMessage = "User data not found [3]";
          });
        }
        return;
      }

      final currentUserData =
          Map<String, dynamic>.from(json.decode(userDataValue));
      final preparedData = prepareUserDataForMDC(currentUserData);

      setState(() {
        userData = preparedData;
      });
    } catch (e) {
      setState(() {
        errorMessage = "Error loading user data: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    if (errorMessage != null) {
      return Text(errorMessage!, style: const TextStyle(color: Colors.red));
    }

    if (userData == null) {
      return const SizedBox.shrink();
    }

    return MinimumDailyQty(
      data: userData!,
      name: widget.config['label'] ?? '',
      showAsField: '1',
    );
  }
}

// Factory functions to be used in CrudEditor callbacks

Widget userMinimumDailyQty({
  required Map<String, dynamic> config,
  required String value,
  required Function onChanged,
  required String action,
  required BuildContext context,
  Map<String, dynamic>? props,
}) {
  return UserMinimumDailyQty(
    config: config,
    value: value,
    onChanged: onChanged,
    action: action,
    props: props,
  );
}

Widget userTotalQtyAndCondition({
  required Map<String, dynamic> config,
  required String value,
  required Function onChanged,
  required String action,
  required BuildContext context,
  Map<String, dynamic>? props,
}) {
  return UserTotalQtyAndCondition(
    config: config,
    value: value,
    onChanged: onChanged,
    action: action,
    props: props,
  );
}
```

### Componentes secundarios (relaciones 1-N)

El editor CRUD de Flutter gestiona `childComponents` del mismo modo que el editor CRUD de [genericsuite-fe (React)](https://github.com/tomkat-cr/genericsuite-fe/blob/main/src/lib/services/generic.editor.rfc.service.jsx): la configuración JSON del frontend de una entidad principal enumera los nombres de sus componentes secundarios, y cada uno se muestra dentro del formulario de edición de la entidad principal.

Configuración de la entidad principal (`assets/config_dbdef/frontend/users.json`):

```json
{
    "childComponents": [
        "UsersFoodTimes"
    ]
}
```

En dispositivos móviles, cada componente secundario aparece como una sección seleccionable en la parte inferior del formulario de **edición** de la entidad principal (nunca al crearla).

Al tocar una sección, se abre el editor secundario a pantalla completa y se le pasa la fila principal mediante `parentData`.

Registra un constructor para cada nombre en el mapa `callbacks['childComponents']`:

```dart
Map<String, dynamic> callbacks = {
  "childComponents": {
    "UsersFoodTimes": ({
      required Map<String, dynamic> parentData,
      Map<String, dynamic>? props,
    }) =>
        CrudEditor(
          jsonFileName: 'users_food_times.json',
          callbacks: {},
          props: {...?props, 'parentData': parentData},
        ),
  },
};
```

NOTA: es importante propagar el `props` recibido al `props` de `CrudEditor` (contiene `isChildComponent: true` y `showAppMenu: false`, que habilitan el botón para volver en la pantalla abierta) y añadir `'parentData': parentData`.

Por lo general, el constructor devuelve un `CrudEditor` cuya configuración JSON tiene `"type": "child_listing"`, un `"subType"` con el valor `"array"` (las filas secundarias se almacenan en un atributo de tipo array de la fila principal; requiere `"array_name"`) o `"table"` (las filas secundarias están en su propia tabla), y `"endpointKeyNames"`, que asigna el nombre del parámetro de la API al campo del ID de la fila principal.

Así, en este caso, la configuración JSON del componente secundario declara la relación:

```json
{
    "type": "child_listing",
    "subType": "array",
    "array_name": "food_times",
    "parentUrl": "users",
    "endpointKeyNames": [
        {
          "parameterName": "user_id",
          "parentElementName": "_id"
        }
    ]
}
```

- `subType: "array"`: las filas secundarias se encuentran dentro de un atributo de tipo array de la fila principal (se requiere `array_name`). Las escrituras envían `{parentKey, <array_name>: newValues, <array_name>_old: initialValues}`.
- `subType: "table"`: las filas secundarias están en su propia tabla; la clave de la entidad principal se combina con cada fila secundaria.

### CRUD basado en JSON

#### assets/config_dbdef/backend/app_main_menu.json

Aquí puedes definir la estructura del menú de la aplicación. El menú se define como una lista de elementos, cada uno de los cuales puede ser un enlace de navegación (`nav_link`, un elemento de nivel superior) o un menú desplegable (`nav_dropdown`, un elemento que contiene una lista de otros elementos).

```json
[
    {
        "title": "Dashboard",
        "location": "top_menu",
        "type": "nav_link",
        "path": "/",
        "element": "HomePage",
        "hard_prefix": false,
        "reload": true
    },
    {
        "title": "Sub Menu",
        "location": "top_menu",
        "type": "nav_dropdown",
        "sec_group": "users",
        "sub_menu_options": [
            {
                "type": "editor",
                "sec_group": "users",
                "title": "Any Other Table",
                "element": "ExampleappAnyOtherCrudEditorView_EditorData"
            }
        ]
    },
    {
        "title": "User Menu",
        "location": "hamburger",
        "sub_menu_options": [
            {
                "title": "Profile",
                "path": "/profile",
                "element": "UserProfileEditor"
            },
            {
                "title": "About",
                "on_click": "|about|"
            },
            {
                "title": "Logout",
                "path": "/logout",
                "on_click": "logout"
            }
        ]
    }
]
```

#### assets/config_dbdef/backend/exampleapp_any_other_table.json

Aquí puedes definir el nombre físico de la tabla y otras opciones de configuración del Backend para la tabla de la base de datos.

```json
{
    "table_name": "any_other_table"
}
```

#### assets/config_dbdef/frontend/exampleapp_any_other_table.json

Aquí puedes definir la configuración para mostrar los datos de la tabla en una vista del editor CRUD.

```json
{
    "baseUrl": "any_other_table",
    "title": "Any Other Tables",
    "name": "Any Other Table",
    "component": "ExampleappAnyOtherCrudEditorView",
    "dbApiUrl": "any_other_table",
    "mandatoryFilters": {
        "user_id": "{CurrentUserId}"
    },
    "createReenter": true,
    "defaultOrder": "any_other_date|desc",
    "fieldElements": [
        {
            "name": "id",
            "required": true,
            "label": "ID",
            "type": "_id",
            "readonly": true,
            "hidden": true
        },
        {
            "name": "user_id",
            "required": true,
            "label": "User ID",
            "type": "text",
            "readonly": true,
            "hidden": true
        },
        {
            "name": "any_other_date",
            "required": true,
            "label": "Date",
            "type": "date",
            "readonly": false,
            "listing": true
        },
        {
            "name": "today_total_qty",
            "label": "Total Quantity",
            "type": "number",
            "readonly": true,
            "listing": true,
            "component": "UserTotalQtyAndCondition"
        },
        {
            "name": "minimun_daily_qty",
            "label": "Minimun Daily Quantity",
            "type": "component",
            "component": "UserMinimumDailyQty",
            "readonly": true,
            "listing": false
        },
        {
            "name": "observations",
            "required": false,
            "label": "Observations",
            "type": "textarea",
            "readonly": false,
            "listing": true
        }
    ],
    "childComponents": [
        "DailyMealIngredients"
    ]
}
```

#### Pantalla de listado

La pantalla de listado muestra las filas de una entidad. Cada fila puede tener dos líneas de texto:

- La línea 1 es el título de la fila. Muestra las primeras columnas del listado.
- La línea 2 es el subtítulo de la fila. Muestra las columnas siguientes del listado.

Una columna del listado es un campo con `"listing": true`. Las columnas aparecen en el mismo orden que en `fieldElements`.

Define el número de columnas de cada línea en el archivo JSON del frontend de la entidad (`assets/config_dbdef/frontend/<entity>.json`). Usa estas dos claves opcionales de nivel superior de tipo int:

| Clave | Predeterminado | Uso |
| --- | --- | --- |
| `colsForListingLine1` | `1` | Número de columnas del listado en la línea 1 (título de la fila) |
| `colsForListingLine2` | `0` | Número de columnas del listado en la línea 2 (subtítulo de la fila). `0` significa que no se muestra ningún subtítulo. |

Ejemplo:

```json
{
    "name": "users",
    "colsForListingLine1": 2,
    "colsForListingLine2": 2,
    "fieldElements": [
        {
            "name": "firstname",
            "label": "First name",
            "type": "text",
            "listing": true
        },
        {
            "name": "lastname",
            "label": "Last name",
            "type": "text",
            "listing": true
        },
        {
            "name": "email",
            "label": "Email",
            "type": "text",
            "listing": true
        },
        {
            "name": "superuser",
            "label": "Superuser",
            "type": "boolean",
            "listing": true
        }
    ]
}
```

Con este ejemplo, cada fila muestra:

- Línea 1: `John · Smith`
- Línea 2: `john@mail.com · Yes`

Estas son las reglas:

- La prioridad es: el valor de `CrudEditor(props: {...})`, luego el valor del JSON del frontend y, por último, el valor predeterminado.
- El valor puede ser un int o una cadena numérica, por ejemplo, `"2"`.
- Si el valor no es válido, se utiliza el valor predeterminado.
- Los valores negativos se convierten en `0`.
- El número total de columnas está limitado por la cantidad de campos del listado.
- Si la línea 1 es `0` y la entidad tiene campos de listado, la línea 1 pasa a ser `1`.

Los valores se formatean en el listado:

| Tipo de campo | Valor del listado |
| --- | --- |
| `select_table` | La descripción |
| `select` | La etiqueta de la opción. Si no hay etiqueta, se muestra el valor sin procesar. |
| `date` | `yyyy-MM-dd` |
| `datetime` | `yyyy-MM-dd HH:mm` |
| `boolean` | `Yes` o `No` |

Los valores vacíos o nulos no se muestran. Los valores de una misma línea se unen con el parámetro de tema `listingColumnSeparator` (por defecto, `' · '`).

Los colores de las filas y el separador son parámetros del tema. Consulta [Tematización](#tematización). Para sobrescribirlos, usa `getThemeParams()`:

```dart
class AppCallables extends AppCallablesSuper {
  @override
  Map<String, dynamic> getThemeParams() {
    return {
      'listingRowEvenBackgroundColor': Colors.white,
      'listingRowOddBackgroundColor': Color(0xFFF2F2F7),
      'listingColumnSeparator': ' | ',
    };
  }
}
```

Para establecer las columnas en el código, pasa las mismas claves en las propiedades de `CrudEditor`:

```dart
CrudEditor(
  jsonFileName: 'users.json',
  callbacks: {},
  props: {
    'colsForListingLine1': 2,
    'colsForListingLine2': 1,
  },
)
```

### Configuración de la aplicación

#### assets/config

Para cada entorno (dev, qa, staging, prod, demo, etc.), debe haber archivos `config-{stage}.json` y `stage-{stage}.json` en el directorio `assets/config` con la siguiente estructura:

#### assets/config/config-dev.json

```json
{
  "API_URL": "https://app.exampleapp.local:5001/v1",
  "ENV": "local",
}
```

#### assets/config/config-prod.json

```json
{
  "API_URL": "https://app.exampleapp.com/v1",
  "ENV": "prod",
}
```

#### assets/config/stage-dev.json

```json
{
  "STAGE": "dev"
}
```

#### assets/config/stage-prod.json

```json
{
  "STAGE": "prod"
}
```

#### assets/config/stage.json

Este archivo define el entorno en uso. Puede ser `dev`, `qa`, `staging`, `prod`, `demo`, etc.

```json
{
  "STAGE": "dev"
}
```

## Estructura de directorios del paquete GenericSuite

```
genericsuite
├── analysis_options.yaml
├── CHANGELOG.md
├── genericsuite.iml
├── lib
│   ├── genericsuite.dart
│   ├── services
│   │   ├── app_callables_super.dart
│   │   ├── autocomplete_service.dart
│   │   ├── config_service.dart
│   │   ├── convertion_utilities.dart
│   │   ├── crud_editor_commons.dart
│   │   ├── crud_editor_selector.dart
│   │   ├── crud_editor_sf_filters.dart
│   │   ├── crud_editor_sf_timestamps.dart
│   │   ├── crud_editor_sf_users.dart
│   │   ├── crud_editor.dart
│   │   ├── current_user_service.dart
│   │   ├── form_field_service.dart
│   │   ├── general_messages.dart
│   │   ├── http_service.dart
│   │   ├── logout_service.dart
│   │   ├── message_service.dart
│   │   ├── redirect_service.dart
│   │   ├── select_options_service.dart
│   │   ├── theme_config_defaults.dart
│   │   ├── timestamp_utilities.dart
│   │   └── utilities.dart
│   ├── views
│   │   ├── homepage.dart
│   │   └── login.dart
│   └── widgets
│       ├── app_drawer.dart
│       ├── app_frame.dart
│       ├── back_button.dart
│       └── error_reporter_widget.dart
├── LICENSE
├── pubspec.lock
├── pubspec.yaml
├── README.md
└── test
    └── genericsuite_test.dart
```

## Información adicional

- README de la biblioteca:
  [genericsuite_flutter](https://github.com/tomkat-cr/genericsuite-mobile/tree/main/genericsuite_flutter)

- Plantilla de inicio:
  [flutter_project_template](https://github.com/tomkat-cr/genericsuite-mobile-exampleapp)