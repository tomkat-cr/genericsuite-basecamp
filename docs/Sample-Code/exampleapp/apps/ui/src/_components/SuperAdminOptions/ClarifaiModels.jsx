import React from 'react';

import * as gs from "genericsuite";
import clarifai_models from "../../configs/frontend/clarifai_models.json";

const GenericCrudEditor = gs.genericEditorRfcService.GenericCrudEditor;
const GetFormData = gs.genericEditorRfcService.GetFormData;
const TRUE_FALSE = gs.generalConstants.TRUE_FALSE;

export function ClarifaiModels_EditorData() {
    // console_debug_log("ClarifaiModels_EditorData");
    const registry = {
        "ClarifaiModels": ClarifaiModels, 
        "TRUE_FALSE": TRUE_FALSE,
    }
    return GetFormData(clarifai_models, registry, 'ClarifaiModels_EditorData');
}

export const ClarifaiModels = () => (
    <GenericCrudEditor editorConfig={ClarifaiModels_EditorData()} />
)
