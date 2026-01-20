import Questions from '../Questions'

function Level1({passwordList}) {
    return (
        <section className='border-b-2 pb-4 m-4 border-[#61dafb]'>
            <h2 className="text-2xl m-4 font-bold underline">Level 1</h2>
            <p className='py-2 m-4 border-b-2 border-[#61dafb]'>Pouvez-vous accomplir les tâches du level 1 en déchiffrant ces hachages ?</p>
            {passwordList.map((password) => (
                <Questions key={password.id} id={password.id} hash={password.hash} response={password.response} help={password.help} />
            ))}    
        </section>
    );
}

export default Level1;
