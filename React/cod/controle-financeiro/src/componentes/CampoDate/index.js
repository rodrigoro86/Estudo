import './CampoDate.css'
import { useState } from 'react'


const CampoDate = (props) => {

    const dataAtual = new Date().toISOString().split('T')[0]
    
    return (
        <div className="campo-texto">
            <label>{props.label}</label>
            <input type="date" name="data-conta" defaultValue={dataAtual} /> 
            {console.log(dataAtual)}
        </div>
    )
}

export default CampoDate

