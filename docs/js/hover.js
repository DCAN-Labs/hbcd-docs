<script>
document.addEventListener('DOMContentLoaded', function() {
    const tooltips = document.querySelectorAll('.tooltip');

    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseover', function() {
            const tooltipText = tooltip.querySelector('.tooltiptext');
            const rect = tooltip.getBoundingClientRect();
            const viewportWidth = window.innerWidth;
            const tooltipWidth = tooltipText.offsetWidth;
            
            // Check if tooltip goes off the right side
            if (rect.left + tooltipWidth > viewportWidth) {
                // If it does, position the tooltip to the left
                tooltipText.style.left = 'auto';
                tooltipText.style.right = '0';
                tooltipText.style.transform = 'translateX(0)';
            } else {
                // Otherwise, keep the tooltip centered
                tooltipText.style.left = '50%';
                tooltipText.style.right = 'auto';
                tooltipText.style.transform = 'translateX(-50%)';
            }
        });
    });
});
</script>
