import { useState } from "react";
import logoHelp from "../../images/help.png"

function Questions({id, hash, response, help}) {

    const [inputContent, setInputContent] = useState("");
    const [buttonContent, setButtonContent] = useState("Envoyer");
    const [helperView, setHelperView] = useState(false);
    const [isValid, setisValid] = useState(false);

    const checkResponse = (responseSend) => {
        let inputSelect = document.querySelector('#response_'+id);
        if(responseSend === response){
            setButtonContent("Correct !")
            inputSelect.style.backgroundColor = '#81dd81ff';
            setisValid(true)
        }
        else{
            inputSelect.style.backgroundColor = '#fbd6d0';
            setInputContent('Mauvaise réponse')
        }
    }

    const hundelInput = (evt) => {
        setInputContent(evt.target.value)
    }

    const hundelSubmit = (evt) => {
        evt.preventDefault();
        checkResponse(inputContent)
    }

    const hundelMouseEnter = (evt) => {
        setHelperView(true)
    }

    const hundelMouseLeave = (evt) => {
        setHelperView(false)
    }

    return (
        <div className="m-2 ">
            <h3 className="text-xl" >{hash}</h3>
            <form onSubmit={hundelSubmit} className="flex items-center">
                <input id={"response_"+id} disabled={isValid} className="rounded-lg w-1/2 m-2 text-[#282c34]" value={inputContent} onChange={hundelInput} />
                <input type="submit" id={"button_"+id} value={buttonContent} className="m-2" />
                <div className="flex static">
                    <img onMouseEnter={hundelMouseEnter} onMouseLeave={hundelMouseLeave} src={logoHelp} className="w-8 m-2 rounded-full bg-[#ff8a00]" alt="logo" />
                    {helperView && <div className="ml-12 mt-2 absolute">{help}</div> }
                </div>
            </form>
        </div>
    );
}

export default Questions;
