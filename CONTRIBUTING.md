# Contributing

Thank you for helping improve the tracker.

## Before opening an issue

- Search existing entries, Special Cases, and issues
- Find the strongest available primary source
- For surveillance research, search the [Atlas of Surveillance](https://www.atlasofsurveillance.org/search), preserve relevant record links, and follow its citations to the underlying sources
- Check whether the technology or policy is still current rather than relying only on an older discovery record
- Remove personal and sensitive information
- Separate what you know from what you suspect

Atlas of Surveillance is an approved discovery source, not automatic proof of current deployment, configuration, policy, or data-sharing practices. Promising Atlas leads should be independently verified and opened as separate research issues before publication.

Automated `discovery` issues opened by the Tennessee Rights Scout are research leads, not publication-ready entries. Search those issues too, inspect the underlying source, and follow the research protocol before drafting an entry.

## Entry requirements

A publishable entry needs:

- A clear title
- Event date
- Last-reviewed date
- Primary category
- Status
- Confidence label
- At least one primary source
- Confirmed facts
- Uncertainties
- Affected groups
- Lawful action options
- Revision history

## Special Case requirements

A Special Case is for a complex, multi-event investigation that cannot be represented accurately as one dated entry.

Before publication, a Special Case must:

- have a meaningful Tennessee nexus;
- follow `docs/special-cases.md`;
- maintain a persistent research record under `research/` for substantive investigations;
- distinguish Direct, Conditional, and Context Tennessee connections;
- distinguish documented connections from supported or unestablished relationships;
- include a section stating what the evidence does not establish;
- link to at least one ordinary published Tracker entry using `special_case_id`;
- satisfy the Special Case schema and validator; and
- remain within the Tracker's technology, data, digital-rights, privacy, surveillance, civic-information, or election-infrastructure scope.

Political importance, controversy, or national attention alone is not enough to justify a Special Case.

## Pull-request checklist

- [ ] I used primary sources where available.
- [ ] I treated discovery databases, including Atlas of Surveillance, as research leads unless independently verified.
- [ ] I attributed interpretations.
- [ ] I labeled uncertainty.
- [ ] I avoided stating motive as fact.
- [ ] I did not include sensitive personal information.
- [ ] I did not claim anonymity or guaranteed safety.
- [ ] If this changes a Special Case, I followed `docs/special-cases.md` and verified related-entry links.
- [ ] I ran the validation script.
