import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "../theme";
import { Background, Words, Logo, Center, Card, clamp } from "./common";

const useSp = (delay = 0, damping = 200) => {
  const f = useCurrentFrame(); const { fps } = useVideoConfig();
  return spring({ frame: f - delay, fps, config: { damping } });
};

// Cercle lumineux du logo qui se dessine
const Ring: React.FC<{ progress: number; size: number }> = ({ progress, size }) => {
  const r = size / 2 - 10, c = 2 * Math.PI * r;
  return (
    <svg width={size} height={size} style={{ filter: "drop-shadow(0 0 24px rgba(63,140,255,0.8))" }}>
      <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#5fb0ff" /><stop offset="1" stopColor={theme.blue2} /></linearGradient></defs>
      <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="url(#g)" strokeWidth={10} strokeDasharray={c} strokeDashoffset={c * (1 - progress)} strokeLinecap="round" transform={`rotate(-90 ${size / 2} ${size / 2})`} />
    </svg>
  );
};

// 1 · Accroche
export const S1: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <Background>
      <Center gap={80}>
        <Ring progress={interpolate(f, [0, 40], [0, 1], clamp)} size={300} />
        <Words text="Tu veux apprendre le trading ?" highlight={["trading"]} />
      </Center>
    </Background>
  );
};

// 2 · Ce qu'on vend ailleurs
const Bubble: React.FC<{ text: string; delay: number }> = ({ text, delay }) => {
  const p = useSp(delay);
  return (
    <div style={{ alignSelf: "flex-end", transform: `translateX(${(1 - p) * 400}px)`, opacity: p, background: "#1b2440", borderRadius: "40px 40px 8px 40px", padding: "26px 36px", fontFamily: theme.body, fontWeight: 600, fontSize: 44, color: theme.text }}>{text}</div>
  );
};
export const S2: React.FC = () => (
  <Background glow={0.6}>
    <AbsoluteFill style={{ padding: "260px 90px", flexDirection: "column", gap: 70 }}>
      <Words text="Signaux. Promesses. Dépôt obligatoire." size={92} />
      <Card style={{ display: "flex", flexDirection: "column", gap: 26, padding: 40 }}>
        <div style={{ fontWeight: 700, fontSize: 34, color: theme.muted }}>VIP SIGNALS · exemple fictif</div>
        <Bubble text="🚀 Achète maintenant !" delay={12} />
        <Bubble text="+500 % garanti" delay={18} />
        <Bubble text="Dépose 250 € pour commencer" delay={24} />
      </Card>
    </AbsoluteFill>
  </Background>
);

// 3 · Stop
export const S3: React.FC = () => {
  const f = useCurrentFrame(); const wipe = interpolate(f, [0, 14], [0, 120], clamp); const p = useSp(10);
  return (
    <Background glow={0.4}>
      <AbsoluteFill style={{ background: `linear-gradient(115deg, ${theme.red} ${wipe - 20}%, transparent ${wipe}%)`, opacity: 0.85 }} />
      <Center>
        <div style={{ fontFamily: theme.display, fontWeight: 800, fontSize: 260, color: "#fff", transform: `scale(${1.1 - 0.1 * p})`, opacity: p }}>Stop.</div>
      </Center>
    </Background>
  );
};

// 4 · Logo TIA, puis zoom à travers le cercle
export const S4: React.FC = () => {
  const f = useCurrentFrame(); const { durationInFrames } = useVideoConfig(); const p = useSp(0);
  const through = interpolate(f, [durationInFrames - 18, durationInFrames], [1, 6], clamp);
  const fade = interpolate(f, [durationInFrames - 10, durationInFrames], [1, 0], clamp);
  return (
    <Background>
      <Center gap={70}>
        <div style={{ transform: `scale(${(0.7 + 0.3 * p) * through})`, opacity: fade }}><Logo size={420} /></div>
        <div style={{ opacity: fade }}><Words text="Voici Trading IA Academy." highlight={["Trading", "IA", "Academy."]} delay={8} size={92} /></div>
      </Center>
    </Background>
  );
};

