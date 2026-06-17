# SCH_DATA_COMMENT

> schedule data comment

**Description:** schedule data comment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the address row is related (i.e., person_id, organization_id, etc.) |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this address row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 5 | `SCH_DATA_COMMENT_ID` | DOUBLE | NOT NULL |  | schedule data comment identifier |
| 6 | `SUB_TEXT_CD` | DOUBLE | NOT NULL |  | The coded identifier for the scheduling sub text type. The sub text types allow for multiple set of text within a text type (prep, post, guidelines, etc.) |
| 7 | `TEXT_ID` | DOUBLE | NOT NULL | FK→ | text identifier |
| 8 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL |  | text type code |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

