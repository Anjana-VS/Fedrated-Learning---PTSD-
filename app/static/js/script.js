function playSound() {
    var audio = new Audio("{% static 'sounds/success-sound.mp3' %}");
    audio.play();
}
