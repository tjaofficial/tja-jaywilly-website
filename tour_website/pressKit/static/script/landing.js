function transition_into_layout(){
    console.log(document.getElementsByTagName('body')[0].style.backgroundImage);
    document.getElementsByTagName('body')[0].style.backgroundImage = 'linear-gradient(to left, #005544 0%, #005544 80%, #FF7F50 80%, #FF7F50 100%)';
}