// 5 · Méthode DÉCISION (cartes en cascade)
const LETTERS = ["D", "É", "C", "I", "S", "I", "O", "N"];
const Letters: React.FC<{ line?: number }> = ({ line = 0 }) => {
  const f = useCurrentFrame(); const { fps } = useVideoConfig();
  return (
    <div style={{ position: "relative", display: "flex", gap: 18 }}>
      <div style={{ position: "absolute", left: 50, top: 60, height: 6, width: `${line * 900}px`, background: `linear-gradient(90deg, ${theme.blue}, ${theme.blue2})`, boxShadow: "0 0 20px rgba(63,140,255,0.9)" }} />
      {LETTERS.map((l, i) => {
        const p = spring({ frame: f - i * 3, fps, config: { damping: 200 } });
        return <div key={i} style={{ width: 100, height: 120, borderRadius: 22, background: "linear-gradient(160deg,#1b3a8f,#0b1020)", border: "2px solid rgba(63,140,255,0.7)", display: "grid", placeItems: "center", fontFamily: theme.display, fontWeight: 800, fontSize: 64, color: "#fff", opacity: p, transform: `translateY(${(1 - p) * 80}px)`, position: "relative" }}>{l}</div>;
      })}
    </div>
  );
};
export const S5: React.FC = () => (
  <Background>
    <Center gap={90}>
      <Words text="La Méthode DÉCISION" highlight={["DÉCISION"]} />
      <Letters />
    </Center>
  </Background>
);

// 6 · 8 étapes, ligne lumineuse
export const S6: React.FC = () => {
  const f = useCurrentFrame(); const { durationInFrames } = useVideoConfig();
  const pan = interpolate(f, [0, durationInFrames], [40, -40], clamp);
  return (
    <Background>
      <Center gap={90}>
        <div style={{ transform: `translateX(${pan}px)` }}><Letters line={interpolate(f, [0, 50], [0, 1], clamp)} /></div>
        <Words text="8 étapes. Toujours le même ordre." size={88} delay={6} />
      </Center>
    </Background>
  );
};

// 7 · Respiration : prompt qui se tape
export const S7: React.FC = () => {
  const f = useCurrentFrame(); const t = "Critique mon plan de trade";
  const n = Math.floor(interpolate(f, [6, 50], [0, t.length], clamp));
  return (
    <Background glow={0.7}>
      <Center gap={90}>
        <Card style={{ width: 880, fontSize: 42, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <span>{t.slice(0, n)}<span style={{ opacity: Math.floor(f / 8) % 2 ? 1 : 0, color: theme.blue }}>|</span></span>
          <span style={{ width: 70, height: 70, borderRadius: 20, background: theme.blue2, display: "grid", placeItems: "center", fontSize: 40 }}>↑</span>
        </Card>
        <Words text="L'IA prépare. Toi, tu décides." highlight={["décides."]} delay={30} size={96} />
      </Center>
    </Background>
  );
};

// 8 · Carte risque inclinée en 3D + compteur
export const S8: React.FC = () => {
  const f = useCurrentFrame(); const p = useSp(0);
  const val = Math.round(interpolate(f, [10, 55], [0, 100], clamp));
  return (
    <Background>
      <Center gap={80}>
        <Words text="Ton risque, calculé avant d'entrer." size={90} />
        <div style={{ perspective: 1600 }}>
          <Card style={{ width: 820, transform: `rotateY(${(1 - p) * -35 + interpolate(f, [0, 90], [-8, 4], clamp)}deg) rotateX(6deg)` }}>
            <div style={{ fontSize: 32, color: theme.muted, fontWeight: 700 }}>PLAN DE RISQUE · exemple fictif</div>
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 40, marginTop: 24 }}><span>Capital</span><b>10 000 €</b></div>
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 40, marginTop: 14 }}><span>Risque</span><b>1 %</b></div>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginTop: 26 }}><span style={{ fontSize: 40 }}>1 R</span><b style={{ fontFamily: theme.display, fontSize: 110, color: theme.blue }}>{val} €</b></div>
          </Card>
        </div>
      </Center>
    </Background>
  );
};

