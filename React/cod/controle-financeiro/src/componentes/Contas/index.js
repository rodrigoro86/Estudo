import Botao from '../Botao'
import CampoDate from '../CampoDate'
import CampoDinheiro from '../CampoDinheiro'
import CampoTexto from '../CampoTexto'
import './Contas.css'
import { useState } from 'react';

const Contas = () =>{
    const [nome, setNome] = useState('')
    const [data, setData] = useState('')
    const [valor, setValor] = useState('')

    const aoSalvar = (evento) => {
        evento.preventDefault()
        console.log('Form foi submetido => ', nome, data, valor)
    }

    return (
        <section className="formulario">
            <form onSubmit={aoSalvar}>
                <CampoTexto 
                    label="Nome da Conta" 
                    placeholder="Digite o nome da conta"
                    valor={nome}
                    aoAlterado={valor => setNome(valor)}
                />
                <CampoDate 
                    label="Data da Conta"
                    valor={data}
                    aoAlterado={valor => setData(valor)}
                />
                <CampoDinheiro 
                    label="Valor da Conta" 
                    valor={valor}
                    aoAlterado={valor => setValor(valor)}
                />
                <Botao>
                    Salvar
                </Botao>
            </form>
        </section>
    )
}

export default Contas