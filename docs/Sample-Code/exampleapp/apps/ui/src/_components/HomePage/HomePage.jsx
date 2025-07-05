import React from 'react';
// import { useState, useEffect } from 'react';

import * as gs from "genericsuite";

// const authenticationService = gs.authenticationService.authenticationService;
const useUser = gs.UserContext.useUser;
const console_debug_log = gs.loggingService.console_debug_log;

const debug = false;

export const HomePage = () => {
    if (debug) console_debug_log('>>>> ExampleApp HomePage <<<<');
    const { currentUser } = useUser();
    return (
        <gs.HomePage>
            <>
                <h2>Hi {currentUser.firstName}!</h2>
            </>
        </gs.HomePage>
    );
}
