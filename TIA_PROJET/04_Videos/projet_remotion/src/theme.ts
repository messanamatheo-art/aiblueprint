// Polices installées localement (Inter / Inter Display) : aucun téléchargement au rendu.

export const theme = {
  fps: 30,
  width: 1080,
  height: 1920,
  bg: "#04060D",
  bg2: "#0B1020",
  blue: "#3F8CFF",
  blue2: "#2F5FFF",
  text: "#EEF2FF",
  muted: "#9AA6C7",
  red: "#FF4B4B",
  display: "'Inter Display', Inter, sans-serif",
  body: "Inter, sans-serif",
  titleSize: 104,
  stagger: 4, // images entre deux éléments
  transition: 10, // durée des transitions (images)
};

// Durées du storyboard, en secondes (total 30,0 s)
export const durations = [2.0, 2.5, 2.0, 2.5, 2.5, 3.0, 3.0, 3.0, 3.0, 2.5, 2.0, 2.0];
export const sec = (s: number) => Math.round(s * theme.fps);
