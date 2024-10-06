function handleButtonClick() {
    document.getElementById("testButton").style.backgroundcolor ="darkgrey"

    fetch('/button-clicked', {
        method: 'POST'
    }).then(response => {
        console.log('Button click recorded')
    });
}