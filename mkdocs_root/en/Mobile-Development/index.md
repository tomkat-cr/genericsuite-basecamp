# GenericSuite Mobile (Flutter)

[GenericSuite Mobile](https://github.com/tomkat-cr/genericsuite-mobile) brings
the GenericSuite JSON-driven CRUD pattern to Flutter apps: define your
entities in JSON config files and mount the `CrudEditor` widget — no
per-entity Dart code needed for standard CRUD.

Repository layout:

- `genericsuite_flutter/` — the reusable Flutter library (consumed as a Git
  dependency).
- `flutter_project_template/` — a starter app template showing real-world
  usage.

## Installation

Add the library to your app's `pubspec.yaml`:

```yaml
dependencies:
  genericsuite:
    git:
      url: https://github.com/tomkat-cr/genericsuite-mobile.git
      path: genericsuite_flutter
      ref: main
```

## App bootstrap

Subclass `AppCallablesSuper` to inject your app's behavior, then start the
app with `CreateGsApp`:

```dart
void main() {
  runApp(CreateGsApp(appCallables: AppCallables()));
}
```

`CreateGsApp` builds the widget-tree root with `ShadApp`
([shadcn_ui](https://pub.dev/packages/shadcn_ui), the Flutter port of
ShadCN) and derives the `MaterialApp` theme from the GenericSuite theme
tokens (see [Theming](#theming)).

## JSON-driven CRUD

Configuration files live under `assets/`:

- `assets/config/stage.json` — selects the environment (`dev`, `qa`,
  `staging`, `prod`).
- `assets/config/config-{stage}.json` — API base URL and other values.
- `assets/config_dbdef/backend/*.json` — REST endpoint + schema definitions.
- `assets/config_dbdef/frontend/*.json` — field types, labels, form layout.

Mount an editor:

```dart
CrudEditor(
  jsonFileName: 'users.json',
  callbacks: callbacks,
  props: props,
)
```

## Child components (1-N relationships)

The Flutter CRUD Editor handles `childComponents` the same way the
genericsuite-fe (React) CRUD Editor does: the frontend JSON config of a
parent entity lists child component names, and each one renders inside the
parent's edit form.

Parent config (`assets/config_dbdef/frontend/users.json`):

```json
{
    "childComponents": [
        "UsersFoodTimes"
    ]
}
```

On mobile, each child appears as a tappable section at the bottom of the
parent's **edit** form (never on creation). Tapping opens the child editor
full-screen with the parent row passed as `parentData`.

Register a builder for each name in the `callbacks['childComponents']` map:

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

The child JSON config declares the relationship:

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

- `subType: "array"` — child rows live inside an array attribute of the
  parent row (`array_name` required). Writes send
  `{parentKey, <array_name>: newValues, <array_name>_old: initialValues}`.
- `subType: "table"` — child rows live in their own table; the parent key is
  merged into each child row.

## Theming

The design language is Apple-clean: white/neutral surfaces, near-black text,
one accent color (default `Colors.green`), 12 px corner radius, and iOS
system semantic colors.

Override `getThemeParams()` in your `AppCallables` to customize — return
only the keys you want to change; they are merged over the library defaults
(`defaultThemeParams` in `theme_config_defaults.dart`):

| Token | Default | Purpose |
| --- | --- | --- |
| `accentColor` | `Colors.green` | The single accent color |
| `borderRadius` | `12.0` | Corner radius (px) for inputs, buttons, cards |
| `fontFamily` | `'Inter'` | Typography; `'Inter'` loads via google_fonts (SF-Pro-like) |
| `textTheme` | `null` | Optional full `TextTheme` override |
| `textColor` | `#111111` | Near-black primary text |
| `secondaryTextColor` | `#6E6E73` | iOS secondary label |
| `separatorColor` | `#D1D1D6` | iOS separator (borders, dividers) |
| `neutralSurfaceColor` | `#F2F2F7` | iOS systemGray6 neutral surface |
| `scaffoldBackgroundColor` | `Colors.white` | Screen background |
| `appBarBackgroundColor` / `appBarForegroundColor` | white / near-black | App bar surfaces |
| `errorBackgroundColor` | `#FF3B30` (systemRed) | Error messages |
| `infoBackgroundColor` | `#007AFF` (systemBlue) | Info messages |
| `warningBackgroundColor` | `#FF9500` (systemOrange) | Warnings |
| `successBackgroundColor` | `#34C759` (systemGreen) | Success messages |

Example:

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

## More information

- Library README:
  [genericsuite_flutter](https://github.com/tomkat-cr/genericsuite-mobile/tree/main/genericsuite_flutter)
- Starter template:
  [flutter_project_template](https://github.com/tomkat-cr/genericsuite-mobile/tree/main/flutter_project_template)
