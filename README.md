# simplified_mediapipe_face_landmarks
Extracts essential Mediapipe face landmarks and arranges them in a sequenced order.

The default Mediapipe face landmarks are scattered randomly all over the place and makes it difficult to isolate specific parts of the face. The mpFaceSimplified.py library returns landmarks of left eyebrow → right eyebrow → left eye → right eye → inner lip → outer lip → face boundary, in a sequence, making it easier to isolate these parts.
