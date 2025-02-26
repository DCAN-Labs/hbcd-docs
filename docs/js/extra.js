// Function to make embedded links open new tab when clicked
document.addEventListener('DOMContentLoaded', function() {
    // Select all anchor tags with href starting with "http"
    const externalLinks = document.querySelectorAll('a[href^="http"]:not([target="_blank"])');
    
    externalLinks.forEach(function(link) {
        link.setAttribute('target', '_blank'); 
        link.setAttribute('rel', 'noopener noreferrer');
    });
});

// Collapsible content: toggles open class AND rotate class to ON when arrow is clicked to expand/collapse the section.
function toggleCollapse(element) {
  const collapsibleContent = element.nextElementSibling;
  const arrow = element.querySelector(['.arrow', '.notification-arrow', '.table-arrow']);

  if (collapsibleContent.classList.contains('open')) {
    collapsibleContent.classList.remove('open');
    arrow.classList.remove('rotate');
  } else {
    collapsibleContent.classList.add('open');
    arrow.classList.add('rotate');
  }
}

// Utility function to expand a collapsible section by ID
function expandCollapsibleById(id) {
  const element = document.getElementById(id);
  
  if (element && (element.classList.contains('notification-banner') || 
                  element.classList.contains('table-banner'))) {
    const collapsibleContent = element.nextElementSibling;
    const arrow = element.querySelector(['.arrow', '.notification-arrow', '.table-arrow']);

    if (collapsibleContent && !collapsibleContent.classList.contains('open')) {
      collapsibleContent.classList.add('open');
      if (arrow) arrow.classList.add('rotate');
    }
    element.scrollIntoView({ behavior: 'smooth' });
  }
}

// Auto-expand all collapsible banners on page load
document.addEventListener('DOMContentLoaded', function () {
  const collapsibleContents = document.querySelectorAll(['.collapsible-content', '.table-open-collapsible-content']);
  const arrowIcons = document.querySelectorAll('.arrow');

  // Loop through all collapsible sections to open and rotate arrow
  collapsibleContents.forEach(content => content.classList.add('open'));
  arrowIcons.forEach(arrow => arrow.classList.add('rotate'));

  // Auto-expand specific banner if navigated via external link
  const hash = window.location.hash.substring(1);
  if (hash) {
    expandCollapsibleById(hash);
  }
});

// Listen for hash changes to expand collapsible sections
window.addEventListener('hashchange', () => {
  const hash = window.location.hash.substring(1);
  if (hash) {
    expandCollapsibleById(hash);
  }
});

// Click to copy 
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".copy-button").forEach(function (button) {
      button.addEventListener("click", function () {
          const textToCopy = this.previousElementSibling.textContent; // Get the text from the sibling element
          navigator.clipboard.writeText(textToCopy).then(
              () => {
                  button.textContent = "Copied!";
                  setTimeout(() => (button.textContent = "Copy"), 2000);
              },
              () => {
                  button.textContent = "Error";
              }
          );
      });
  });
});


// Expand all function for measures overview page 
document.addEventListener("DOMContentLoaded", function () {
  const toggleAllBtn = document.getElementById("toggle-all-btn");
  const banners = document.querySelectorAll(".table-banner");
  const sections = document.querySelectorAll(".table-collapsible-content");

  toggleAllBtn.addEventListener("click", function () {
      const allExpanded = Array.from(sections).every(sec => sec.classList.contains("open"));

      banners.forEach(banner => {
          if (allExpanded) {
              // If all are expanded, collapse them
              if (banner.nextElementSibling.classList.contains("open")) {
                  toggleCollapse(banner);
              }
          } else {
              // If not all are expanded, expand them
              if (!banner.nextElementSibling.classList.contains("open")) {
                  toggleCollapse(banner);
              }
          }
      });

      toggleAllBtn.textContent = allExpanded ? "Expand All Sections  ↕️" : "Collapse All Sections ↕️";
  });
});

