# RAD_MAMMO_LETTER_MGMT_R

> Links a Mammo Letter with the patient recommendation (Management) steps that relate to it.

**Description:** RadNet Mammography Letter Management Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FOLLOW_UP_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The recommendations to the patient based on the assessment done. |
| 2 | `LETTER_ID` | DOUBLE | NOT NULL | FK→ | The MAMMO_LETTER that this management information pertains to. |
| 3 | `RAD_MAMMO_LETTER_MGMT_R_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RAD_MAMMO_LETTER_MGMT_R table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FOLLOW_UP_FIELD_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `LETTER_ID` | [MAMMO_LETTER](MAMMO_LETTER.md) | `LETTER_ID` |

