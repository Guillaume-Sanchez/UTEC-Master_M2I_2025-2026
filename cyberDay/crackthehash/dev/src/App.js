import logo from './images/logo.png';
import './App.css';
import {level1, level2} from './data';

// Components :

import Level1 from './Component/Level1';
import Level2 from './Component/Level2';

function App() {

  return (
    <>
      <header className="flex items-center justify-center mt-4">
        <img src={logo} className="w-16 m-2 rounded-full" alt="logo" />
        <h1 className="text-3xl m-2 font-bold">Crack the hash</h1>
      </header>

      <main className='mt-12 container mx-auto sm:px-2 md:px-24 lg:px-48'>
        <Level1 passwordList={level1} />
        <Level2 passwordList={level2} />
      </main>

      <footer className='text-center p-4'>
        Retrouvez le vrai challenge sur <a href='https://tryhackme.com/room/crackthehash'>tryhackme.com</a>
      </footer>
    </>
  );
}

export default App;
