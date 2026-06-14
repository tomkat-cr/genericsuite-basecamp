import React from 'react'

import * as gs from "genericsuite";

const GsAboutBody = gs.AboutBody;

const debug = false;

export const AboutBody = () => {
    return (
        <GsAboutBody>
            <>
                <p>
                    <b>FastApiTemplate</b> is a full-stack application that allows you to have a template to start your FastAPI application based on GenericSuite.
                </p>
                <p>&nbsp;</p>
                <p>
                    FastApiTemplate brings AI-powered experiences to the users by letting them to communicate by voice, text or sending images to a specialized assistant called 'AI Assistant', which is based on large language models, speech-to-text, text to image and image to text technologies.
                </p>
            </>
        </GsAboutBody>
    )
}
