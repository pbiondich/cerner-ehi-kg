# ESO_FIELD_FILTER_RELTN

> eso field filter relation Table

**Description:** eso field filter relation  
**Table type:** REFERENCE  
**Primary key:** `FIELD_FILTER_RELTN_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the record was created |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXCLUDE_IND` | DOUBLE | NOT NULL |  | Indicates whether this result is included or excluded from the calculation of the Mean and Standard Deviation. A value of 0 indicates the result should be included in the calculation. A value of 1 indicates the result should be excluded from the calculation. |
| 6 | `FIELD_FILTER_RELTN_ID` | DOUBLE | NOT NULL | PK | field filter relation identifierColumn |
| 7 | `FIELD_TRANS_ID` | DOUBLE | NOT NULL | FK→ | field filter identifierColumn |
| 8 | `FILTER_ID` | DOUBLE | NOT NULL | FK→ | filter identifierColumn |
| 9 | `RELTN_SEQ` | DOUBLE | NOT NULL |  | relation sequenceColumn |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_TRANS_ID` | [ESO_FIELD_TRANS](ESO_FIELD_TRANS.md) | `FIELD_TRANS_ID` |
| `FILTER_ID` | [ESO_FILTER](ESO_FILTER.md) | `FILTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ESO_FILTER_COND_RELTN](ESO_FILTER_COND_RELTN.md) | `FIELD_FILTER_RELTN_ID` |

