# Special Cases

Special Cases are living evidence records for complex Tracker subjects that cannot be represented accurately as a single dated event.

They are appropriate when multiple individually sourced laws, court decisions, government systems, agency actions, contracts, policies, datasets, or implementation changes must be considered together to understand a Tennessee digital-rights issue.

Special Cases do not lower the Tracker's evidence standards. The normal research protocol, methodology, editorial policy, privacy rules, and publication-readiness requirements continue to apply.

## When to use a Special Case

Use a Special Case only when all of the following are true:

- the subject has a meaningful Tennessee nexus;
- the subject materially involves technology, data, records, identity systems, digital infrastructure, surveillance, automated decision-making, civic-information infrastructure, or closely related digital rights;
- no single event date or primary source adequately represents the investigation;
- multiple independently sourced developments are necessary to understand the issue; and
- at least one ordinary published Tracker entry can be linked to the case.

Do not use a Special Case merely because a subject is politically important, controversial, national, fast-moving, or personally concerning.

## Tennessee nexus labels

Every material development in a Special Case should be classified using one of these labels.

### Direct

The development directly involves Tennessee, a Tennessee state or local entity, Tennessee residents as an identified target population, Tennessee-specific data or infrastructure, or a documented Tennessee implementation.

### Conditional

The development is federal, interstate, or otherwise external to Tennessee but would materially apply to Tennessee if a stated legal, technical, or operational condition occurs.

### Context

The development does not itself establish a Tennessee implementation or effect, but it is necessary to understand the architecture, authority, chronology, or institutions involved in a directly or conditionally Tennessee-connected issue.

Context-only developments must not be used to create the appearance of a Tennessee connection that the evidence does not establish.

## Relationship labels

When explaining how developments connect, use language that distinguishes the strength of the evidence.

### Documented connection

A primary or strong official source directly establishes the relationship between the developments, systems, agencies, or data flows.

### Supported relationship

The relationship is a reasonable evidence-backed synthesis, but no single source fully states it in the same terms.

### Possible relationship / not established

Timing, institutional proximity, shared policy goals, or other facts make a relationship relevant to investigate, but the available evidence does not establish causation, coordination, motive, or a direct operational connection.

Temporal sequence alone is not evidence of causation.

## Required public sections

Every published Special Case must contain:

- Case scope
- Tennessee nexus
- Current status
- Documented timeline
- How the pieces connect
- What is confirmed?
- What is not established?
- What remains uncertain?
- Digital-rights significance
- Update triggers
- Lawful actions and resources
- Sources
- Revision history

The `What is not established?` section is mandatory. It should identify important allegations, causal claims, motive claims, predicted effects, or public assumptions that the evidence does not currently support.

## Related Tracker entries

Ordinary entries connect to a Special Case through the optional front-matter field:

```yaml
special_case_id: "example-special-case"
```

The value must match the published Special Case's `case_id` exactly.

A published Special Case must have at least one related published entry. The Special Case should synthesize those entries and broader necessary context rather than duplicate their full prose.

## Research record

Substantive Special Case work should maintain a persistent research dossier under `research/`, normally using the existing research-notes structure plus an event ledger and connection matrix.

For each material event, record at minimum:

- date;
- actor or responsible institution;
- atomic claim;
- evidence status;
- Tennessee nexus label;
- strongest source;
- current status; and
- unresolved questions.

For proposed relationships between events or systems, record whether the connection is documented, supported, or not established.

## Publication threshold

A Special Case may be published when:

- the Tennessee nexus is supported by evidence;
- the core chronology is reproducible;
- at least one related ordinary Tracker entry is already publication-ready and linked;
- important contradictory evidence is preserved;
- material unknowns are visible;
- the current status is reasonably supported;
- claims of coordination, motive, causation, or effect do not exceed the evidence; and
- the case passes the repository validator.

Special Cases remain subject to update as new evidence changes the chronology, connections, legal status, or Tennessee implementation.
