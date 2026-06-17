# DSM_COMPONENT

> DSM-IV Components

**Description:** DSM-IV Components desc  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AXIS_FLAG` | DOUBLE |  |  | Axis the assessment is being performed on (1-5) |
| 2 | `COMPONENT_DESC1` | VARCHAR(255) |  |  | Primary component description field |
| 3 | `COMPONENT_DESC2` | VARCHAR(255) |  |  | Secondary component description field |
| 4 | `COMPONENT_SEQ` | DOUBLE |  |  | User defined sequencing for order of precedence and component display purposes. |
| 5 | `DSM_ASSESSMENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the overall assessment |
| 6 | `DSM_COMPONENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the individual assessment component |
| 7 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | The DSM-IV or ICD-9 unique identifier |
| 8 | `PRIMARY_DIAG_IND` | DOUBLE |  |  | Indicates whether the component is the primary component for its particular axis. Override component_seq order of precedence |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DSM_ASSESSMENT_ID` | [DSM_ASSESSMENT](DSM_ASSESSMENT.md) | `DSM_ASSESSMENT_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

