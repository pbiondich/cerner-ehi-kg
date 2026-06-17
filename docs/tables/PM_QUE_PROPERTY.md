# PM_QUE_PROPERTY

> Work queue property.

**Description:** Work queue property.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DATA_TYPE_FLAG` | DOUBLE |  |  | Data type of this column. |
| 4 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of the property. |
| 5 | `DISPLAY` | VARCHAR(100) | NOT NULL |  | Display value of the property. |
| 6 | `DISPLAY_KEY` | VARCHAR(100) | NOT NULL |  | Display key of the property. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `NAME` | VARCHAR(100) | NOT NULL |  | Name of the property. |
| 9 | `PARENT_ID` | DOUBLE | NOT NULL |  | Primary key for the table row associated with the property row. |
| 10 | `PARENT_TABLE` | VARCHAR(32) | NOT NULL |  | Name of the table associated with the property row. |
| 11 | `PROPERTY_ID` | DOUBLE | NOT NULL |  | Primary key. |
| 12 | `REQUIRED_IND` | DOUBLE |  |  | Indicates that the property must be populated before the associated method can be executed. For example, the ACTION property of the PMAction object must be populated before the ACTION method is executed. |
| 13 | `SEQUENCE` | DOUBLE |  |  | Sequence of the property on a given application/method |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

