import React from "react";
import { Composition } from "remotion";
import { TIATest } from "./Video";
import { theme, durations, sec } from "./theme";

const total = durations.reduce((a, b) => a + sec(b), 0); // 30,0 s exactement

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="TIATest" component={TIATest} durationInFrames={total} fps={theme.fps} width={1080} height={1920} />
  </>
);
