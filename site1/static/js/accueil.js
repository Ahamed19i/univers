





document.addEventListener('DOMContentLoaded', function () {
    var marquee = document.querySelector('.marquee-content');
    var clone = marquee.cloneNode(true);
    marquee.parentNode.appendChild(clone);
});
