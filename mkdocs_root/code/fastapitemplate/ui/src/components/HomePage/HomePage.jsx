import React from 'react';
import * as gs from "genericsuite";

const useUser = gs.UserContext.useUser;
const debug = false;

export const HomePage = () => {
    const { currentUser } = useUser();
    return (
        <gs.HomePage>
            <>
                <h2>Hi {currentUser.firstName}!</h2>
            </>
        </gs.HomePage>
    );
}
