import React from 'react'

import * as gs from "genericsuite";

const GsAboutBody = gs.AboutBody;
const console_debug_log = gs.loggingService.console_debug_log;

const debug = false;

export const AboutBody = () => {
    if (debug) console_debug_log('>>>> ExampleApp AboutBody <<<<');
    return (
        <GsAboutBody>
            <>
                <p>
                    <b>ExampleApp</b> is an application to achieve weight loss goals and maintain a better lifestyle, based on proper nutrition, a positive mindset, and physical activity.
                </p>
                <p>&nbsp;</p>
                <p>
                    ExampleApp let users record their preferred food ingredients, recipes, daily meals, keep track their calorie consumption and build caloric deficit menus based on the ingredients and recipes they can pay for and like the most. It brings AI-powered experiences to the users by letting them to communicate by voice, text or sending images to a specialized assistant called ExampleApp Bot, which is based on large language models, speech-to-text, text to image and image to text technologies.
                </p>
            </>
        </GsAboutBody>
    )
}
