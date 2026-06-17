# ESO_FILTER_COND_RELTN

> eso filter cond relation Table

**Description:** eso filter cond relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date that the record was created in the table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXCLUDE_IND` | DOUBLE | NOT NULL |  | Indicates whether this result is included or excluded from the calculation of the Mean and Standard Deviation. A value of 0 indicates the result should be included in the calculation. A value of 1 indicates the result should be excluded from the calculation. |
| 6 | `FIELD_FILTER_RELTN_ID` | DOUBLE | NOT NULL | FK→ | field filter relation identifierColumn |
| 7 | `FILTER_COND_ID` | DOUBLE | NOT NULL | FK→ | filter condition identifierColumn |
| 8 | `FILTER_COND_RELTN_ID` | DOUBLE | NOT NULL |  | filter cond relation identifierColumn |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_FILTER_RELTN_ID` | [ESO_FIELD_FILTER_RELTN](ESO_FIELD_FILTER_RELTN.md) | `FIELD_FILTER_RELTN_ID` |
| `FILTER_COND_ID` | [ESO_FILTER_COND](ESO_FILTER_COND.md) | `FILTER_COND_ID` |