// 9 · Mur de cartes en profondeur
const TAGS = ["Brief de séance", "Plan si/alors", "Taille de position", "Avant un trade", "Après une perte", "Revue hebdo", "Multi-timeframe", "Journal", "Avocat du diable", "Fin de journée", "Biais FOMO", "Revue mensuelle"];
export const S9: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <Background>
      <AbsoluteFill style={{ perspective: 1400 }}>
        {TAGS.map((t, i) => {
          const row = i % 4, col = Math.floor(i / 4);
          const x = -260 + col * 420 - f * (3 + row), y = 260 + row * 240;
          return <div key={i} style={{ position: "absolute", left: x + 300, top: y, transform: `translateZ(${-row * 120}px)`, opacity: 0.55 + (row % 2) * 0.35 }}><Card style={{ padding: "22px 30px", fontSize: 34, fontWeight: 700, whiteSpace: "nowrap" }}>{i % 2 ? "☑ " : "✦ "}{t}</Card></div>;
        })}
      </AbsoluteFill>
      <AbsoluteFill style={{ justifyContent: "flex-end", paddingBottom: 380 }}><Words text="100 prompts · 20 checklists" size={100} highlight={["100", "20"]} /></AbsoluteFill>
    </Background>
  );
};

// 10 · Excel + Notion en 3D
const Win: React.FC<{ title: string; side: number; delay: number }> = ({ title, side, delay }) => {
  const p = useSp(delay);
  return (
    <div style={{ perspective: 1400 }}>
      <Card style={{ width: 430, height: 520, transform: `translateX(${side * (1 - p) * 500}px) rotateY(${side * -22}deg)`, opacity: p }}>
        <div style={{ fontWeight: 700, fontSize: 36, marginBottom: 24 }}>{title}</div>
        {[0, 1, 2, 3, 4, 5].map((k) => <div key={k} style={{ height: 34, borderRadius: 10, marginBottom: 18, background: k % 2 ? "rgba(63,140,255,0.35)" : "rgba(255,255,255,0.08)", width: `${90 - k * 8}%` }} />)}
      </Card>
    </div>
  );
};
export const S10: React.FC = () => (
  <Background>
    <Center gap={90}>
      <div style={{ display: "flex", gap: 40 }}><Win title="Classeur Excel" side={-1} delay={0} /><Win title="Espace Notion" side={1} delay={6} /></div>
      <Words text="Excel et Notion inclus." size={96} delay={8} />
    </Center>
  </Background>
);

// 11 · Deux coches
const Check: React.FC<{ label: string; delay: number }> = ({ label, delay }) => {
  const f = useCurrentFrame(); const d = interpolate(f, [delay, delay + 14], [60, 0], clamp); const p = useSp(delay);
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 40, opacity: p }}>
      <svg width={130} height={130}><circle cx={65} cy={65} r={60} fill={theme.blue2} /><path d="M38 66 L57 85 L93 47" fill="none" stroke="#fff" strokeWidth={12} strokeLinecap="round" strokeLinejoin="round" strokeDasharray={60} strokeDashoffset={d} /></svg>
      <span style={{ fontFamily: theme.display, fontWeight: 800, fontSize: 96, color: theme.text }}>{label}</span>
    </div>
  );
};
export const S11: React.FC = () => (
  <Background>
    <Center gap={80}><Check label="Sans promesse." delay={0} /><Check label="Sans dépôt." delay={14} /></Center>
  </Background>
);

// 12 · Fin
export const S12: React.FC = () => {
  const f = useCurrentFrame(); const p = useSp(0); const p2 = useSp(14);
  const breathe = 1 + Math.sin(f / 8) * 0.03;
  return (
    <Background glow={1.3}>
      <Center gap={70}>
        <div style={{ transform: `scale(${(0.8 + 0.2 * p) * breathe})`, opacity: p }}><Logo size={380} /></div>
        <div style={{ fontFamily: theme.display, fontWeight: 800, fontSize: 84, color: theme.text, opacity: p }}>Trading IA Academy</div>
        <div style={{ opacity: p2, transform: `translateY(${(1 - p2) * 40}px)`, background: `linear-gradient(135deg, ${theme.blue}, ${theme.blue2})`, borderRadius: 999, padding: "28px 70px", fontFamily: theme.body, fontWeight: 700, fontSize: 56, color: "#fff", boxShadow: "0 20px 60px rgba(47,95,255,0.5)" }}>Lien en bio</div>
      </Center>
    </Background>
  );
};

export const SCENES = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12];
