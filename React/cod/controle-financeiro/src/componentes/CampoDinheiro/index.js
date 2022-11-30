import './CampoDinheiro.css'
import React, { useState } from 'react';

const CampoDinheiro = (props) => {

    return (
        <div className="campo-dinheiro">
            <label>{props.label}</label>
            <input type="number" />
        </div>
    )
}

export default CampoDinheiro

