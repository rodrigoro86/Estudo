import './CampoDinheiro.css'
import React, { useState } from 'react';

const CampoDinheiro = (props) => {
    const ao_digitar = (evento) => {
        props.aoAlterado(evento.target.value)
    }
    return (
        <div className="campo-dinheiro">
            <label>{props.label}</label>
            <input onChange={ao_digitar} type="number" />
        </div>
    )
}

export default CampoDinheiro

