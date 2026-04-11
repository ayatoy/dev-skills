# Path Format

Keep the walkthrough short and serial.

## Default Shape

- Use 3 to 7 steps.
- Each step should say what to open, what it does, what to verify, and why it appears at that point in the path.
- Prefer behavior order over commit order or directory order.

## Good Reading Order

1. Entry point or user-visible surface.
2. Core logic or state transition.
3. Persistence or external side effects.
4. Tests or examples that confirm intent.
5. Low-risk supporting files.
