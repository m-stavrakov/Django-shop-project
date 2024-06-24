// $(document).ready(function(){
//     $('[data-toggle="tooltip"]').tooltip();
//   });

// Visible/Invisible password
document.addEventListener('DOMContentLoaded', function() {
  const passwordToggles = document.querySelectorAll('.password-toggle');

  passwordToggles.forEach(function(toggle) {
      toggle.addEventListener('click', function() {
          const inputGroup = toggle.closest('.input-group');
          if (inputGroup) {
              const passwordField = inputGroup.querySelector('.password');
              if (passwordField) {
                  const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
                  passwordField.setAttribute('type', type);

                  const toggleText = toggle.querySelector('.showPasswordToggle');
                  if (toggleText) {
                      toggleText.textContent = type === 'password' ? 'Show' : 'Hide';
                  }
              }
          }
      });
  });
});

// Opening item description when clicking on the image in inbox
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.inbox-container').forEach(function(container) {
      container.addEventListener('click', function(event) {
          if (!event.target.closest('.inbox-img-wrapper')) {
              window.location.href = container.getAttribute('data-url');
          }
      });
  });

  // Function to handle click on the image wrapper
  document.querySelectorAll('.inbox-img-wrapper').forEach(function(wrapper) {
      wrapper.addEventListener('click', function(event) {
          event.stopPropagation(); // Prevent the click from bubbling up to the container
          window.location.href = wrapper.getAttribute('data-url');
      });
  });
});

// Loading longer description of items
document.addEventListener('DOMContentLoaded', function(){
  let readMoreBtn = document.getElementById('readMoreBtn');
    if (readMoreBtn) {
        let truncated = document.getElementById('truncated');
        let moreText = document.getElementById('moreText');
        
        readMoreBtn.addEventListener('click', function() {
            if (moreText.style.display === 'none' || moreText.style.display === '') {
                truncated.style.display = 'none';
                moreText.style.display = 'inline';
                readMoreBtn.textContent = 'Read less';
            } else {
                truncated.style.display = 'inline';
                moreText.style.display = 'none';
                readMoreBtn.textContent = 'Read more';
            }
        });
    }
})

// Showing the latest message in conversation page
// let chatContainer = document.getElementById('chatContainer');
// if(chatContainer){
  document.addEventListener('DOMContentLoaded', function() {
    let chatContainer = document.getElementById('chatContainer')
    chatContainer.scrollTop = chatContainer.scrollHeight;
  });
// }