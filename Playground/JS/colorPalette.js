const colorPalette = {
    black: "#000000",
    slate: "#404040",
    grey: "#808080",
    silver: "#C0C0C0",
    white: "#ffffff",

    auburn: "#000000", taupe: "#a9a48e", brown: "#a52a2a", beige: "#F5F5DC",
    umber: "#8B4513", sienna: "#A0522D", sepia: "#5E2612",

    maroon: "#800000", brick: "#C04040", red: "#ff0000", pink: "#FF8080",
    gold: "#808000", khaki: "#C0C040", yellow: "#FFFF00", banana: "#FFFF80",
    viridian: "#008000", celadon: "#40C040", green: "#00FF00", lightGreen: "#80FF80",
    teal: "#008080", seafoam: "#40C0C0", cyan: "#00FFFF", electric: "#80ffff",
    navy: "#000080", cadet: "#4040c0", blue: "#0000FF", lightBlue: "#8080FF",
    plum: "#800080", grape: "#C040C0", magenta: "#FF00FF", hotPink: "#FF80FF",

    hazel: "#804000", goldenrod: "#C08040", orange: "#FF8000", coral: "#FFC080",
    martian: "#408000", jasmine: "#80C040", chartreuse: "#80FF00", avocado: "#C0FF80",
    jungle: "#008040", ming: "#40C080", spring: "#00FF80", verdigris: "#80FFC0",
    midnight: "#004080", tuft: "#4080C0", azure: "#0080FF", celeste: "#80C0FF",
    periwinkle: "#400080", harley: "#8040C0", violet: "#8000FF", mauve: "#C080FF",
    wine: "#800040", dazzle: "#C04080", rose: "#FF0080", rouge: "#FF80C0",

    cinnabar: "#802200", ochre: "#C06240", vermilion: "#FF4400", salmon: "#FFA280",
    earth: "#806200", wheat: "#C0A240", amber: "#FFC300", honey: "#FFE180",
    olive: "#608000", tropical: "#A2C040", lime: "#C3FF00", mystic: "#E1FF80",
    pepper: "#228000", sour: "#62C040", harlequin: "#44FF00", radar: "#A2FF80",
    verdant: "#008022", turf: "#40C062", erin: "#00FF44", menthol: "#80FFA2",
    abyssal: "#008060", jade: "#40C0A2", aquamarine: "#00FFC3", lagoon: "#80FFE1",
    adriatic: "#006080", norse: "#40A2C0", capri: "#00C3FF", lightCapri: "#80E1FF",
    darkCerulean: "#002280", speech: "#4062C0", cerulean: "#0044FF", pool: "#80A2FF",
    darkIndigo: "#220080", dragonlord: "#6240C0", indigo: "#4400FF", lilac: "#A280FF",
    gloam: "#600080", pheromone: "#A240C0", purple: "#C300FF", orchid: "#E180FF",
    xereus: "#800060", nusp: "#C040A2", cerise: "#FF00C3", grenadine: "#FF80E1",
    oxBlood: "#800022", ruby: "#C04062", crimson: "#FF0044", blush: "#FF80A2",

    scarlet: "#FF2000",
    persimmon: "#FF6000",
    orangePeel: "#FFA000",
    goldenYellow: "#FFE000",
    lemon: "#E0FF00",
    springBud: "#A0FF00",
    brightGreen: "#60FF00",
    neon: "#20FF00",
    jade: "#00FF20",
    emerald: "#00FF60",
    mint: "#00FFA0",
    turquoise: "#00FFE0",
    sky: "#00E0FF",
    cornflower: "#00A0FF",
    cobalt: "#0060FF",
    sapphire: "#0020FF",
    iris: "#2000FF",
    veronica: "#8000FF",
    amethyst: "#A000FF",
    phlox: "#E000FF",
    fuchsia: "#FF00E0",
    deepPink: "#FF00A0",
    raspberry: "#FF0060",
    amaranth: "#FF0020",

    automatic: "#333",
    offwhite: "#f0f0f0",
    light: "#f8f9fa",
    dark: "#343a40",
    primary: "#007bff",
    secondary: "#6c757d",
    info: "#17a2b8",
    visited: "#551A8B",
    success: "#28a745",
    warning: "#ffc107",
    danger: "#dc3545",

    darkGrey: "#404040",
    lightGrey: "#C0C0C0",

    darkBrown: "#000000", mutedBrown: "#a9a48e", lightBrown: "#F5F5DC",

    darkRed: "#800000", mutedRed: "#C04040", lightRed: "#FF8080",
    darkYellow: "#808000", mutedYellow: "#C0C040", lightYellow: "#FFFF80",
    darkGreen: "#008000", mutedGreen: "#40C040", lightGreen: "#80FF80",
    darkCyan: "#008080", mutedCyan: "#40C0C0", lightCyan: "#80ffff",
    darkBlue: "#000080", mutedBlue: "#4040c0", lightBlue: "#8080FF",
    darkMagenta: "#800080", mutedMagenta: "#C040C0", lightMagenta: "#FF80FF"
};

function injectColorVariables() {
    let css = ':root {';
    for (const [key, value] of Object.entries(colorPalette)) {
        css += `--${key}: ${value};`;
    }
    css += '}';

    const style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);
}

injectColorVariables();

export default colorPalette;