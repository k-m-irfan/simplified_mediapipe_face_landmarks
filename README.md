# simplified_mediapipe_face_landmarks
Extracts essential Mediapipe face landmarks and arranges them in a sequenced order.

The default 478 Mediapipe face landmarks are scattered randomly all over the place and makes it difficult to isolate specific parts of the face. This mpFaceSimplified.py library returns 138 landmarks of left eyebrow → right eyebrow → left eye → right eye → inner lip → outer lip → face boundary, in a sequence, making it easier to isolate these parts.

## Original Landmarks from Mediapipe face_mesh

  - **Left Eyebrow** = [70,63,105,66,107,55,65,52,53,46]
  - **Right Eyebrow** = [300,293,334,296,336,285,295,282,283,276]
  - **Left Eye** = [33,246,161,160,159,158,157,173,133,155,154,153,145,144,163,7]
  - **Right Eye** = [263,466,388,387,386,385,384,398,362,382,381,380,374,373,390,249]
  - **Inner Lip** = [78,191,80,81,82,13,312,311,310,415,308,324,318,402,317,14,87,178,88,95]
  - **Outer Lip** = [61,185,40,39,37,0,267,269,270,409,291,375,321,405,314,17,84,181,91,146]
  - **Face Boundary** = [10,338,297,332,284,251,389,356,454,323,361,288,397,365,379,378,400,377,152,148,176,149,150,136,172,58,132,93,234,127,162,21,54,103,67,109]
  - **Left iris** = [468,469,470,471,472]
  - **Right iris** = [473,474,475,476,477]
\
\
\
![originalLandmarks](https://user-images.githubusercontent.com/80172338/147330227-97fbf8bd-dd73-4d5d-b98b-3ac2489c1759.jpg)

## Simplified Landmarks after sequencing

  - **Left Eyebrow** = [0->9]
  - **right Eyebrow** = [10->19]
  - **Left Eye** = [20->35]
  - **Right Eye** = [36->51]
  - **Iner Lip** = [52->71]
  - **outer Lip** = [72->91]
  - **Face Boundary** = [92->127]
  - **Left iris** = [128->132]
  - **Right iris** = [133->137]
\
\
\
![simplifiedLandmarks](https://user-images.githubusercontent.com/80172338/147331993-067d58da-1b97-4caf-935c-35fb06aaad34.jpg)

**Keep 'mpFaceSimplified.py' and 'exampleProgram.py' in the same folder and then run 'exampleProgram.py' to try it out.**
