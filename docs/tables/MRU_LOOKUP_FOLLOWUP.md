# MRU_LOOKUP_FOLLOWUP

> Provides the MRU framework with a unique identifier for follow-up visits.

**Description:** MRU Lookup Follow-up  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | %followup% |
| 2 | `CODED_FOLLOWUP_INTERVAL_CD` | DOUBLE | NOT NULL |  | Code value of a coded range for the follow-up time |
| 3 | `FOLLOWUP_DT_TM` | DATETIME |  |  | Date offset till the follow-up date |
| 4 | `FOLLOWUP_INTERVAL` | DOUBLE | NOT NULL |  | Numeric offset till the follow-up (within) date. |
| 5 | `FOLLOWUP_INTERVAL_UNITS_FLAG` | DOUBLE | NOT NULL |  | Indicates the units for the follow-up interval (0 for days, 1 for weeks). |
| 6 | `FOLLOWUP_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the follow-up type (clinic, provider, specialty). |
| 7 | `MRU_LOOKUP_FOLLOWUP_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID of a parent entity value |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the parent entity for which data represents |
| 10 | `PHONE_ID` | DOUBLE | NOT NULL | FK→ | %followup% |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |

