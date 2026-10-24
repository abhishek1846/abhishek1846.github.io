## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)

## Writing & Style Guidelines

- Never use emdash (—) or endash (–). Always use a standard hyphen (-).
- Never write long sentences with too many commas. Keep sentences clean and easy to follow.
- Never use 3-word phrase triplets or cliché copywriting triads.
- Write naturally like a human.
- Proactively suggest better approaches and push back when a design or technical decision is sub-optimal.

## Blog drafts

- Keep new blog drafts in `src/content/writing/` with `draft: true` and the required frontmatter. They must appear on the local dev server for review, including the writing list and article pages. Do not put blog drafts in the shared Obsidian Agent Workspace or a separate drafts directory.
- Include drafts during development only. Exclude them from production listings and generated article routes.
- Review and edit locally with Abhishek. Once approved, mark ready for publication and commit and push to main as authorized.
