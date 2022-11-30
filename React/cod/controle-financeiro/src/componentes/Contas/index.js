import CampoDate from '../CampoDate'
import CampoDinheiro from '../CampoDinheiro'
import CampoTexto from '../CampoTexto'
import './Contas.css'

const Contas = () =>{
    return (
        <section className="formulario">
            <form>
               <CampoTexto label="Nome da Conta" placeholder="Digite o nome da conta"/>
               <CampoDate label="Data da Conta"/>
               <CampoDinheiro label="Valor da Conta" />
            </form>
        </section>
    )
}

export default Contas