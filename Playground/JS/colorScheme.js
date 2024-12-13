// Function to retrieve CSS variables from the :root element
const getCSSVariable = (varName) => {
    return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
}

// Access colors from colorPalette.css
const colors = {
    black: getCSSVariable('--black'),
    red: getCSSVariable('--red'),
    cyan: getCSSVariable('--cyan'),
    // Add other colors as needed
};

// Define relational colors
const colorScheme = {
    dominant: colors.red,           // Example using the red color from the palette
    surface: getCSSVariable('--lightGrey'), // Surface color could be a light grey
    accent: colors.cyan             // Accent color using the cyan from the palette
};

// Example usage: Apply these colors to the document or elements
document.body.style.backgroundColor = colorScheme.surface;
document.body.style.color = colorScheme.dominant;

console.log(colorScheme);
