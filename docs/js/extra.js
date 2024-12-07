document.addEventListener('DOMContentLoaded', function() {
    // Select all anchor tags with href starting with "http"
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([target="_blank"])');
    
    externalLinks.forEach(function(link) {
        link.setAttribute('target', '_blank'); // Open in new tab
        link.setAttribute('rel', 'noopener noreferrer'); // Security improvement
    });
});

// Function for collapsible warning banners: Toggles the open class on the collapsible content and the rotate class on the arrow to expand/collapse the section.
function toggleCollapse(element) {
const collapsibleContent = element.nextElementSibling;
const arrow = element.querySelector('.arrow');

if (collapsibleContent.classList.contains('open')) {
    collapsibleContent.classList.remove('open');
    arrow.classList.remove('rotate');
} else {
    collapsibleContent.classList.add('open');
    arrow.classList.add('rotate');
}
}

// Auto-expand collapsible banners on external navigation
window.addEventListener('DOMContentLoaded', () => {
  const hash = window.location.hash;
  const bannerIds = ['warning-banner', 'alert-banner', 'notification-banner'];

  if (bannerIds.includes(hash.substring(1))) {
    const banner = document.getElementById(hash.substring(1));
    if (banner) {
      toggleCollapse(banner);
      banner.scrollIntoView({ behavior: 'smooth' });
    }
  }
});

// Auto-expand collapsible notification banner on page load
window.addEventListener('DOMContentLoaded', () => {
  const banner = document.getElementById('notification-banner');
  if (banner) {
    // Ensure the banner is expanded (assuming toggleCollapse is defined)
    if (banner.classList.contains('collapsed')) {
      toggleCollapse(banner);
    }
  }
});