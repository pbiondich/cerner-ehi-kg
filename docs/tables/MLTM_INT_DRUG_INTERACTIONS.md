# MLTM_INT_DRUG_INTERACTIONS

> This table contains essential information about drug interactions, including codes for each of the drugs that participate in a specific interaction, a severity code, and a code representing specific text describing the interaction. Each interaction is described only once in the table, so interaction checking must also occur in the reverse order.

**Description:** Multum drug Interactions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRUG_IDENTIFIER_1` | VARCHAR(6) | NOT NULL | FK→ | This field contains Multum's identification codes for generic drugs. |
| 2 | `DRUG_IDENTIFIER_2` | VARCHAR(6) | NOT NULL | FK→ | This field contains Multum's identification codes for generic drugs. |
| 3 | `INT_ID` | DOUBLE | NOT NULL | FK→ | FK from the interaction description table |
| 4 | `SEVERITY_ID` | DOUBLE | NOT NULL |  | FK from the Multum severity table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_IDENTIFIER_1` | [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_IDENTIFIER` |
| `DRUG_IDENTIFIER_2` | [MLTM_DRUG_ID](MLTM_DRUG_ID.md) | `DRUG_IDENTIFIER` |
| `INT_ID` | [MLTM_INTERACTION_DESCRIPTION](MLTM_INTERACTION_DESCRIPTION.md) | `INT_ID` |

