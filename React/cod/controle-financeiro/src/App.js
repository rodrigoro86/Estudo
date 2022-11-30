import Sidebar from './componentes/Sidebar';
import Contas from './componentes/Contas';

function App() {
  return (
    <div className="App">
      <Sidebar />
      <div class="content">
        <Contas />
      </div>      
    </div>
  );
}

export default App;
