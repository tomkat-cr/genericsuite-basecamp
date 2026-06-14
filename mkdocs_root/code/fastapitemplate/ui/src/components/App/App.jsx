import React from 'react';

// import * as gs from "genericsuite";
import { App as GsAiApp } from "genericsuite-ai";

import { Users_EditorData } from '../SuperAdminOptions/Users.jsx';
import { UserProfileEditor } from '../UsersMenu/UserProfile.jsx';

import { AboutBody } from '../About/About.jsx';
import { HomePage } from '../HomePage/HomePage.jsx';

// const AppLogo = 'app_logo_square.svg';
const AppLogo = 'app_logo_circle.svg';
const AppLogoHeader = 'app_logo_horizontal.svg';

const componentMap = {
    "UserProfileEditor": UserProfileEditor,
    "Users_EditorData": Users_EditorData,
    "AboutBody": AboutBody,
    "HomePage": HomePage,
};

export const App = () => {
    return (
        <GsAiApp
            appLogo={AppLogo}
            appLogoHeader={AppLogoHeader}
            componentMap={componentMap}
        />
    );
}