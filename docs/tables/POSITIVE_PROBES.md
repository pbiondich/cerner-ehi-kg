# POSITIVE_PROBES

> Indicates which probes in an HLA molecular testing blot require a positive reaction to conclude that a particular HLA allele or specificity is present.

**Description:** Positive Probes  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLELE_CD` | DOUBLE | NOT NULL | FK→ | The code for the allele which this Molecular Blot tests for that requires or a positive reaction for this probe. |
| 2 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Relates the Molecular Blot positive probes to the inventory lot and related blot. It is a foreign key reference to the primary key of the lot_number_info table. |
| 3 | `PROBE_NUMBER` | DOUBLE | NOT NULL |  | The number of the probe on the Molecular Blot which is being defined as positive for this allele. |
| 4 | `REACTION_SYMBOL_CD` | DOUBLE | NOT NULL |  | The code for the reaction symbol used to indicate the probes requires or may have a positive reaction to indicate the presence of the related allele. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALLELE_CD` | [BLOT_SPECIFICITY](BLOT_SPECIFICITY.md) | `ALLELE_CD` |
| `LOT_NUMBER_ID` | [BLOT_SPECIFICITY](BLOT_SPECIFICITY.md) | `LOT_NUMBER_ID` |

