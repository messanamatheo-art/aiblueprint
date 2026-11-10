import React from "react";
import { AbsoluteFill, Audio, staticFile } from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { wipe } from "@remotion/transitions/wipe";
import { SCENES } from "./scenes/Scenes";
import { theme, durations, sec } from "./theme";

// Transitions variées (glissement, volet, fondu) ; la scène 4 -> 5 est un zoom à travers le logo, fait dans la scène 4.
// eslint-disable-next-line @typescript-eslint/no-explicit-any
const TRANS: any[] = [
  slide({ direction: "from-right" }), wipe({ direction: "from-left" }), fade(), fade(), slide({ direction: "from-bottom" }),
  wipe({ direction: "from-top-left" }), slide({ direction: "from-left" }), wipe({ direction: "from-right" }), slide({ direction: "from-bottom" }), fade(), fade(),
];

export const TIATest: React.FC = () => {
  const T = theme.transition;
  return (
    <AbsoluteFill style={{ background: theme.bg }}>
      <TransitionSeries>
        {SCENES.map((Scene, i) => (
          <React.Fragment key={i}>
            {/* chaque scène (sauf la dernière) est allongée de la durée de la transition : le total reste à 30 s */}
            <TransitionSeries.Sequence durationInFrames={sec(durations[i]) + (i < SCENES.length - 1 ? T : 0)}>
              <Scene />
            </TransitionSeries.Sequence>
            {i < SCENES.length - 1 && <TransitionSeries.Transition presentation={TRANS[i]} timing={linearTiming({ durationInFrames: T })} />}
          </React.Fragment>
        ))}
      </TransitionSeries>
      <Audio src={staticFile("audio.wav")} />
    </AbsoluteFill>
  );
};
