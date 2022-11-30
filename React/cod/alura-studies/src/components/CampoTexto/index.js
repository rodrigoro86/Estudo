import './CampoTexto.css'
import { useState } from 'react'

const CampoTexto = (props) => {
    const placeholderModificada = `${props.placeholder}...`

    const ao_digitar = (evento) => {
        props.aoAlterado(evento.target.value)
    }

    return (
        <div className="campo-texto">
            <label>{ props.label }</label>
            <input value={props.valor} onChange={ao_digitar} required={props.obrigatorio} placeholder={placeholderModificada}/>
        </div>
    )
}

export default CampoTexto