import './CampoTexto.css'
import { useState } from 'react'


const CampoTexto = (props) => {
    const ao_digitar = (evento) => {
        props.aoAlterado(evento.target.value)
    }
    
    return (
        <div className="campo-texto">
            <label>{props.label}</label>
            <input onChange={ao_digitar} placeholder={props.placeholder}/>
        </div>
    )
}

export default CampoTexto

