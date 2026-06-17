# CCR_VIEW_SET_RELTN

> Defines the relationship between the VIEW table and the SET table.

**Description:** View Set Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_CHG_FILTER_IND` | DOUBLE | NOT NULL |  | Indication that user may modify filters at runtime |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `IGNORE_ENC_IND` | DOUBLE | NOT NULL |  | Indicates if encounters for this relationship should not be used when reading data. |
| 6 | `PAGE_SIZE` | DOUBLE | NOT NULL |  | A suggested default page size for all data in the set |
| 7 | `PREV_VIEW_SET_RELTN_ID` | DOUBLE | NOT NULL |  | Previous View Set Relation ID - required for versioning |
| 8 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Sequence Number |
| 9 | `SET_ID` | DOUBLE | NOT NULL | FK→ | Set ID - FK from CCR_SET |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VIEW_ID` | DOUBLE | NOT NULL | FK→ | View ID. ID from CCR_VIEW |
| 16 | `VIEW_SET_RELTN_ID` | DOUBLE | NOT NULL |  | Primary key for this table |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SET_ID` | [CCR_SET](CCR_SET.md) | `SET_ID` |
| `VIEW_ID` | [CCR_VIEW](CCR_VIEW.md) | `VIEW_ID` |

