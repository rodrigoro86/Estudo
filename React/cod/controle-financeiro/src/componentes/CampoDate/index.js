import './CampoDate.css'
import { useState } from 'react'


const CampoDate = (props) => {

    const dataAtual = new Date().toISOString().split('T')[0]
    props.aoAlterado(dataAtual)
    const ao_digitar = (evento) => {
        props.aoAlterado(evento.target.value)
    }
    return (
        <div className="campo-texto">
            <label>{props.label}</label>
            <input onChange={ao_digitar} type="date" name="data-conta" defaultValue={dataAtual} /> 
        </div>
    )
}

export default CampoDate

