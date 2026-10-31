# Foldable and large screens (iPhone Duo)

iPhone Duo has a narrow, short closed screen and a wide open screen; prepare for both. If an iPad layout already exists, the work is short (K13).

Lines marked **Implementation note** are not from the sources; they show how to apply the rule with Flutter or RevenueCat Paywalls.

## Steps

1. **Test the states.** Open the app on the Duo simulator closed, open and rotated (K13).
2. **Navigation.** If the tab bar wastes space or breaks on the wide screen, consider the system navigation component or a layout that adapts to the width instead of a custom-drawn tab bar (K14).
   - **Implementation note (Flutter):** Flutter draws its whole UI itself; `NavigationBar` is not iOS's native tab bar. Use `LayoutBuilder` to switch to `NavigationRail` on wide screens.
3. **Paywall and forms.** Cap the width, and keep critical content visible without scrolling on the closed screen (K15). RevenueCat's guide gives the figures: content at most ~600pt, the purchase button ~400pt, centred; price and button visible on the closed screen; the close button is a system control, inside the safe area and accessible.
   - **Implementation note (Flutter):** `Center(child: ConstrainedBox(constraints: BoxConstraints(maxWidth: 600), child: ...))`, and `maxWidth: 400` for the button.
   - **Implementation note (RevenueCat Paywalls, `purchases_ui_flutter`):** set the content and the button to "Fill" with a max width, and turn on "Use system navigation" for the close button. Min/max width needs iOS SDK 5.93.0+ and multi-step paywalls need 5.83.0+; check the Flutter package's equivalent on RevenueCat's SDK requirements page.
4. **Check list** (from RevenueCat's guide) (K15):
   - Do titles and text wrap instead of being cut off?
   - On the open screen, are buttons and text comfortable to read?
   - Does a fixed footer leave room for the other content?
   - Are close, back, continue and purchase visible in every state?
   - Does every step of a multi-step flow work?
5. **Store screenshots.** Produce Duo screenshots for the store page too.
