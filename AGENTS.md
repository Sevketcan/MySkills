# Maintaining MySkills

Keep skills for non-obvious tool contracts, explicit personal/project preferences, or observed recurring failures. General tutorials alone do not justify a new discoverable entry point.

New entry points need an entry in skill-reviews.json: the reason, concrete evidence, one intended trigger, one nearby request that should not trigger it, and how the benefit will be checked. Existing entries are recorded as previously reviewed, not as empirically proven improvements.

Use skill-sources.json to keep one active source for overlapping workflows. Preserve local fixes and plugin-only capabilities; never edit plugin caches. Reapply scripts/configure-skill-sources.py after Unity plugin updates.

Project stack, deployment and appearance preferences belong in opt-in project profiles. Do not apply them to unrelated existing projects. Keep scripts parameterized, preserve caller state, and verify actual effects.

For changed Python/scripts, run the relevant unit tests plus scripts/validate_collection.py and scripts/build_manifest.py. Skill text edits need frontmatter and reference checks; do not add tests that only restate prose. Do not claim performance gains from catalog counts or mocked tools.
