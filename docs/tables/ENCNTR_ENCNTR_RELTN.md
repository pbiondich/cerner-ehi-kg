# ENCNTR_ENCNTR_RELTN

> Encounter to Encounter relationships

**Description:** Encounter Encounter Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ENCNTR_RELTN_ID` | DOUBLE | NOT NULL |  | Identifies a Encounter Encounter relationship |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter to whom an Encounter relationship exists. |
| 3 | `ENCNTR_RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Type of Encounter Relationship |
| 4 | `RELATED_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The "Related" Encounter to the relationship |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `RELATED_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

