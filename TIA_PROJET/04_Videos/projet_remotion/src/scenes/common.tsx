import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig, Img, staticFile } from "remotion";
import { theme } from "../theme";

export const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

// Fond : dégradé sombre + halo bleu qui dérive + zoom continu (jamais d'image figée)
export const Background: React.FC<{ children: React.ReactNode; glow?: number }> = ({ children, glow = 1 }) => {
  const f = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const zoom = interpolate(f, [0, durationInFrames], [1, 1.06], clamp);
  const gx = 50 + Math.sin(f / 40) * 12, gy = 42 + Math.cos(f / 55) * 8;
  return (
    <AbsoluteFill style={{ background: theme.bg, overflow: "hidden" }}>
      <AbsoluteFill style={{ background: `radial-gradient(circle at ${gx}% ${gy}%, rgba(47,95,255,${0.32 * glow}) 0%, rgba(4,6,13,0) 55%)` }} />
      <Particles />
      <AbsoluteFill style={{ transform: `scale(${zoom})` }}>{children}</AbsoluteFill>
    </AbsoluteFill>
  );
};

// Particules floues qui montent lentement (parallaxe)
const DOTS = Array.from({ length: 18 }, (_, i) => ({ x: (i * 137) % 100, y: (i * 61) % 100, r: 4 + (i % 5) * 3, s: 0.15 + (i % 4) * 0.12 }));
const Particles: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill>
      {DOTS.map((d, i) => (
        <div key={i} style={{ position: "absolute", left: `${d.x}%`, top: `${(d.y - f * d.s * 0.12 + 200) % 110 - 5}%`, width: d.r * 2, height: d.r * 2, borderRadius: "50%", background: theme.blue, opacity: 0.18 + (i % 3) * 0.08, filter: `blur(${2 + (i % 3) * 3}px)` }} />
      ))}
    </AbsoluteFill>
  );
};

// Texte qui monte mot par mot (décalage de 3 à 6 images)
export const Words: React.FC<{ text: string; size?: number; color?: string; delay?: number; weight?: number; highlight?: string[] }> = ({ text, size = theme.titleSize, color = theme.text, delay = 0, weight = 800, highlight = [] }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", gap: `0 ${size * 0.28}px`, padding: "0 70px", textAlign: "center" }}>
      {text.split(" ").map((w, i) => {
        const p = spring({ frame: f - delay - i * theme.stagger, fps, config: { damping: 200 } });
        return (
          <span key={i} style={{ display: "inline-block", fontFamily: theme.display, fontWeight: weight, fontSize: size, lineHeight: 1.08, letterSpacing: "-0.02em", color: highlight.includes(w) ? theme.blue : color, opacity: p, transform: `translateY(${(1 - p) * 60}px)`, filter: `blur(${(1 - p) * 10}px)` }}>{w}</span>
        );
      })}
    </div>
  );
};

export const Logo: React.FC<{ size: number; opacity?: number }> = ({ size, opacity = 1 }) => (
  <Img src={staticFile("logo.png")} style={{ width: size, height: size, borderRadius: "50%", opacity }} />
);

export const Center: React.FC<{ children: React.ReactNode; gap?: number }> = ({ children, gap = 60 }) => (
  <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", flexDirection: "column", gap }}>{children}</AbsoluteFill>
);

export const Card: React.FC<{ children: React.ReactNode; style?: React.CSSProperties }> = ({ children, style }) => (
  <div style={{ background: "rgba(11,16,32,0.92)", border: "2px solid rgba(63,140,255,0.45)", borderRadius: 36, padding: "36px 44px", boxShadow: "0 30px 90px rgba(47,95,255,0.25)", fontFamily: theme.body, color: theme.text, ...style }}>{children}</div>
);
