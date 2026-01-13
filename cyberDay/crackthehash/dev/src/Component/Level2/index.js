import Questions from '../Questions'

function Level2({passwordList}) {
    return (
        <section className="border-b-2 pb-4 m-4 border-[#61dafb]">
            <h2 className="text-2xl m-4 font-bold underline">Level 2</h2>
            <p className='py-2 m-4 border-b-2 border-[#61dafb]'>
                On augmente la difficulté.<br />
                Toutes les réponses se trouvent dans la liste des mots de passe de <a href='https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt'>Rock You</a>.<br />
                Il vous faudra peut-être utiliser Hashcat plutôt que des outils en ligne.<br />
                Consulter des exemples de hachages sur la page de <a href='https://hashcat.net/wiki/doku.php?id=example_hashes'>Hashcat</a> pourrait également s'avérer utile.<br />
            </p>
            {passwordList.map((password) => (
                <Questions key={password.id} id={password.id} hash={password.hash} response={password.response} help={password.help} />
            ))}    
        </section>
    );
}

export default Level2;
