


document.addEventListener('DOMContentLoaded', function() {
    // Exemples d'effets ou d'interactions supplémentaires
    const profileImg = document.querySelector('.profile-img');
    profileImg.addEventListener('mouseenter', function() {
        profileImg.style.transform = 'scale(1.1)';
        profileImg.style.transition = 'transform 0.2s';
    });
    profileImg.addEventListener('mouseleave', function() {
        profileImg.style.transform = 'scale(1)';
    });
});











/*
document.addEventListener('DOMContentLoaded', function() {
    const profileCard = document.querySelector('.profile-card');
    const detailsCard = document.querySelector('.details-card');

    // Example of a simple animation on card hover
    profileCard.addEventListener('mouseover', function() {
        profileCard.style.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.2)';
    });

    profileCard.addEventListener('mouseout', function() {
        profileCard.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
    });

    detailsCard.addEventListener('mouseover', function() {
        detailsCard.style.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.2)';
    });

    detailsCard.addEventListener('mouseout', function() {
        detailsCard.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
    });
});

*/

/*
document.addEventListener('DOMContentLoaded', function() {
    // Example of adding some JavaScript interactions or animations if needed
    const profileImage = document.querySelector('.profile-img');
    profileImage.addEventListener('mouseenter', () => {
        profileImage.classList.add('rotate');
    });
    profileImage.addEventListener('mouseleave', () => {
        profileImage.classList.remove('rotate');
    });
});

*/



/*

// Add any custom JavaScript if needed
document.addEventListener('DOMContentLoaded', function() {
    console.log('Profile page loaded');
});

*/