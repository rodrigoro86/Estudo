import './MenuSidebar.css'


const MenuSidebar = (props) =>{
    return (
        <a href={props.referencia}>{props.nomeMenu}</a>
    )
}

export default MenuSidebar