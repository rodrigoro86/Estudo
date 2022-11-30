import MenuSidebar from '../MenuSidebar'
import './Sidebar.css'

const Sidebar = () => {
    return (
        <div class="sidebar">
            <div class="menu">
                
                <MenuSidebar nomeMenu="Dashboard" referencia="#Dashboard"/>
                {/*<MenuSidebar nomeMenu="Contas" referencia="#Contas"/>*/}
                <a class="active"  href="index.html">Contas</a>
                <MenuSidebar nomeMenu="Receita" referencia="#Receita"/>
                <MenuSidebar nomeMenu="Sobre" referencia="#Sobre"/>
            </div>
        </div>
    )
}

export default Sidebar
